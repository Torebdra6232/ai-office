import streamlit as st
import os
import time
from datetime import datetime
from dotenv import load_dotenv
from google import genai
from PIL import Image

# 1. Page Configuration
st.set_page_config(
    page_title="AutoOffice OS - Multi-Agent AI Enterprise",
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

# Global Session State for Accounting & Usage
if "token_ledger" not in st.session_state:
    st.session_state.token_ledger = []
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

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
    
    # Blended estimate: ~$0.15 per 1M input, ~$0.60 per 1M output
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


# 2. Sidebar Navigation & Team Selection
st.sidebar.title("🏢 AutoOffice OS")
st.sidebar.caption("Autonomous 9-Agent Enterprise")

mode = st.sidebar.radio(
    "Select Department / Workspace:",
    [
        "💬 Executive Suite (Marcus Vance, CEO)",
        "🚀 Team Alpha (Engineering & DevOps)",
        "🎨 Team Beta (Product & Design)",
        "🌐 Web Operator (Atlas - Browser Control)",
        "📱 Social Media (Chloe - Viral Growth)",
        "💰 Accountant & FinOps (Finley - Cost Tracker)"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 👥 Full Roster (9 Agents)")
st.sidebar.markdown("""
**Executive & Operations:**
- 👔 **Marcus Vance** — CEO & Chief Strategist
- 🌐 **Atlas** — Autonomous Web & Browser Operator
- 💰 **Finley** — Corporate Accountant & Token Auditor

**Engineering (Team Alpha):**
- 🏛️ **Elena Rostova** — Lead Software Architect
- 💻 **Devon Brooks** — Senior Full-Stack Engineer
- 🛡️ **Tariq Chen** — DevOps & Cloud Security Lead

**Growth & Design (Team Beta):**
- 🎨 **Sora Takahashi** — Head of UI/UX & Design Systems
- 📈 **Maya Lin** — VP of Growth & Conversion Copy
- 📱 **Chloe** — Head of Social Media & Viral Campaigns
""")

st.sidebar.markdown("---")
if st.sidebar.button("🧹 Clear Chat History"):
    st.session_state.chat_history = []
    st.rerun()


# =============================================================
# 1. EXECUTIVE SUITE (Marcus Vance, CEO)
# =============================================================
if mode == "💬 Executive Suite (Marcus Vance, CEO)":
    st.header("👔 Executive War Room: Marcus Vance (CEO)")
    st.caption("Plan 2-week roadmaps, cross-team directives, or upload wireframes & screenshots.")

    uploaded_file = st.file_uploader("📎 Attach Document, Wireframe, or Screenshot:", type=["png", "jpg", "jpeg", "txt", "py", "json"])

    marcus_system = (
        "You are Marcus Vance, the decisive, experienced CEO and Chief Strategist of AutoOffice. "
        "Keep responses structured, confident, practical, and highly direct."
    )

    for role, msg in st.session_state.chat_history:
        with st.chat_message(role, avatar="👔" if role == "assistant" else "👤"):
            st.markdown(msg)

    user_input = st.chat_input("Ask Marcus anything or command your executive team...")
    if user_input:
        st.session_state.chat_history.append(("user", user_input))
        with st.chat_message("user", avatar="👤"):
            st.markdown(user_input)

        contents = []
        if uploaded_file:
            if uploaded_file.type.startswith("image/"):
                img = Image.open(uploaded_file)
                contents.append(img)
            else:
                text_content = uploaded_file.read().decode("utf-8", errors="ignore")
                contents.append(f"Attached file ({uploaded_file.name}):\n{text_content}\n")
        contents.append(user_input)

        with st.chat_message("assistant", avatar="👔"):
            with st.spinner("Marcus is reviewing your request..."):
                reply = safe_generate_content(contents, system_instruction=marcus_system, agent_name="Marcus (CEO)")
                st.markdown(reply)
                st.session_state.chat_history.append(("assistant", reply))


# =============================================================
# 2. TEAM ALPHA SPRINT (Engineering & DevOps)
# =============================================================
elif mode == "🚀 Team Alpha (Engineering & DevOps)":
    st.header("🚀 Team Alpha: Technical Architecture & Implementation")
    st.caption("Marcus (Strategy) ➔ Elena (Architecture) ➔ Devon (Code) ➔ Tariq (DevOps)")

    project_task = st.text_area("Describe what Team Alpha should architect & build:", placeholder="e.g. Build an AI-driven invoice parsing microservice with FastAPI, PostgreSQL, and Docker.")

    if st.button("⚡ Launch Team Alpha Sprint", type="primary"):
        if not project_task.strip():
            st.warning("Please provide a technical task description first.")
        else:
            with st.status("🚀 Team Alpha is executing your engineering sprint...", expanded=True) as status:
                status.update(label="👔 Marcus Vance is setting engineering deliverables...")
                marcus_out = safe_generate_content(f"Scope:\n{project_task}\nProvide an executive engineering directive.", "You are Marcus Vance, CEO.", agent_name="Marcus (CEO)")
                time.sleep(1)

                status.update(label="🏛️ Elena Rostova is architecting the system schema...")
                elena_out = safe_generate_content(f"Directive:\n{marcus_out}\nTask:\n{project_task}\nProvide detailed system architecture and DB schema.", "You are Elena Rostova, Lead Architect.", agent_name="Elena (Architect)")
                time.sleep(1)

                status.update(label="💻 Devon Brooks is producing production implementation code...")
                devon_out = safe_generate_content(f"Architecture:\n{elena_out}\nWrite complete implementation code.", "You are Devon Brooks, Senior Full-Stack Engineer.", agent_name="Devon (Engineer)")
                time.sleep(1)

                status.update(label="🛡️ Tariq Chen is building deployment & security configs...")
                tariq_out = safe_generate_content(f"Code:\n{devon_out}\nProvide Dockerfile, CI/CD, and security measures.", "You are Tariq Chen, DevOps Lead.", agent_name="Tariq (DevOps)")

                status.update(label="✅ Team Alpha Sprint Complete!", state="complete")

            t1, t2, t3, t4 = st.tabs(["👔 Strategy (Marcus)", "🏛️ Architecture (Elena)", "💻 Code (Devon)", "🛡️ DevOps (Tariq)"])
            with t1: st.markdown(marcus_out)
            with t2: st.markdown(elena_out)
            with t3: st.markdown(devon_out)
            with t4: st.markdown(tariq_out)


# =============================================================
# 3. TEAM BETA SPRINT (Product, Design & Growth)
# =============================================================
elif mode == "🎨 Team Beta (Product & Design)":
    st.header("🎨 Team Beta: Product, UI/UX & Go-To-Market")
    st.caption("Marcus (Positioning) ➔ Sora (Design System) ➔ Maya (Conversion Copy)")

    product_goal = st.text_area("Describe your product idea & target market:", placeholder="e.g. Modern CRM for freelance video editors with automated client onboarding.")

    if st.button("🌟 Launch Team Beta Sprint", type="primary"):
        if not product_goal.strip():
            st.warning("Please provide a product description first.")
        else:
            with st.status("🎨 Team Beta is assembling product assets...", expanded=True) as status:
                status.update(label="🎯 Marcus Vance is defining positioning & pricing...")
                positioning = safe_generate_content(f"Goal:\n{product_goal}\nDefine target persona and pricing model.", "You are Marcus Vance, CEO.", agent_name="Marcus (CEO)")
                time.sleep(1)

                status.update(label="🎨 Sora Takahashi is creating UI/UX wireframes...")
                design = safe_generate_content(f"Positioning:\n{positioning}\nCreate the UI/UX layout and design tokens.", "You are Sora Takahashi, Head of UI/UX.", agent_name="Sora (UI/UX)")
                time.sleep(1)

                status.update(label="📈 Maya Lin is writing high-converting launch copy...")
                marketing = safe_generate_content(f"Design:\n{design}\nWrite landing page copy and launch hooks.", "You are Maya Lin, Growth Director.", agent_name="Maya (Copy)")

                status.update(label="✅ Team Beta Sprint Complete!", state="complete")

            b1, b2, b3 = st.tabs(["🎯 Positioning (Marcus)", "🎨 UI/UX System (Sora)", "📈 Copywriting (Maya)"])
            with b1: st.markdown(positioning)
            with b2: st.markdown(design)
            with b3: st.markdown(marketing)


# =============================================================
# 4. WEB OPERATOR (Atlas - Autonomous Browser Control)
# =============================================================
elif mode == "🌐 Web Operator (Atlas - Browser Control)":
    st.header("🌐 Atlas: Autonomous Web & Browser Operator")
    st.caption("Instruct Atlas to navigate to any website, fill input fields, and click buttons autonomously.")

    target_url = st.text_input("Target Website URL:", placeholder="https://example.com/signup or https://news.ycombinator.com")
    action_directive = st.text_area(
        "Action Directive (What should Atlas click, fill, or submit?):",
        placeholder="e.g. Go to the search bar, type 'AI multi-agent frameworks', click the Search button, and extract the top 3 results."
    )

    col_btn1, col_btn2 = st.columns([1, 4])
    with col_btn1:
        run_op = st.button("🤖 Execute Web Operation", type="primary")

    if run_op:
        if not target_url.strip() or not action_directive.strip():
            st.warning("Please provide both a Target URL and an Action Directive.")
        else:
            with st.status("🌐 Atlas is executing browser automation...", expanded=True) as status:
                status.update(label=f"🔍 Atlas is inspecting {target_url}...")
                
                atlas_system = (
                    "You are Atlas, an elite Autonomous Web Browser Operator and Computer-Use Agent. "
                    "You plan and execute precise browser automation sequences: navigating URLs, detecting input fields, "
                    "filling form data, clicking buttons, handling popups, and confirming successful submission."
                )

                op_prompt = f"""
Target Website: {target_url}
User Directive: {action_directive}

Provide:
1. 📋 **Autonomous Action Plan**: Exact sequence of steps to perform on this page.
2. 🎯 **DOM Selector & Field Mapping**: Target elements (input fields, dropdowns, submit buttons) with CSS/XPath selectors and values to inject.
3. 💻 **Executable Playwright / Python Script**: A production-grade, headless browser automation script that executes this task seamlessly.
4. ✅ **Verification & Fallback**: How Atlas verifies the button click succeeded (e.g. URL change, confirmation message).
"""
                atlas_output = safe_generate_content(op_prompt, system_instruction=atlas_system, agent_name="Atlas (Web Operator)")
                status.update(label="✅ Atlas Web Operation Completed!", state="complete")

            st.markdown(atlas_output)


# =============================================================
# 5. SOCIAL MEDIA (Chloe - Viral Multi-Platform Growth)
# =============================================================
elif mode == "📱 Social Media (Chloe - Viral Growth)":
    st.header("📱 Chloe: Head of Social Media & Viral Growth")
    st.caption("Turn any product, feature, or announcement into viral posts across all major social networks.")

    topic = st.text_area("What are we promoting or announcing?", placeholder="e.g. Launching AutoOffice OS - our 9-agent autonomous AI enterprise that builds software and operates browsers.")
    platforms = st.multiselect("Select Target Platforms:", ["X (Twitter) Viral Thread", "LinkedIn Authority Post", "Instagram / TikTok Short Script", "Reddit Value Post"], default=["X (Twitter) Viral Thread", "LinkedIn Authority Post"])

    if st.button("🚀 Generate Viral Social Campaign", type="primary"):
        if not topic.strip():
            st.warning("Please describe what we are promoting.")
        else:
            with st.spinner("Chloe is crafting your viral campaign..."):
                chloe_system = (
                    "You are Chloe, a world-class VP of Social Media & Viral Copywriting. "
                    "You write punchy, engaging, high-retention content with irresistible hooks, clean spacing, "
                    "strategic hashtags, and compelling calls-to-action (CTAs). Avoid corporate clichés."
                )
                chloe_prompt = f"Topic:\n{topic}\nTarget Platforms:\n{', '.join(platforms)}\nCreate high-converting, platform-tailored copy for each selected channel."
                campaign = safe_generate_content(chloe_prompt, system_instruction=chloe_system, agent_name="Chloe (Social)")
                st.markdown(campaign)


# =============================================================
# 6. ACCOUNTANT & FINOPS (Finley - Token & Expense Tracker)
# =============================================================
elif mode == "💰 Accountant & FinOps (Finley - Cost Tracker)":
    st.header("💰 Finley: Corporate Accountant & Token Auditor")
    st.caption("Live financial oversight: token metrics, API expense tracking, and cost optimization.")

    ledger = st.session_state.token_ledger
    total_tokens = sum(item["total_tokens"] for item in ledger)
    total_cost = sum(item["cost_usd"] for item in ledger)
    total_calls = len(ledger)

    # Metric Cards
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("Total Spent", f"${total_cost:.5f} USD")
    with c2:
        st.metric("Total Tokens Processed", f"{total_tokens:,}")
    with c3:
        st.metric("API Calls Logged", f"{total_calls}")
    with c4:
        avg_cost = (total_cost / total_calls) if total_calls > 0 else 0
        st.metric("Avg Cost / Request", f"${avg_cost:.5f}")

    st.markdown("---")
    st.subheader("📜 Itemized Expense Ledger")
    if ledger:
        st.dataframe(ledger, use_container_width=True)
    else:
        st.info("No API transactions logged in this session yet. Run a sprint or chat with any agent to generate live expense data!")

    st.markdown("---")
    st.subheader("📊 Finley's Financial Audit & ROI Report")
    if st.button("📈 Run FinOps Audit with Finley", type="primary"):
        with st.spinner("Finley is auditing your token efficiency and API costs..."):
            finley_system = (
                "You are Finley, the sharp, prudent Chief Accountant and FinOps Auditor for AutoOffice. "
                "You provide precise financial audits, token consumption breakdowns, ROI calculations, "
                "and cost-saving recommendations to run multi-agent workflows at minimal expense."
            )
            finley_prompt = f"""
Current Session Financials:
- Total Cost: ${total_cost:.5f} USD
- Total Tokens: {total_tokens:,}
- Total Agent Invocations: {total_calls}
- Recent Transaction History: {ledger[-10:] if ledger else 'Fresh session'}

Provide an executive financial audit:
1. 💡 **Cost Efficiency Analysis**: Assessment of current token burn rate.
2. 📉 **FinOps Optimization Tips**: Exact techniques to cut token overhead by 30-50%.
3. 💰 **Projected Scale Costs**: Estimated budget required for 1,000 daily tasks.
"""
            audit_report = safe_generate_content(finley_prompt, system_instruction=finley_system, agent_name="Finley (Accountant)")
            st.markdown(audit_report)
