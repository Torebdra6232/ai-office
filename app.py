import streamlit as st
import os
import time
import json
import requests
from datetime import datetime
from dotenv import load_dotenv
from google import genai
from PIL import Image

# 1. Page Configuration
st.set_page_config(
    page_title="AutoOffice OS - Enterprise Mission Control",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = None
if api_key:
    try:
        client = genai.Client(api_key=api_key)
    except Exception as e:
        st.error(f"Failed to initialize Gemini Client: {e}")

# Isolated Chat Memories for Each Private Room
if "chat_ceo" not in st.session_state:
    st.session_state.chat_ceo = []
if "chat_social" not in st.session_state:
    st.session_state.chat_social = []
if "chat_trading" not in st.session_state:
    st.session_state.chat_trading = []
if "chat_appdev" not in st.session_state:
    st.session_state.chat_appdev = []

# Financial & Dispatch Logs
if "token_ledger" not in st.session_state:
    st.session_state.token_ledger = []
if "webhook_logs" not in st.session_state:
    st.session_state.webhook_logs = []
if "trade_logs" not in st.session_state:
    st.session_state.trade_logs = []

# Daily Mission Control Statuses
if "social_draft" not in st.session_state:
    st.session_state.social_draft = "Campaign Draft: 5 AI Automation Tools that save 20 hrs/week (YouTube Script + 6-part X Thread ready)."
if "trading_setup" not in st.session_state:
    st.session_state.trading_setup = "XAU/USD (Gold) BUY Limit @ 2354.20 | SL: 2348.00 (62 pips) | TP: 2372.00 | Lot: 0.10"
if "app_status" not in st.session_state:
    st.session_state.app_status = "HabitFlow Mobile App: Core React Native auth, SQLite offline cache, and RevenueCat paywalls built."

@st.cache_resource(show_spinner=False)
def discover_active_models():
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
    prompt_tokens = getattr(usage_metadata, "prompt_token_count", 0) or 0
    candidate_tokens = getattr(usage_metadata, "candidates_token_count", 0) or 0
    total_tokens = prompt_tokens + candidate_tokens
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


# -------------------------------------------------------------
# SIDEBAR NAVIGATION
# -------------------------------------------------------------
st.sidebar.title("🏢 AutoOffice OS")
st.sidebar.caption("Autonomous Enterprise Operations")

nav_choice = st.sidebar.radio(
    "NAVIGATION:",
    [
        "📊 Mission Control Dashboard",
        "💬 Private Chat: Social Media (Chloe)",
        "💬 Private Chat: Forex Trading (Ray Dalton)",
        "💬 Private Chat: Executive CEO (Marcus Vance)",
        "🚀 Team Alpha Sprint (Engineering & Code)",
        "🌐 Web Operator (Atlas - Browser Control)",
        "💰 FinOps & Token Auditor (Finley)"
    ],
    index=0
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 👥 Your Active Staff")
st.sidebar.markdown("""
- 👔 **Marcus Vance** — CEO & Lead Strategist
- 📱 **Chloe & Liam** — Social Media & YouTube
- 📊 **Ray Dalton** — Chief Forex Quant & MT5
- 💻 **Devon & Kaelen** — App Architects
- 💰 **Finley** — FinOps Accountant
- 🌐 **Atlas** — Web Operator
""")


# =============================================================
# 1. MISSION CONTROL DASHBOARD (Easy-to-Understand Hub)
# =============================================================
if nav_choice == "📊 Mission Control Dashboard":
    st.title("📊 Mission Control: Daily Operations Hub")
    st.caption("Real-time operational status for your 3 primary business streams.")

    # High-level Metric Strip
    total_cost = sum(item["cost_usd"] for item in st.session_state.token_ledger)
    total_calls = len(st.session_state.token_ledger)

    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.metric(label="📱 Social Content Status", value="Ready to Post", delta="1 Pending")
    with m2:
        st.metric(label="📈 Forex MT5 Desk", value="Active Setup", delta="XAU/USD")
    with m3:
        st.metric(label="📲 Commercial App Lab", value="In Build", delta="React Native")
    with m4:
        st.metric(label="💰 Today's Token Spend", value=f"${total_cost:.4f}", delta=f"{total_calls} calls")

    st.markdown("---")

    # 3 Easy-To-Understand Operations Cards
    col1, col2, col3 = st.columns(3)

    # CARD 1: SOCIAL MEDIA
    with col1:
        st.subheader("📱 1. Social Media Hub")
        st.markdown("**Channels:** YouTube, Instagram, Facebook, X")
        st.info(f"**Latest Deliverable:**\n{st.session_state.social_draft[:140]}...")
        st.markdown("**Status:** 🟢 `Ready for Approval`")
        st.caption("Want changes? Open your **Private Chat with Chloe** to rewrite hooks or slides before posting!")

    # CARD 2: FOREX TRADING
    with col2:
        st.subheader("📈 2. Forex MT5 Desk")
        st.markdown("**Market:** MetaTrader 5 (24/5 Automated)")
        st.success(f"**Active Setup:**\n{st.session_state.trading_setup}")
        st.markdown("**Status:** 🟢 `Setup Verified`")
        st.caption("Need to adjust risk or Stop-Loss? Open your **Private Chat with Ray Dalton** before firing orders!")

    # CARD 3: APP DEV
    with col3:
        st.subheader("📲 3. Commercial App Lab")
        st.markdown("**Targets:** Apple App Store & Google Play")
        st.warning(f"**Current Sprint:**\n{st.session_state.app_status[:140]}...")
        st.markdown("**Status:** 🔵 `Code Generated`")
        st.caption("Review architecture, monetization models, and native code in **Team Alpha Sprint**.")

    st.markdown("---")
    st.subheader("⚡ Quick Executive Actions")
    q1, q2 = st.columns(2)
    with q1:
        if st.button("📋 Generate Marcus's Daily Morning Standup", type="primary", use_container_width=True):
            with st.spinner("Compiling cross-department standup briefing..."):
                brief_prompt = f"""
Social State: {st.session_state.social_draft}
Forex State: {st.session_state.trading_setup}
App State: {st.session_state.app_status}
Provide a crisp 4-bullet executive standup for the founder.
"""
                standup = safe_generate_content(brief_prompt, "You are Marcus Vance, CEO. Deliver a concise 4-bullet standup.", agent_name="Marcus (CEO)")
                st.markdown(standup)
    with q2:
        if st.button("🧹 Clear All Stored Drafts & Reset", use_container_width=True):
            st.session_state.social_draft = "No pending draft."
            st.session_state.trading_setup = "No active trade."
            st.rerun()


# =============================================================
# 2. PRIVATE CHAT: SOCIAL MEDIA TEAM (Chloe & Liam)
# =============================================================
elif nav_choice == "💬 Private Chat: Social Media (Chloe)":
    st.title("💬 Private War Room: Social Media Team")
    st.caption("Talk directly with Chloe (Social Lead) & Liam (YouTube). Review drafts, request tweaks, and approve posts!")

    # Top Action Bar
    t_c1, t_c2 = st.columns([3, 1])
    with t_c1:
        st.markdown(f"**Current Working Draft:** `{st.session_state.social_draft[:90]}...`")
    with t_c2:
        if st.button("🧹 Clear Chat History"):
            st.session_state.chat_social = []
            st.rerun()

    st.markdown("---")

    # Render Chat History
    for role, msg in st.session_state.chat_social:
        with st.chat_message(role, avatar="📱" if role == "assistant" else "👤"):
            st.markdown(msg)

    social_input = st.chat_input("Tell Chloe: 'Make the YouTube hook punchier', 'Rewrite for Instagram carousel', etc...")
    if social_input:
        st.session_state.chat_social.append(("user", social_input))
        with st.chat_message("user", avatar="👤"):
            st.markdown(social_input)

        chloe_system = (
            "You are Chloe, Head of Social Media, working alongside Liam Cole (YouTube Producer). "
            "You help the user review, write, edit, and polish high-converting content for YouTube, Instagram, Facebook, and Twitter/X. "
            "When the user requests changes, rewrite the content precisely as asked with hooks, captions, and slide layouts. "
            "Be energetic, professional, and trend-aware."
        )

        with st.chat_message("assistant", avatar="📱"):
            with st.spinner("Chloe is updating your content..."):
                reply = safe_generate_content(social_input, system_instruction=chloe_system, agent_name="Chloe (Social Team)")
                st.markdown(reply)
                st.session_state.chat_social.append(("assistant", reply))
                st.session_state.social_draft = reply

    # Direct Webhook Dispatcher
    st.markdown("---")
    st.subheader("🚀 1-Click Dispatch to Live Social Media")
    st.caption("Once you are happy with the draft above, dispatch it to your Make.com, Zapier, or Buffer webhook!")

    webhook_url = st.text_input("Webhook URL:", placeholder="https://hook.make.com/your-live-social-hook")
    if st.button("⚡ Dispatch Approved Draft Now", type="primary"):
        if not webhook_url.strip():
            st.warning("Please paste your Webhook URL above.")
        else:
            try:
                res = requests.post(webhook_url, json={"content": st.session_state.social_draft, "time": datetime.now().isoformat()}, timeout=8)
                st.success(f"✅ Dispatched successfully! Status code: {res.status_code}")
                st.session_state.webhook_logs.append({"time": datetime.now().strftime("%H:%M:%S"), "status": "Dispatched", "code": res.status_code})
            except Exception as e:
                st.error(f"❌ Failed to reach Webhook: {e}")


# =============================================================
# 3. PRIVATE CHAT: FOREX TRADING (Ray Dalton)
# =============================================================
elif nav_choice == "💬 Private Chat: Forex Trading (Ray Dalton)":
    st.title("💬 Private Desk: Ray Dalton (Forex & MT5)")
    st.caption("Direct consultation with your Chief Quantitative Analyst. Adjust Stop-Loss, recalculate lot sizes, and review chart setups.")

    t_r1, t_r2 = st.columns([3, 1])
    with t_r1:
        st.markdown(f"**Current Trade Setup:** `{st.session_state.trading_setup}`")
    with t_r2:
        if st.button("🧹 Clear Desk History"):
            st.session_state.chat_trading = []
            st.rerun()

    st.markdown("---")

    for role, msg in st.session_state.chat_trading:
        with st.chat_message(role, avatar="📈" if role == "assistant" else "👤"):
            st.markdown(msg)

    trade_input = st.chat_input("Ask Ray: 'Tighten the Stop-Loss on Gold', 'What if CPI news drops today?', 'Calculate lot for $5k'...")
    if trade_input:
        st.session_state.chat_trading.append(("user", trade_input))
        with st.chat_message("user", avatar="👤"):
            st.markdown(trade_input)

        ray_system = (
            "You are Ray Dalton, veteran institutional Forex trader and quantitative analyst. "
            "You manage 24/5 automated MetaTrader 5 setups for EURUSD, GBPUSD, and XAUUSD (Gold). "
            "When the user asks to adjust trade parameters (Stop-Loss, Take-Profit, lot sizing, invalidation levels), "
            "calculate exact price points and risk percentages. Be disciplined, risk-first, and concise."
        )

        with st.chat_message("assistant", avatar="📈"):
            with st.spinner("Ray is analyzing the market parameters..."):
                reply = safe_generate_content(trade_input, system_instruction=ray_system, agent_name="Ray Dalton (Forex)")
                st.markdown(reply)
                st.session_state.chat_trading.append(("assistant", reply))
                st.session_state.trading_setup = reply

    # Direct MT5 Execution
    st.markdown("---")
    st.subheader("⚡ Fire Approved Order to MT5 Bridge")
    st.caption("Send this trade order to your local or VPS MetaTrader 5 Webhook EA.")

    mt5_url = st.text_input("MT5 Bridge URL:", placeholder="http://your-vps-ip:5000/trade")
    if st.button("🚀 Fire Order to MT5", type="primary"):
        if not mt5_url.strip():
            st.warning("Please provide your MT5 Bridge URL.")
        else:
            try:
                res = requests.post(mt5_url, json={"trade": st.session_state.trading_setup, "time": datetime.now().isoformat()}, timeout=6)
                st.success(f"✅ Order fired to MT5! Response: {res.status_code}")
                st.session_state.trade_logs.append({"time": datetime.now().strftime("%H:%M:%S"), "status": "Sent to MT5"})
            except Exception as e:
                st.error(f"❌ Could not reach MT5 Bridge: {e}")


# =============================================================
# 4. PRIVATE CHAT: EXECUTIVE CEO (Marcus Vance)
# =============================================================
elif nav_choice == "💬 Private Chat: Executive CEO (Marcus Vance)":
    st.title("💬 Private Suite: Marcus Vance (CEO)")
    st.caption("High-level strategic consultation, multi-team directives, and business roadmaps.")

    c_b1, c_b2 = st.columns([3, 1])
    with c_b2:
        if st.button("🧹 Clear CEO Chat"):
            st.session_state.chat_ceo = []
            st.rerun()

    st.markdown("---")

    for role, msg in st.session_state.chat_ceo:
        with st.chat_message(role, avatar="👔" if role == "assistant" else "👤"):
            st.markdown(msg)

    ceo_input = st.chat_input("Talk to Marcus Vance about your company roadmap...")
    if ceo_input:
        st.session_state.chat_ceo.append(("user", ceo_input))
        with st.chat_message("user", avatar="👤"):
            st.markdown(ceo_input)

        with st.chat_message("assistant", avatar="👔"):
            with st.spinner("Marcus is evaluating..."):
                reply = safe_generate_content(ceo_input, "You are Marcus Vance, decisive CEO of AutoOffice OS.", agent_name="Marcus (CEO)")
                st.markdown(reply)
                st.session_state.chat_ceo.append(("assistant", reply))


# =============================================================
# 5. TEAM ALPHA SPRINT (Engineering & App Dev)
# =============================================================
elif nav_choice == "🚀 Team Alpha Sprint (Engineering & Code)":
    st.title("🚀 Team Alpha: Commercial App Development Lab")
    st.caption("Kaelen Frost (App Architect), Devon Brooks (Code), and Tariq Chen (DevOps) build complete commercial software.")

    app_idea = st.text_area("Commercial App Concept:", placeholder="e.g. Offline-first habit & subscription tracker with RevenueCat paywalls and iOS widgets.")
    framework = st.selectbox("Framework:", ["React Native / Expo (iOS & Android)", "Flutter / Dart", "SwiftUI Native iOS", "PWA Next.js"])

    if st.button("⚡ Build Complete App Package", type="primary"):
        if not app_idea.strip():
            st.warning("Please describe your app idea.")
        else:
            with st.status("🚀 Team Alpha is building your software package...", expanded=True) as status:
                prompt = f"App: {app_idea}\nFramework: {framework}\nProvide full screen breakdown, RevenueCat paywall integration, production source code, and App Store submission guide."
                app_out = safe_generate_content(prompt, "You are Kaelen Frost and Devon Brooks, mobile architects.", agent_name="Kaelen (App Dev)")
                status.update(label="✅ App Package Built!", state="complete")
            st.markdown(app_out)
            st.session_state.app_status = f"App Built: {app_idea[:60]} ({framework})"


# =============================================================
# 6. WEB OPERATOR (Atlas - Browser Control)
# =============================================================
elif nav_choice == "🌐 Web Operator (Atlas - Browser Control)":
    st.title("🌐 Atlas: Autonomous Web & Browser Operator")
    st.caption("Direct Atlas to inspect sites, fill form inputs, and click buttons.")

    url = st.text_input("Target URL:", placeholder="https://example.com")
    action = st.text_area("Directive:", placeholder="e.g. Type 'AI Multi-Agent' into search bar and click Submit.")

    if st.button("🤖 Run Web Operator Plan", type="primary"):
        if url and action:
            with st.status("🌐 Atlas is mapping DOM elements...", expanded=True) as status:
                prompt = f"Target: {url}\nAction: {action}\nProvide Action Sequence, CSS/XPath Selectors, and executable Playwright Python script."
                out = safe_generate_content(prompt, "You are Atlas, autonomous browser operator.", agent_name="Atlas (Web Operator)")
                status.update(label="✅ Automation Script Ready!", state="complete")
            st.markdown(out)


# =============================================================
# 7. FINOPS & TOKEN AUDITOR (Finley)
# =============================================================
elif nav_choice == "💰 FinOps & Token Auditor (Finley)":
    st.title("💰 Finley: Corporate Accountant & Token Auditor")
    st.caption("Live cost tracking across all your teams, chats, and automated dispatches.")

    ledger = st.session_state.token_ledger
    total_tokens = sum(item["total_tokens"] for item in ledger)
    total_cost = sum(item["cost_usd"] for item in ledger)
    total_calls = len(ledger)

    f1, f2, f3, f4 = st.columns(4)
    with f1: st.metric("Total Spent", f"${total_cost:.5f} USD")
    with f2: st.metric("Total Tokens", f"{total_tokens:,}")
    with f3: st.metric("API Calls", f"{total_calls}")
    with f4:
        avg = (total_cost / total_calls) if total_calls > 0 else 0
        st.metric("Avg / Call", f"${avg:.5f}")

    st.markdown("---")
    st.subheader("📜 Live Ledger")
    if ledger:
        st.dataframe(ledger, use_container_width=True)
    else:
        st.info("No API transactions recorded in this session yet.")
