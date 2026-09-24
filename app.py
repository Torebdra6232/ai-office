import streamlit as st
import os
import time
from dotenv import load_dotenv
from google import genai
from PIL import Image

# 1. Page Configuration
st.set_page_config(
    page_title="AutoOffice OS - Autonomous Multi-Agent Suite",
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

# Active 2026 production models (with automated fallback sequence)
PRIMARY_MODELS = [
    "gemini-2.5-flash",
    "gemini-3.8-flash",
    "gemini-3.1-flash-lite",
    "gemini-flash-latest"
]

def safe_generate_content(prompt_or_contents, system_instruction=None):
    """
    Resilient generation helper:
    Tries active production models sequentially and handles rate limits cleanly.
    """
    if not client:
        return "⚠️ Please set your `GEMINI_API_KEY` in Streamlit Secrets or your .env file."

    last_error = None
    for model_name in PRIMARY_MODELS:
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
                return response.text
        except Exception as e:
            last_error = str(e)
            # If rate-limited (429), pause briefly before trying next model
            if "429" in last_error or "RESOURCE_EXHAUSTED" in last_error:
                time.sleep(2)
            continue

    return f"⚠️ Service notice: AI agents are momentarily resting. Please try again in a few seconds. (Details: {last_error})"


# 2. Sidebar Navigation & Team Selection
st.sidebar.title("🏢 AutoOffice OS")
st.sidebar.caption("Autonomous Multi-Agent AI Corporation")

mode = st.sidebar.radio(
    "Select Operating Mode:",
    [
        "💬 Executive Suite (Marcus Vance, CEO)",
        "🚀 Team Alpha Sprint (Engineering & Architecture)",
        "🎨 Team Beta Sprint (Product, Design & Growth)"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 👥 Active Staff (6+ Agents)")
st.sidebar.markdown("""
**Executive:**
- 👔 **Marcus Vance** — CEO & Chief Strategist

**Team Alpha (Engineering):**
- 🏛️ **Elena Rostova** — Lead Software Architect
- 💻 **Devon Brooks** — Senior Full-Stack Engineer
- 🛡️ **Tariq Chen** — DevOps & Cloud Security Lead

**Team Beta (Product & Growth):**
- 🎨 **Sora Takahashi** — Head of UI/UX & Design Systems
- 📈 **Maya Lin** — VP of Growth & Conversion Copy
""")

st.sidebar.markdown("---")
if st.sidebar.button("🧹 Clear Chat / Session"):
    st.session_state.chat_history = []
    st.rerun()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# -------------------------------------------------------------
# MODE 1: Executive Suite (Direct 1-on-1 with Marcus Vance)
# -------------------------------------------------------------
if mode == "💬 Executive Suite (Marcus Vance, CEO)":
    st.header("👔 Executive War Room: Marcus Vance (CEO)")
    st.caption("Plan 2-week roadmaps, ask questions, or upload wireframes & screenshots for Marcus to review.")

    uploaded_file = st.file_uploader(
        "📎 Attach Screenshot, Wireframe, or Document for Marcus:",
        type=["png", "jpg", "jpeg", "txt", "py", "json"]
    )

    marcus_system = (
        "You are Marcus Vance, the decisive, experienced CEO and Chief Strategist of AutoOffice. "
        "You provide actionable executive advice, technical project management, and clear strategic direction. "
        "Keep responses structured, confident, practical, and highly direct."
    )

    # Display history
    for role, msg in st.session_state.chat_history:
        with st.chat_message(role, avatar="👔" if role == "assistant" else "👤"):
            st.markdown(msg)

    user_input = st.chat_input("Ask Marcus anything or plan a sprint...")
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
                reply = safe_generate_content(contents, system_instruction=marcus_system)
                st.markdown(reply)
                st.session_state.chat_history.append(("assistant", reply))


# -------------------------------------------------------------
# MODE 2: Team Alpha Sprint (Engineering & Architecture)
# -------------------------------------------------------------
elif mode == "🚀 Team Alpha Sprint (Engineering & Architecture)":
    st.header("🚀 Team Alpha: Technical Architecture & Implementation")
    st.caption("Marcus (Strategy) ➔ Elena (Architecture) ➔ Devon (Code) ➔ Tariq (DevOps)")

    project_task = st.text_area(
        "Describe the feature, architecture, or full project for Team Alpha to build:",
        placeholder="e.g. Build a secure real-time notification engine with WebSockets, Redis pub/sub, and PostgreSQL."
    )

    if st.button("⚡ Launch Team Alpha Sprint", type="primary"):
        if not project_task.strip():
            st.warning("Please provide a project description first.")
        else:
            with st.status("🚀 Team Alpha is collaborating on your sprint...", expanded=True) as status:
                
                # 1. Marcus Vance
                status.update(label="👔 Marcus Vance is outlining the technical scope and priorities...")
                marcus_prompt = f"Executive Scope & Technical Objective:\n{project_task}\nProvide an executive engineering directive."
                marcus_out = safe_generate_content(marcus_prompt, "You are Marcus Vance, CEO. Set high-level engineering deliverables.")
                time.sleep(1)

                # 2. Elena Rostova
                status.update(label="🏛️ Elena Rostova is formulating the system architecture...")
                elena_prompt = f"CEO Directive:\n{marcus_out}\n\nTask:\n{project_task}\nProvide detailed system architecture, database schema, and component design."
                elena_out = safe_generate_content(elena_prompt, "You are Elena Rostova, Lead Architect. Output clean architectural specifications.")
                time.sleep(1)

                # 3. Devon Brooks
                status.update(label="💻 Devon Brooks is producing production implementation code...")
                devon_prompt = f"Architecture Spec:\n{elena_out}\n\nWrite the complete implementation code and core components."
                devon_out = safe_generate_content(devon_prompt, "You are Devon Brooks, Senior Full-Stack Engineer. Output clean, working, documented code.")
                time.sleep(1)

                # 4. Tariq Chen
                status.update(label="🛡️ Tariq Chen is generating CI/CD pipelines & security configs...")
                tariq_prompt = f"Code & Architecture:\n{devon_out}\n\nProvide Dockerfile, GitHub Actions CI/CD, and security hardening."
                tariq_out = safe_generate_content(tariq_prompt, "You are Tariq Chen, DevOps & Cloud Security Lead. Output deployment & security specs.")
                
                status.update(label="✅ Team Alpha Sprint Complete!", state="complete")

            # Display results in organized tabs
            t1, t2, t3, t4 = st.tabs([
                "👔 Strategy (Marcus)",
                "🏛️ Architecture (Elena)",
                "💻 Implementation (Devon)",
                "🛡️ DevOps & Security (Tariq)"
            ])
            with t1: st.markdown(marcus_out)
            with t2: st.markdown(elena_out)
            with t3: st.markdown(devon_out)
            with t4: st.markdown(tariq_out)


# -------------------------------------------------------------
# MODE 3: Team Beta Sprint (Product, Design & Growth)
# -------------------------------------------------------------
elif mode == "🎨 Team Beta Sprint (Product, Design & Growth)":
    st.header("🎨 Team Beta: Product, UI/UX & Go-To-Market Sprint")
    st.caption("Marcus (Positioning) ➔ Sora (Design System & UI/UX) ➔ Maya (Growth & Copy)")

    product_goal = st.text_area(
        "Describe your product idea, audience, and market target:",
        placeholder="e.g. AI-powered financial companion for freelance creatives with automated tax forecasting."
    )

    if st.button("🌟 Launch Team Beta Sprint", type="primary"):
        if not product_goal.strip():
            st.warning("Please provide a product description first.")
        else:
            with st.status("🎨 Team Beta is assembling product & go-to-market assets...", expanded=True) as status:
                
                # 1. Marcus Vance
                status.update(label="🎯 Marcus Vance is defining product positioning & monetization...")
                pos_prompt = f"Product Goal:\n{product_goal}\nDefine target persona, value proposition, and pricing strategy."
                positioning = safe_generate_content(pos_prompt, "You are Marcus Vance, CEO. Focus on market positioning and revenue models.")
                time.sleep(1)

                # 2. Sora Takahashi
                status.update(label="🎨 Sora Takahashi is designing UI/UX wireframes & design tokens...")
                sora_prompt = f"Positioning Document:\n{positioning}\nCreate the UI/UX layout hierarchy, color palette, and user onboarding flow."
                design = safe_generate_content(sora_prompt, "You are Sora Takahashi, Head of UI/UX. Provide wireframe blueprints and design tokens.")
                time.sleep(1)

                # 3. Maya Lin
                status.update(label="📈 Maya Lin is writing high-converting landing page copy & launch strategy...")
                maya_prompt = f"Product & UX Blueprint:\n{design}\nWrite high-converting headline copy, email launch sequence, and viral growth hooks."
                marketing = safe_generate_content(maya_prompt, "You are Maya Lin, Growth & Marketing Director. Output high-converting copy and acquisition strategy.")

                status.update(label="✅ Team Beta Sprint Complete!", state="complete")

            b1, b2, b3 = st.tabs([
                "🎯 Positioning & Pricing (Marcus)",
                "🎨 UI/UX Design System (Sora)",
                "📈 Growth & Copy (Maya)"
            ])
            with b1: st.markdown(positioning)
            with b2: st.markdown(design)
            with b3: st.markdown(marketing)
