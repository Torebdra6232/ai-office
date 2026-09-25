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
    page_title="AutoOffice OS - Multi-Agent Enterprise Suite",
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

# =============================================================
# PERSISTENT STORAGE (Saves to disk so chats & tasks never vanish)
# =============================================================
MEMORY_FILE = "autooffice_memory.json"

def load_persistent_memory():
    defaults = {
        "chat_ceo": [],
        "chat_social": [],
        "chat_trading": [],
        "chat_engineering": [],
        "chat_design": [],
        "tasks": [
            {
                "id": "TSK-01",
                "team": "📱 Social Media Team",
                "title": "Cross-Platform Video & Thread Engine",
                "platform": "YouTube, Instagram, Facebook, X",
                "status": "⚡ Ready to Dispatch",
                "updated": "Today 09:15",
                "output": "1 YouTube script + 3 carousel slides + 6 tweet hooks ready for webhook."
            },
            {
                "id": "TSK-02",
                "team": "📈 Forex Trading Team",
                "title": "XAU/USD (Gold) & EUR/USD Automated Setups",
                "platform": "MetaTrader 5 (MT5)",
                "status": "⚡ Ready to Execute",
                "updated": "Today 08:30",
                "output": "XAU/USD BUY Limit @ 2354.20 | SL: 2348.00 | TP: 2372.00 | Lot: 0.10"
            },
            {
                "id": "TSK-03",
                "team": "📲 App Development Team",
                "title": "SaaS Habit Tracker with In-App Subscriptions",
                "platform": "iOS & Android (React Native)",
                "status": "⚡ In Progress",
                "updated": "Today 10:00",
                "output": "Elena (Architecture), Devon (Code), and Sora (UI/UX) built core flow and paywalls."
            }
        ],
        "social_draft": "Campaign Draft: 5 AI Automation Tools that save 20 hrs/week (YouTube Script + 6-part X Thread ready).",
        "trading_setup": "XAU/USD (Gold) BUY Limit @ 2354.20 | SL: 2348.00 (62 pips) | TP: 2372.00 | Lot: 0.10",
        "app_status": "HabitFlow Mobile App: Core React Native auth, SQLite offline cache, and RevenueCat paywalls built.",
        "token_ledger": []
    }
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                for k, v in defaults.items():
                    if k not in data:
                        data[k] = v
                return data
        except Exception:
            return defaults
    return defaults

def save_persistent_memory():
    data = {
        "chat_ceo": st.session_state.get("chat_ceo", []),
        "chat_social": st.session_state.get("chat_social", []),
        "chat_trading": st.session_state.get("chat_trading", []),
        "chat_engineering": st.session_state.get("chat_engineering", []),
        "chat_design": st.session_state.get("chat_design", []),
        "tasks": st.session_state.get("tasks", []),
        "social_draft": st.session_state.get("social_draft", ""),
        "trading_setup": st.session_state.get("trading_setup", ""),
        "app_status": st.session_state.get("app_status", ""),
        "token_ledger": st.session_state.get("token_ledger", [])
    }
    try:
        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Memory save warning: {e}")

# Initialize session state from disk
if "initialized_memory" not in st.session_state:
    saved = load_persistent_memory()
    for k, v in saved.items():
        st.session_state[k] = v
    st.session_state.webhook_logs = []
    st.session_state.trade_logs = []
    st.session_state.initialized_memory = True

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
    save_persistent_memory()

def build_chat_context(history_list, current_input, system_instruction=None):
    """Combines previous conversation history so the agent never forgets past context."""
    full_prompt = ""
    if system_instruction:
        full_prompt += f"System Persona & Directives:\n{system_instruction}\n\n"
    
    if history_list:
        full_prompt += "--- PREVIOUS CONVERSATION HISTORY ---\n"
        for role, text in history_list:
            speaker = "User" if role == "user" else "Assistant"
            full_prompt += f"{speaker}: {text}\n\n"
        full_prompt += "--- END CONVERSATION HISTORY ---\n\n"

    full_prompt += f"User's Latest Message:\n{current_input}\n\nPlease respond to the user, taking into full account the entire conversation above."
    return full_prompt

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
st.sidebar.caption("Autonomous Multi-Agent Enterprise Suite")

