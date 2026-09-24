import streamlit as st
import os
import time
from datetime import datetime
from dotenv import load_dotenv
from google import genai
from PIL import Image

# 1. Page Configuration
st.set_page_config(
    page_title="AutoOffice OS - Multi-Task Enterprise Dashboard",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

# Initialize Google GenAI client
client = None
if api_key:
    try:
        client = genai.Client(api_key=api_key)
    except Exception as e:
        st.error(f"Failed to initialize Gemini Client: {e}")

# Global Session State for Accounting, Tasks & Chat
if "token_ledger" not in st.session_state:
    st.session_state.token_ledger = []
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Pre-seeded Daily Task Dashboard
if "tasks" not in st.session_state:
    st.session_state.tasks = [
        {
            "id": "TSK-01",
            "team": "📱 Social Media Team",
            "title": "Weekly Content Engine (YouTube Script & X Thread)",
            "platform": "YouTube & Twitter/X",
            "status": "⚡ In Progress",
            "updated": "Today 09:15",
            "output": "Drafting viral script on '5 AI tools replacing entire agencies' + 8-part tweet breakdown."
        },
        {
            "id": "TSK-02",
            "team": "📈 Trading & Markets Team",
            "title": "BTC & ETH Liquidity Sweep Analysis + Gold (XAU/USD)",
            "platform": "Crypto & Forex",
            "status": "✅ Ready for Review",
            "updated": "Today 08:30",
            "output": "Bullish divergence identified on 4H chart. Key support held at $64,200. Risk/Reward ratio 1:3.2."
        },
        {
            "id": "TSK-03",
            "team": "📲 App Development Team",
            "title": "SaaS Habit & Micro-Journaling App for iOS/Android",
            "platform": "App Store & Play Store",
            "status": "⚡ In Progress",
            "updated": "Today 10:00",
            "output": "Kaelen & Devon building React Native auth flow, local SQLite caching, and RevenueCat subscription tiers."
        }
    ]

@st.cache_resource(show_spinner=False)
def discover_active_models():
    """Dynamically asks Google's API which models are actively available."""
    defaults = ["gemini-3.1-pro-preview", "gemini-2.5-flash", "gemini-2.5-flash-lite"]
    if not client:
        return defaults
    try:
        discovered = []
        for m in client.models.list():
            raw_name = getattr(m, "name", "")
            name = raw_name.replace("models/", "")
            if "gemini" in name.lower() and not any(legacy in name for legacy in ["1.5", "2.0"]):
                discovered.append(name)
        ordered = [m for m in defaults if m in discovered]
        for m in discovered:
            if m not in ordered:
                ordered.append(m)
        return ordered if ordered else defaults
    except Exception:
        return defaults

def record_token_usage(agent_name, model_name, usage_metadata):
    """Logs token usage and cost for Finley the Accountant."""
    prompt_tokens = getattr(usage_metadata, "prompt_token_count", 0) or 0
    candidate_tokens = getattr(usage_metadata, "candidates_token_count", 0) or 0
    total_tokens = prompt_tokens + candidate_tokens
    
    # Blended estimate: ~$0.15/1M input, ~$0.60/1M output
    cost_usd = (prompt_tokens * 0.00000015) + (candidate_tokens * 0.00000060)

    st.session_state.token_ledger.append({
        "timestamp": datetime.now().strftime("%H:%M:%S"),
        "agent": agent_name,
        "model": model_name,
        "prompt_tokens": prompt_tokens,
        "output_tokens": candidate_tokens,
        "total_tokens": total_tokens,
        "cost_usd": cost_usd
    })

def safe_generate_content(prompt_or_contents, system_instruction=None, agent_name="AI Agent", max_retries=2):
    """Resilient generation with auto-retry and automated accounting logging."""
    if not client:
        return "⚠️ Please set your `GEMINI_API_KEY` in Streamlit Secrets or your .env file."

    models_to_try = discover_active_models()
    last_error = ""

    for model_name in models_to_try:
        for attempt in range(max_retries + 1):
            try:
                config = {}
                if system_instruction:
                    config["system_instruction"] = system_instruction

                response = client.models.generate_content(
                    model=model_name,
                    contents=prompt_or_contents,
                    config=config if config else None
                )
                if response and response.text:
                    if hasattr(response, "usage_metadata") and response.usage_metadata:
                        record_token_usage(agent_name, model_name, response.usage_metadata)
                    return response.text
            except Exception as e:
                err_str = str(e)
                last_error = err_str
                if any(code in err_str for code in ["503", "UNAVAILABLE", "429", "RESOURCE_EXHAUSTED"]):
                    time.sleep(1.5 * (attempt + 1))
                    continue
                else:
                    break

    return f"⚠️ Service notice: AI agents are momentarily resting. Please try again. (Details: {last_error})"


# 2. Sidebar Navigation
st.sidebar.title("🏢 AutoOffice OS")
st.sidebar.caption("Autonomous Multi-Task Enterprise")

mode = st.sidebar.radio(
    "Select Workstation:",
    [
        "📊 Mission Control & Task Board",
        "📱 Task 1: Social Media Team (YT, IG, FB, X)",
        "📈 Task 2: Trading Team (Stocks, Forex, Crypto)",
        "📲 Task 3: App Store Dev Team (Commercial Apps)",
        "🌐 Web Operator (Atlas - Browser Control)",
        "💬 Executive Suite (Marcus Vance, CEO)",
        "💰 Accountant & FinOps (Finley - Cost Tracker)"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 👥 Enterprise Staff (10 Agents)")
st.sidebar.markdown("""
**Executive & Management:**
- 👔 **Marcus Vance** — CEO & Chief Strategist
- 💰 **Finley** — Accountant & Token Cost Auditor
- 🌐 **Atlas** — Web & Browser Operator

**Task 1: Social Media Team:**
- 📱 **Chloe** — Head of Social Media (IG/TikTok/X)
- 🎬 **Liam Cole** — YouTube Strategist & Video Producer
- 📈 **Maya Lin** — Conversion & Community Copywriter

**Task 2: Trading Team:**
- 📊 **Ray Dalton** — Chief Quantitative Market Analyst
- 🛡️ **Marcus Vance** — Risk & Capital Sizing

**Task 3: App Development Team:**
- 📲 **Kaelen Frost** — Principal App Store Architect
- 💻 **Devon Brooks** — Senior Mobile & Full-Stack Engineer
- 🛡️ **Tariq Chen** — Security & App Store Compliance
""")


# =============================================================
# 1. MISSION CONTROL & TASK DASHBOARD (Overview Board)
# =============================================================
if mode == "📊 Mission Control & Task Board":
    st.header("📊 Mission Control: Daily Operations Board")
    st.caption("Live status, active pipelines, and task updates across your 3 primary business operations.")

    # Top KPI Metrics
    ledger = st.session_state.token_ledger
    total_cost = sum(item["cost_usd"] for item in ledger)
    active_count = len([t for t in st.session_state.tasks if "Progress" in t["status"]])
    ready_count = len([t for t in st.session_state.tasks if "Ready" in t["status"]])

    k1, k2, k3, k4 = st.columns(4)
    with k1:
        st.metric("Active Daily Tasks", f"{len(st.session_state.tasks)}")
    with k2:
        st.metric("Sprints in Progress", f"{active_count}", delta="Live" if active_count > 0 else "Idle")
    with k3:
        st.metric("Deliverables Ready", f"{ready_count}", delta="Ready")
    with k4:
        st.metric("Today's Token Spend", f"${total_cost:.4f} USD")

    st.markdown("---")

    # Quick Executive Action
    col_dash1, col_dash2 = st.columns([3, 1])
    with col_dash1:
        st.subheader("📋 Real-Time Operations Board")
    with col_dash2:
        if st.button("⚡ Executive Status Briefing", type="primary", use_container_width=True):
            with st.spinner("Marcus Vance is compiling your 3-team daily briefing..."):
                brief_prompt = f"""
Current Active Tasks on Board:
{st.session_state.tasks}

Provide an executive morning standup briefing:
1. Status of Social Media Team (YouTube, Instagram, Facebook, X)
2. Status of Trading & Markets Team (Positions, Setups, Risk)
3. Status of App Store Commercial Dev Team (Build progress & release target)
4. Marcus's direct command for today's priority focus.
"""
                briefing = safe_generate_content(brief_prompt, "You are Marcus Vance, CEO. Deliver a punchy executive standup briefing.", agent_name="Marcus (CEO)")
                st.info(briefing)

    # Render Task Cards
    for task in st.session_state.tasks:
        with st.container():
            t_col1, t_col2, t_col3, t_col4 = st.columns([1, 3, 2, 2])
            with t_col1:
                st.markdown(f"**`{task['id']}`**")
            with t_col2:
                st.markdown(f"**{task['title']}**\n\n*{task['team']}*")
            with t_col3:
                st.markdown(f"🎯 **Platform/Target:** `{task['platform']}`\n\n🕒 **Updated:** {task['updated']}")
            with t_col4:
                status_color = "🟢" if "Ready" in task["status"] else "🟡"
                st.markdown(f"**Status:** {status_color} {task['status']}")
            
            with st.expander(f"🔍 View Latest Output & Deliverable ({task['id']})"):
                st.markdown(task["output"])
            st.divider()


# =============================================================
# 2. TASK 1: SOCIAL MEDIA TEAM (YouTube, IG, FB, X)
# =============================================================
elif mode == "📱 Task 1: Social Media Team (YT, IG, FB, X)":
    st.header("📱 Social Media Team: Cross-Platform Campaign Hub")
    st.caption("Chloe (Head of Social), Liam Cole (YouTube Producer), and Maya Lin (Copywriter)")

    platforms_selected = st.multiselect(
        "Select Channels for this Sprint:",
        ["YouTube (Video Script & Title)", "Twitter/X (Viral Thread & Hooks)", "Instagram (Carousel & Reel Script)", "Facebook (Ad Copy & Community Post)"],
        default=["YouTube (Video Script & Title)", "Twitter/X (Viral Thread & Hooks)"]
    )

    campaign_brief = st.text_area(
        "Campaign Objective or Content Topic:",
        placeholder="e.g. Announcing our new productivity app launch; share 5 actionable tips on mastering daily deep work."
    )

    if st.button("🚀 Launch Social Media Campaign Sprint", type="primary"):
        if not campaign_brief.strip():
            st.warning("Please provide a content topic or campaign objective.")
        else:
            with st.status("📱 Social Media Team is producing multi-channel assets...", expanded=True) as status:
                status.update(label="📱 Chloe is developing cross-platform hooks & publishing schedule...")
                time.sleep(1)

                prompt = f"""
Campaign Topic: {campaign_brief}
Channels: {', '.join(platforms_selected)}

Provide:
1. 🎬 **YouTube Content** (if selected): 3 High-CTR Titles, Thumbnail Visual Concept, Hook Script (First 30 seconds), and Video Chapter Outline.
2. 🐦 **Twitter/X Thread** (if selected): Irresistible hook tweet, 5 value body tweets, and strong CTA tweet.
3. 📸 **Instagram Deliverables** (if selected): 5-slide carousel layout & Reel video script with visual cues.
4. 📘 **Facebook Strategy** (if selected): Engaging storytelling post + conversion-focused ad copy.
5. 📅 **Recommended Posting Schedule**: Optimal posting days and times.
"""
                social_output = safe_generate_content(prompt, "You are Chloe & Liam Cole, elite social media directors. Deliver viral, platform-native content.", agent_name="Chloe (Social Team)")
                status.update(label="✅ Social Media Content Ready!", state="complete")

            st.markdown(social_output)

            # Auto-update Task Board
            new_task = {
                "id": f"TSK-0{len(st.session_state.tasks)+1}",
                "team": "📱 Social Media Team",
                "title": f"Campaign: {campaign_brief[:40]}...",
                "platform": ", ".join(platforms_selected),
                "status": "✅ Ready for Review",
                "updated": datetime.now().strftime("%H:%M"),
                "output": social_output
            }
            st.session_state.tasks.insert(0, new_task)
            st.success("✅ Added to Mission Control Task Dashboard!")


# =============================================================
# 3. TASK 2: TRADING TEAM (Stocks, Forex, Crypto)
# =============================================================
elif mode == "📈 Task 2: Trading Team (Stocks, Forex, Crypto)":
    st.header("📈 Trading & Market Intelligence Team")
    st.caption("Ray Dalton (Chief Quantitative Analyst) & Marcus Vance (Risk & Capital Allocation)")

    market_type = st.selectbox("Asset Class:", ["Crypto (e.g. BTC, ETH, SOL)", "Stocks / Indices (e.g. NVDA, TSLA, SPY, QQQ)", "Forex (e.g. EUR/USD, GBP/JPY, XAU/USD Gold)"])
    ticker = st.text_input("Ticker / Pair:", placeholder="e.g. BTC/USDT, NVDA, or XAU/USD")
    timeframe = st.select_slider("Analysis Timeframe:", options=["15M (Scalp)", "1H (Intraday)", "4H (Swing)", "1D (Position)"], value="4H (Swing)")

    trade_context = st.text_area(
        "Current Market Observations or Specific Question:",
        placeholder="e.g. Price broke above key $68,000 resistance with heavy volume; looking for retest entry and risk parameters."
    )

    if st.button("📊 Run Technical & Trade Setup Analysis", type="primary"):
        if not ticker.strip():
            st.warning("Please specify a ticker or trading pair.")
        else:
            with st.status(f"📈 Ray Dalton is analyzing {ticker} on {timeframe}...", expanded=True) as status:
                status.update(label=f"🔍 Scanning liquidity pools, support/resistance, and risk parameters...")
                
                trade_prompt = f"""
Asset: {ticker} ({market_type})
Timeframe: {timeframe}
Trader Notes: {trade_context}

Provide a professional trading desk briefing:
1. 🎯 **Market Structure & Trend Bias**: Current trend (Bullish, Bearish, or Ranging) and pivotal price levels (Support & Resistance).
2. ⚡ **Actionable Trade Setup**:
   - Ideal Entry Zone
   - Stop-Loss (Invalidation level)
   - Take-Profit 1, 2, and 3
   - Risk/Reward Ratio (Must be minimum 1:2.5)
3. ⚠️ **Risk Management & Position Sizing**: Capital preservation rules and critical invalidation conditions.
4. 📰 **Macro & Catalyst Watch**: Key upcoming economic data or news catalysts to monitor.
"""
                trade_output = safe_generate_content(trade_prompt, "You are Ray Dalton, veteran prop firm trader and quant analyst. Deliver disciplined, risk-first trade analysis.", agent_name="Ray Dalton (Trading)")
                status.update(label="✅ Trade Analysis & Setup Complete!", state="complete")

            st.markdown(trade_output)

            # Auto-update Task Board
            new_task = {
                "id": f"TSK-0{len(st.session_state.tasks)+1}",
                "team": "📈 Trading & Markets Team",
                "title": f"Trade Plan: {ticker} ({timeframe})",
                "platform": market_type,
                "status": "✅ Ready for Review",
                "updated": datetime.now().strftime("%H:%M"),
                "output": trade_output
            }
            st.session_state.tasks.insert(0, new_task)
            st.success("✅ Trade Setup logged to Mission Control Task Dashboard!")


# =============================================================
# 4. TASK 3: APP STORE COMMERCIAL DEV TEAM
# =============================================================
elif mode == "📲 Task 3: App Store Dev Team (Commercial Apps)":
    st.header("📲 Commercial App Development Team (App Store & Google Play)")
    st.caption("Kaelen Frost (App Store Architect), Devon Brooks (Senior Engineer), and Tariq Chen (Compliance)")

    app_name = st.text_input("Application Name or Project Codename:", placeholder="e.g. ZenTimer - Focus & Revenue Tracker for Creators")
    tech_stack = st.selectbox("Preferred Framework / Stack:", ["React Native / Expo (iOS & Android)", "Flutter / Dart (Cross-Platform)", "Swift / SwiftUI (Native iOS)", "Progressive Web App (PWA / Next.js)"])
    monetization = st.multiselect("Monetization Model:", ["Freemium + In-App Subscriptions (Weekly/Monthly)", "One-Time Pro Unlock", "Consumable Credits / Tokens"], default=["Freemium + In-App Subscriptions (Weekly/Monthly)"])

    app_spec = st.text_area(
        "Application Concept & Core Features to Build:",
        placeholder="e.g. Offline-first habit tracking app with streak widgets, soundscapes, and RevenueCat paywall integration."
    )

    if st.button("🚀 Build Commercial App Specification & Code", type="primary"):
        if not app_spec.strip():
            st.warning("Please describe the application concept and core features.")
        else:
            with st.status("📲 Commercial App Team is executing the build sprint...", expanded=True) as status:
                status.update(label="🏛️ Kaelen Frost is architecting the App Store pipeline and monetization...")
                time.sleep(1)

                app_prompt = f"""
App Name: {app_name}
Framework: {tech_stack}
Monetization: {', '.join(monetization)}
Core Features: {app_spec}

Provide a complete commercial software delivery package:
1. 📱 **Product Architecture & Screen Flow**: Complete user journey and screen-by-screen breakdown.
2. 💰 **In-App Purchase (IAP) & Paywall Blueprint**: Subscription pricing tiers, trial hook, and paywall trigger points.
3. 💻 **Production Source Code**: Core component/screen implementation code with clean comments, state management, and modern styling.
4. 🍏 **App Store & Google Play Submission Checklist**: Required permissions, privacy guidelines, metadata keywords, and rejection pitfalls to avoid.
"""
                dev_output = safe_generate_content(app_prompt, "You are Kaelen Frost and Devon Brooks, top commercial mobile app architects. Deliver high-value, production-grade app deliverables.", agent_name="Kaelen (App Dev)")
                status.update(label="✅ Commercial App Package Completed!", state="complete")

            st.markdown(dev_output)

            # Auto-update Task Board
            new_task = {
                "id": f"TSK-0{len(st.session_state.tasks)+1}",
                "team": "📲 App Development Team",
                "title": f"App Build: {app_name or 'Commercial App'}",
                "platform": "iOS & Android",
                "status": "⚡ In Progress",
                "updated": datetime.now().strftime("%H:%M"),
                "output": dev_output
            }
            st.session_state.tasks.insert(0, new_task)
            st.success("✅ Commercial App logged to Mission Control Task Dashboard!")


# =============================================================
# 5. WEB OPERATOR (Atlas - Browser Control)
# =============================================================
elif mode == "🌐 Web Operator (Atlas - Browser Control)":
    st.header("🌐 Atlas: Autonomous Web & Browser Operator")
    st.caption("Direct Atlas to navigate websites, fill forms, click buttons, and extract information.")

    target_url = st.text_input("Target Website URL:", placeholder="https://example.com/login or https://news.ycombinator.com")
    action_directive = st.text_area("Directive (What should Atlas click or fill?):", placeholder="e.g. Type 'Next.js SaaS' into the search input and click Submit.")

    if st.button("🤖 Execute Web Operation", type="primary"):
        if not target_url.strip() or not action_directive.strip():
            st.warning("Please provide both Target URL and Directive.")
        else:
            with st.status("🌐 Atlas is executing browser automation plan...", expanded=True) as status:
                prompt = f"""
Target Website: {target_url}
Action: {action_directive}

Provide:
1. 📋 **Action Plan**: Detailed browser click & fill sequence.
2. 🎯 **DOM Elements**: Target CSS/XPath selectors for inputs & buttons.
3. 💻 **Playwright Automation Script**: Production Python script to execute this task headlessly.
4. ✅ **Verification**: Check criteria for success.
"""
                out = safe_generate_content(prompt, "You are Atlas, elite Autonomous Browser Operator.", agent_name="Atlas (Web Operator)")
                status.update(label="✅ Web Operation Plan Ready!", state="complete")
            st.markdown(out)


# =============================================================
# 6. EXECUTIVE SUITE (Marcus Vance, CEO)
# =============================================================
elif mode == "💬 Executive Suite (Marcus Vance, CEO)":
    st.header("👔 Executive War Room: Marcus Vance (CEO)")
    st.caption("Direct strategic consultation across all 3 teams with Marcus.")

    for role, msg in st.session_state.chat_history:
        with st.chat_message(role, avatar="👔" if role == "assistant" else "👤"):
            st.markdown(msg)

    user_input = st.chat_input("Ask Marcus for high-level direction on Social Media, Trading, or App Development...")
    if user_input:
        st.session_state.chat_history.append(("user", user_input))
        with st.chat_message("user", avatar="👤"):
            st.markdown(user_input)

        with st.chat_message("assistant", avatar="👔"):
            with st.spinner("Marcus is reviewing..."):
                reply = safe_generate_content(user_input, "You are Marcus Vance, CEO. Provide decisive strategic advice.", agent_name="Marcus (CEO)")
                st.markdown(reply)
                st.session_state.chat_history.append(("assistant", reply))


# =============================================================
# 7. ACCOUNTANT & FINOPS (Finley - Cost Tracker)
# =============================================================
elif mode == "💰 Accountant & FinOps (Finley - Cost Tracker)":
    st.header("💰 Finley: Corporate Accountant & Token Auditor")
    st.caption("Live cost oversight across all 3 daily task tracks.")

    ledger = st.session_state.token_ledger
    total_tokens = sum(item["total_tokens"] for item in ledger)
    total_cost = sum(item["cost_usd"] for item in ledger)
    total_calls = len(ledger)

    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("Total Spent", f"${total_cost:.5f} USD")
    with c2: st.metric("Total Tokens", f"{total_tokens:,}")
    with c3: st.metric("API Invocations", f"{total_calls}")
    with c4:
        avg = (total_cost / total_calls) if total_calls > 0 else 0
        st.metric("Avg / Task Call", f"${avg:.5f}")

    st.markdown("---")
    st.subheader("📜 Live Multi-Team Expense Ledger")
    if ledger:
        st.dataframe(ledger, use_container_width=True)
    else:
        st.info("No API transactions logged yet. Launch a sprint in any team to populate live cost metrics!")