nav_choice = st.sidebar.radio(
    "WORKSPACE NAVIGATION:",
    [
        "📊 Mission Control Dashboard",
        "👔 Executive War Room (Marcus Vance, CEO)",
        "📱 Social Media Command (Chloe & Liam)",
        "📈 Forex MT5 Desk (Ray Dalton)",
        "🏛️ Software Architecture (Elena Rostova)",
        "🎨 UI/UX Design Systems (Sora Takahashi)",
        "💻 Full-Stack Engineering (Devon Brooks)",
        "🚀 Team Alpha Commercial App Sprint",
        "🌐 Web Operator (Atlas - Browser Control)",
        "💰 FinOps & Token Auditor (Finley)"
    ],
    index=0
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 👥 Full Active Staff (10 Agents)")
st.sidebar.markdown("""
**Executive & Management:**
- 👔 **Marcus Vance** — CEO & Chief Strategist
- 💰 **Finley** — Corporate Accountant & Cost Auditor
- 🌐 **Atlas** — Web & Browser Operator

**Social & Growth:**
- 📱 **Chloe** — Head of Social Media (IG/TikTok/X)
- 🎬 **Liam Cole** — YouTube Producer & Video Strategist
- 📈 **Maya Lin** — Conversion & Copywriting Lead

**Trading & Financial Markets:**
- 📊 **Ray Dalton** — Chief Quantitative Analyst & MT5 Architect

**Engineering & Product:**
- 🏛️ **Elena Rostova** — Lead Software Architect
- 🎨 **Sora Takahashi** — Head of UI/UX & Design Systems
- 💻 **Devon Brooks** — Senior Full-Stack Engineer
- 🛡️ **Tariq Chen** — Security & Cloud Compliance Lead
""")


# =============================================================
# 1. MISSION CONTROL DASHBOARD
# =============================================================
if nav_choice == "📊 Mission Control Dashboard":
    st.title("📊 Mission Control: Daily Operations Hub")
    st.caption("Live monitoring and cross-department status across your core business operations.")

    ledger = st.session_state.token_ledger
    total_cost = sum(item["cost_usd"] for item in ledger)
    active_count = len([t for t in st.session_state.tasks if "Progress" in t["status"] or "Execute" in t["status"]])

    m1, m2, m3, m4 = st.columns(4)
    with m1: st.metric("Active Operations", f"{len(st.session_state.tasks)}")
    with m2: st.metric("Live Sprints", f"{active_count}", delta="Running")
    with m3: st.metric("Persistent Memory", "Active 🟢", delta="Auto-Saving")
    with m4: st.metric("Today's Token Spend", f"${total_cost:.4f} USD")

    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.subheader("📱 1. Social Media Hub")
        st.markdown("**Team:** Chloe & Liam Cole")
        st.info(f"**Latest Draft:**\n{st.session_state.social_draft[:130]}...")
        st.caption("Chat with Chloe to tweak copy before posting!")
    with c2:
        st.subheader("📈 2. Forex MT5 Desk")
        st.markdown("**Lead:** Ray Dalton (Quant)")
        st.success(f"**Active Setup:**\n{st.session_state.trading_setup}")
        st.caption("Chat with Ray to adjust Stop-Loss or lot sizing!")
    with c3:
        st.subheader("📲 3. Commercial App Lab")
        st.markdown("**Team:** Elena, Sora, Devon & Tariq")
        st.warning(f"**Active Build:**\n{st.session_state.app_status[:130]}...")
        st.caption("Elena (Architecture) & Devon (Code) ready for sprints!")

    st.markdown("---")
    st.subheader("📋 Active Enterprise Tasks")
    for task in st.session_state.tasks:
        with st.container():
            col_t1, col_t2, col_t3 = st.columns([1, 4, 2])
            with col_t1: st.markdown(f"**`{task['id']}`**")
            with col_t2: st.markdown(f"**{task['title']}**\n\n*{task['team']}*")
            with col_t3: st.markdown(f"**Status:** {task['status']}\n\n🕒 {task['updated']}")
            with st.expander(f"🔍 View Task Details ({task['id']})"):
                st.markdown(task["output"])
            st.divider()


# =============================================================
# 2. EXECUTIVE WAR ROOM (Marcus Vance, CEO)
# =============================================================
elif nav_choice == "👔 Executive War Room (Marcus Vance, CEO)":
    st.title("👔 Executive War Room: Marcus Vance (CEO)")
    st.caption("Direct strategic consultation. Marcus remembers your past discussions across sessions!")

    top_c1, top_c2 = st.columns([3, 1])
    with top_c2:
        if st.button("🧹 Clear Chat"):
            st.session_state.chat_ceo = []
            save_persistent_memory()
            st.rerun()

    st.markdown("---")
    for role, msg in st.session_state.chat_ceo:
        with st.chat_message(role, avatar="👔" if role == "assistant" else "👤"):
            st.markdown(msg)

    ceo_input = st.chat_input("Talk to Marcus Vance (CEO)...")
    if ceo_input:
        st.session_state.chat_ceo.append(("user", ceo_input))
        with st.chat_message("user", avatar="👤"):
            st.markdown(ceo_input)

        marcus_system = (
            "You are Marcus Vance, decisive CEO and Chief Strategist of AutoOffice. "
            "You manage social media growth, 24/5 Forex MT5 auto-trading, and commercial app software pipelines. "
            "You always remember past conversation context. Give structured, direct, confident advice."
        )

        full_prompt = build_chat_context(st.session_state.chat_ceo[:-1], ceo_input, marcus_system)

        with st.chat_message("assistant", avatar="👔"):
            with st.spinner("Marcus is reviewing your request..."):
                reply = safe_generate_content(full_prompt, agent_name="Marcus (CEO)")
                st.markdown(reply)
                st.session_state.chat_ceo.append(("assistant", reply))
                save_persistent_memory()


# =============================================================
# 3. SOCIAL MEDIA COMMAND (Chloe & Liam)
# =============================================================
elif nav_choice == "📱 Social Media Command (Chloe & Liam)":
    st.title("📱 Social Media Command: Chloe & Liam Cole")
    st.caption("Tell Chloe & Liam what to change before posting. Full multi-turn memory enabled!")

    sc1, sc2 = st.columns([3, 1])
    with sc1:
        st.markdown(f"**Current Working Draft:** `{st.session_state.social_draft[:90]}...`")
    with sc2:
        if st.button("🧹 Clear Social Chat"):
            st.session_state.chat_social = []
            save_persistent_memory()
            st.rerun()

    st.markdown("---")
    for role, msg in st.session_state.chat_social:
        with st.chat_message(role, avatar="📱" if role == "assistant" else "👤"):
            st.markdown(msg)

    social_input = st.chat_input("Ask Chloe: 'Make the YouTube hook punchier', 'Rewrite for Instagram carousel', etc...")
    if social_input:
        st.session_state.chat_social.append(("user", social_input))
        with st.chat_message("user", avatar="👤"):
            st.markdown(social_input)

        chloe_system = (
            "You are Chloe, Head of Social Media, and Liam Cole, YouTube Producer. "
            "You craft high-converting, viral content across YouTube, Instagram, Facebook, and Twitter/X. "
            "Always remember past edits and conversation history. Make exact revisions as requested."
        )

        full_prompt = build_chat_context(st.session_state.chat_social[:-1], social_input, chloe_system)

        with st.chat_message("assistant", avatar="📱"):
            with st.spinner("Chloe & Liam are refining your content..."):
                reply = safe_generate_content(full_prompt, agent_name="Chloe (Social Team)")
                st.markdown(reply)
                st.session_state.chat_social.append(("assistant", reply))
                st.session_state.social_draft = reply
                save_persistent_memory()

    st.markdown("---")
    st.subheader("🚀 1-Click Dispatch to Live Social Media Webhook")
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
# 4. FOREX MT5 DESK (Ray Dalton)
# =============================================================
elif nav_choice == "📈 Forex MT5 Desk (Ray Dalton)":
    st.title("📈 Forex MT5 Desk: Ray Dalton (Quant Analyst)")
    st.caption("Direct consultation on currency and Gold setups. Review and adjust parameters before firing to MT5!")

    rc1, rc2 = st.columns([3, 1])
    with rc1:
        st.markdown(f"**Current Setup:** `{st.session_state.trading_setup}`")
    with rc2:
        if st.button("🧹 Clear Trading Chat"):
            st.session_state.chat_trading = []
            save_persistent_memory()
            st.rerun()

    st.markdown("---")
    for role, msg in st.session_state.chat_trading:
        with st.chat_message(role, avatar="📈" if role == "assistant" else "👤"):
            st.markdown(msg)

    trade_input = st.chat_input("Ask Ray: 'Tighten Stop-Loss on Gold', 'Recalculate for $5,000 account', etc...")
    if trade_input:
        st.session_state.chat_trading.append(("user", trade_input))
        with st.chat_message("user", avatar="👤"):
            st.markdown(trade_input)

        ray_system = (
            "You are Ray Dalton, veteran quantitative analyst and Forex trader. "
            "You manage 24/5 MetaTrader 5 setups for EURUSD, GBPUSD, and XAUUSD (Gold). "
            "Always remember past trade context and calculations. Be disciplined, risk-first, and precise."
        )

        full_prompt = build_chat_context(st.session_state.chat_trading[:-1], trade_input, ray_system)

        with st.chat_message("assistant", avatar="📈"):
            with st.spinner("Ray is analyzing the market parameters..."):
                reply = safe_generate_content(full_prompt, agent_name="Ray Dalton (Forex)")
                st.markdown(reply)
                st.session_state.chat_trading.append(("assistant", reply))
                st.session_state.trading_setup = reply
                save_persistent_memory()

    st.markdown("---")
    st.subheader("⚡ Fire Approved Order to MT5 Bridge")
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
# 5. SOFTWARE ARCHITECTURE (Elena Rostova)
# =============================================================
elif nav_choice == "🏛️ Software Architecture (Elena Rostova)":
    st.title("🏛️ Elena Rostova: Lead Software Architect")
    st.caption("Direct consultation with Elena on database schemas, system architecture, API contracts, and scalability.")

    ec1, ec2 = st.columns([3, 1])
    with ec2:
        if st.button("🧹 Clear Architecture Chat"):
            st.session_state.chat_engineering = []
            save_persistent_memory()
            st.rerun()

    st.markdown("---")
    for role, msg in st.session_state.chat_engineering:
        with st.chat_message(role, avatar="🏛️" if role == "assistant" else "👤"):
            st.markdown(msg)

    arch_input = st.chat_input("Ask Elena: 'Design a PostgreSQL schema for multi-tenant SaaS', 'Plan microservice API contract'...")
    if arch_input:
        st.session_state.chat_engineering.append(("user", arch_input))
        with st.chat_message("user", avatar="👤"):
            st.markdown(arch_input)

        elena_system = (
            "You are Elena Rostova, Lead Software Architect of AutoOffice. "
            "You specify database schemas, system diagrams, high-throughput backend architecture, "
            "and clean architectural blueprints. Be precise, technical, and structured."
        )

        full_prompt = build_chat_context(st.session_state.chat_engineering[:-1], arch_input, elena_system)

        with st.chat_message("assistant", avatar="🏛️"):
            with st.spinner("Elena is formulating system architecture..."):
                reply = safe_generate_content(full_prompt, agent_name="Elena (Architect)")
                st.markdown(reply)
                st.session_state.chat_engineering.append(("assistant", reply))
                save_persistent_memory()


# =============================================================
# 6. UI/UX DESIGN SYSTEMS (Sora Takahashi)
# =============================================================
elif nav_choice == "🎨 UI/UX Design Systems (Sora Takahashi)":
    st.title("🎨 Sora Takahashi: Head of UI/UX & Design Systems")
    st.caption("Direct consultation with Sora on user experience, design tokens, color palettes, and wireframe layouts.")

    sc1, sc2 = st.columns([3, 1])
    with sc2:
        if st.button("🧹 Clear Design Chat"):
            st.session_state.chat_design = []
            save_persistent_memory()
            st.rerun()

    st.markdown("---")
    for role, msg in st.session_state.chat_design:
        with st.chat_message(role, avatar="🎨" if role == "assistant" else "👤"):
            st.markdown(msg)

    design_input = st.chat_input("Ask Sora: 'Create modern dark mode color palette', 'Wireframe onboarding flow for mobile app'...")
    if design_input:
        st.session_state.chat_design.append(("user", design_input))
        with st.chat_message("user", avatar="👤"):
            st.markdown(design_input)

        sora_system = (
            "You are Sora Takahashi, Head of UI/UX & Design Systems. "
            "You specialize in clean typography, responsive layout hierarchy, design tokens, "
            "and intuitive user journeys. Provide visual descriptions, Tailwind classes, and ASCII wireframes."
        )

        full_prompt = build_chat_context(st.session_state.chat_design[:-1], design_input, sora_system)

        with st.chat_message("assistant", avatar="🎨"):
            with st.spinner("Sora is designing your UI/UX layout..."):
                reply = safe_generate_content(full_prompt, agent_name="Sora (UI/UX)")
                st.markdown(reply)
                st.session_state.chat_design.append(("assistant", reply))
                save_persistent_memory()


# =============================================================
# 7. FULL-STACK ENGINEERING (Devon Brooks)
# =============================================================
elif nav_choice == "💻 Full-Stack Engineering (Devon Brooks)":
    st.title("💻 Devon Brooks: Senior Full-Stack Engineer")
    st.caption("Direct consultation with Devon to generate production code, debug scripts, and implement backend/frontend features.")

    if "chat_devon" not in st.session_state:
        st.session_state.chat_devon = []

    dc1, dc2 = st.columns([3, 1])
    with dc2:
        if st.button("🧹 Clear Code Chat"):
            st.session_state.chat_devon = []
            st.rerun()

    st.markdown("---")
    for role, msg in st.session_state.chat_devon:
        with st.chat_message(role, avatar="💻" if role == "assistant" else "👤"):
            st.markdown(msg)

    devon_input = st.chat_input("Ask Devon: 'Write a React Native subscription paywall component', 'Debug Python script'...")
    if devon_input:
        st.session_state.chat_devon.append(("user", devon_input))
        with st.chat_message("user", avatar="👤"):
            st.markdown(devon_input)

        devon_system = (
            "You are Devon Brooks, Senior Full-Stack Engineer. "
            "You write clean, modular, production-ready code with complete TypeScript/Python implementations, "
            "error handling, and zero placeholder comments."
        )

        full_prompt = build_chat_context(st.session_state.chat_devon[:-1], devon_input, devon_system)

        with st.chat_message("assistant", avatar="💻"):
            with st.spinner("Devon is writing production code..."):
                reply = safe_generate_content(full_prompt, agent_name="Devon (Engineer)")
                st.markdown(reply)
                st.session_state.chat_devon.append(("assistant", reply))


# =============================================================
# 8. TEAM ALPHA COMMERCIAL APP SPRINT (Full Collaborative Build)
# =============================================================
elif nav_choice == "🚀 Team Alpha Commercial App Sprint":
    st.title("🚀 Team Alpha: Collaborative Commercial App Sprint")
    st.caption("Watch Marcus (Strategy), Elena (Architecture), Sora (Design), Devon (Code), and Tariq (DevOps) build an entire commercial app together.")

    app_name = st.text_input("App Name / Concept:", placeholder="e.g. ZenTimer - Focus & Revenue Tracker for Creators")
    framework = st.selectbox("Framework:", ["React Native / Expo (iOS & Android)", "Flutter / Dart", "SwiftUI Native iOS", "PWA Next.js"])
    monetization = st.multiselect("Monetization Model:", ["Freemium + Weekly/Monthly Subscriptions", "One-Time Pro Purchase", "Credit Packs"], default=["Freemium + Weekly/Monthly Subscriptions"])

    app_brief = st.text_area("Features to Build:", placeholder="e.g. Offline-first habit tracking with widgets, soundscapes, and RevenueCat subscription paywall.")

    if st.button("⚡ Launch Full Team Alpha Commercial Build", type="primary"):
        if not app_brief.strip():
            st.warning("Please provide feature details.")
        else:
            with st.status("🚀 Team Alpha is executing multi-agent build sprint...", expanded=True) as status:
                status.update(label="👔 Marcus Vance is defining commercial scope & monetization...")
                marcus_out = safe_generate_content(f"App: {app_name}\nStack: {framework}\nFeatures: {app_brief}\nDefine product positioning and revenue model.", "You are Marcus Vance, CEO.", agent_name="Marcus (CEO)")
                time.sleep(1)

                status.update(label="🏛️ Elena Rostova is architecting database schema and data models...")
                elena_out = safe_generate_content(f"Scope:\n{marcus_out}\nProvide complete system architecture and DB schema.", "You are Elena Rostova, Lead Architect.", agent_name="Elena (Architect)")
                time.sleep(1)

                status.update(label="🎨 Sora Takahashi is creating UI/UX wireframes & design tokens...")
                sora_out = safe_generate_content(f"Architecture:\n{elena_out}\nProvide UI screen hierarchy, wireframe layout, and design tokens.", "You are Sora Takahashi, Head of UI/UX.", agent_name="Sora (UI/UX)")
                time.sleep(1)

                status.update(label="💻 Devon Brooks is producing production source code...")
                devon_out = safe_generate_content(f"Design & Architecture:\n{sora_out}\nWrite the complete core code in {framework}.", "You are Devon Brooks, Senior Full-Stack Engineer.", agent_name="Devon (Engineer)")
                time.sleep(1)

                status.update(label="🛡️ Tariq Chen is preparing App Store submission & compliance checklist...")
                tariq_out = safe_generate_content(f"Code:\n{devon_out}\nProvide App Store / Google Play submission checklist, privacy permissions, and rejection pitfalls.", "You are Tariq Chen, Security Lead.", agent_name="Tariq (DevOps)")

                status.update(label="✅ Team Alpha Commercial App Sprint Complete!", state="complete")

            st.session_state.app_status = f"Commercial App: {app_name or 'App'} built with {framework}"
            save_persistent_memory()

            t1, t2, t3, t4, t5 = st.tabs([
                "👔 Strategy (Marcus)",
                "🏛️ Architecture (Elena)",
                "🎨 UI/UX (Sora)",
                "💻 Source Code (Devon)",
                "🛡️ App Store Checklist (Tariq)"
            ])
            with t1: st.markdown(marcus_out)
            with t2: st.markdown(elena_out)
            with t3: st.markdown(sora_out)
            with t4: st.markdown(devon_out)
            with t5: st.markdown(tariq_out)


# =============================================================
# 9. WEB OPERATOR (Atlas - Browser Control)
# =============================================================
elif nav_choice == "🌐 Web Operator (Atlas - Browser Control)":
    st.title("🌐 Atlas: Autonomous Web & Browser Operator")
    st.caption("Direct Atlas to inspect sites, fill form inputs, and click buttons.")
    target_url = st.text_input("Target URL:", placeholder="https://example.com/signup")
    directive = st.text_area("Directive:", placeholder="e.g. Go to the search input, type 'AI Multi-Agent Systems', and click Submit.")
    if st.button("🤖 Run Browser Plan", type="primary"):
        if target_url and directive:
            with st.status("🌐 Atlas is mapping DOM elements...", expanded=True) as status:
                prompt = f"URL: {target_url}\nAction: {directive}\nProvide step-by-step action plan, CSS/XPath selectors, and Playwright Python script."
                out = safe_generate_content(prompt, "You are Atlas, autonomous browser operator.", agent_name="Atlas (Web Operator)")
                status.update(label="✅ Plan Completed!", state="complete")
            st.markdown(out)


# =============================================================
# 10. FINOPS & TOKEN AUDITOR (Finley)
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
    st.subheader("📜 Multi-Team Expense Ledger")
    if ledger:
        st.dataframe(ledger, use_container_width=True)
    else:
        st.info("No API transactions recorded in this session yet.")
