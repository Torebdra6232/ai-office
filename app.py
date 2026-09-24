import streamlit as st
import os
import time
from dotenv import load_dotenv
from google import genai
from PIL import Image

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key) if api_key else None

# Traffic-proof model strategy:
# Gemma for pure text (avoids Gemini 15 RPM limits)
# Gemini 1.5 Flash for vision/multimodal uploads and backup
TEXT_MODEL = "gemma-2-27b-it"
VISION_AND_BACKUP_MODEL = "gemini-1.5-flash"

st.set_page_config(page_title="AutoOffice OS", page_icon="🏢", layout="wide")

# High-contrast command deck styling
st.markdown("""
<style>
    .stApp { background: radial-gradient(circle at 50% 0%, #0f172a 0%, #020617 100%); color: #f8fafc; }
    .stTabs [data-baseweb="tab-list"] { gap: 8px; }
    .stTabs [data-baseweb="tab"] { background-color: #1e293b; border-radius: 8px; padding: 8px 16px; color: #94a3b8; }
    .stTabs [aria-selected="true"] { background-color: #2563eb !important; color: white !important; }
</style>
""", unsafe_allow_html=True)

# Safe generator function: Prevents 429 traffic limit and never crashes with red screen
def safe_generate(prompt_text, image=None):
    if not client:
        return "⚠️ Note: GEMINI_API_KEY is not set in Secrets. Running in simulated offline mode."
    
    # Tiny 1.2s breather between agent steps so 4 agents never trip Google's 15 RPM limit
    time.sleep(1.2)

    # If user attached an image, use Gemini 1.5 Flash (handles vision)
    if image is not None:
        try:
            response = client.models.generate_content(
                model=VISION_AND_BACKUP_MODEL,
                contents=[prompt_text, image]
            )
            return response.text
        except Exception:
            try:
                response = client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=[prompt_text, image]
                )
                return response.text
            except Exception as e:
                return f"⚠️ Multimodal analysis notice: Could not process image. ({str(e)})"

    # For text-only tasks: Use Gemma first to avoid Gemini traffic collisions
    try:
        response = client.models.generate_content(
            model=TEXT_MODEL,
            contents=prompt_text
        )
        return response.text
    except Exception:
        # Automatic fallback to Gemini 1.5 Flash
        try:
            response = client.models.generate_content(
                model=VISION_AND_BACKUP_MODEL,
                contents=prompt_text
            )
            return response.text
        except Exception as e:
            return f"⚠️ Traffic breather active: Google API is currently rate-limited. Please retry in 10 seconds. ({str(e)})"

# Top Bar
st.title("🏢 AutoOffice OS · Multi-Team Autonomous Fleet")
st.caption("6 Autonomous Agents · 2 Operating Squads · Zero-Traffic Burst Protection")

# Top Mode Navigation
mode = st.radio(
    "Select Office Control Room:",
    [
        "👔 1-on-1 CEO Strategy Room (Marcus Vance)",
        "🚀 Team Alpha (Engineering & Code Pipeline)",
        "🎨 Team Beta (Design & Growth Marketing)"
    ],
    horizontal=True
)

st.divider()

# =====================================================================
# ROOM 1: 1-ON-1 CEO STRATEGY ROOM (With Image/Document Uploads)
# =====================================================================
if mode == "👔 1-on-1 CEO Strategy Room (Marcus Vance)":
    st.subheader("👔 Executive War Room: Marcus Vance (CEO)")
    st.caption("Plan 2-week roadmaps, ask questions, or upload wireframes & screenshots for Marcus to review.")

    # Image / File Uploader
    uploaded_file = st.file_uploader(
        "📎 Attach Screenshot, Wireframe, or Document for Marcus:",
        type=["png", "jpg", "jpeg", "txt", "py", "json"]
    )
    
    pil_image = None
    if uploaded_file:
        if uploaded_file.type.startswith("image/"):
            pil_image = Image.open(uploaded_file)
            st.image(pil_image, caption=f"Attached: {uploaded_file.name}", width=280)
        else:
            st.success(f"Attached document: {uploaded_file.name} ({uploaded_file.size} bytes)")

    if "ceo_chat" not in st.session_state:
        st.session_state.ceo_chat = [
            {"role": "assistant", "content": "Welcome to the Executive Suite! I'm **Marcus Vance**, your CEO & Chief Strategist. What are we building today? You can brainstorm ideas, ask technical questions, or upload a wireframe for me to review."}
        ]

    for msg in st.session_state.ceo_chat:
        with st.chat_message(msg["role"], avatar="👔" if msg["role"] == "assistant" else "👤"):
            st.markdown(msg["content"])

    if user_prompt := st.chat_input("Ask Marcus anything or plan a sprint..."):
        st.session_state.ceo_chat.append({"role": "user", "content": user_prompt})
        with st.chat_message("user", avatar="👤"):
            st.markdown(user_prompt)

        with st.chat_message("assistant", avatar="👔"):
            with st.spinner("Marcus is formulating strategy..."):
                sys_prompt = (
                    "You are Marcus Vance, the charismatic, sharp CEO of AutoOffice OS. "
                    "Talk directly to the user as your Co-Founder. Be sharp, visionary, and pragmatic. "
                    "If they ask about writing or applying code, explain that Devon writes the code in the Vault, "
                    "and we keep human guardrails before pushing to production."
                )
                full_prompt = f"{sys_prompt}\nCo-Founder: {user_prompt}"
                res = safe_generate(full_prompt, image=pil_image)
                st.markdown(res)
                st.session_state.ceo_chat.append({"role": "assistant", "content": res})

# =====================================================================
# ROOM 2: TEAM ALPHA (Engineering & Code Pipeline)
# Agents: Marcus (CEO) -> Elena (CTO) -> Devon (Dev) -> Tariq (QA)
# =====================================================================
elif mode == "🚀 Team Alpha (Engineering & Code Pipeline)":
    st.subheader("🚀 Team Alpha: Software Engineering & Architecture")
    st.markdown("**Squad Roster:** 👔 Marcus (CEO) → 📐 Elena (CTO) → 💻 Devon (Lead Dev) → 🛡️ Tariq (QA Auditor)")
    
    alpha_goal = st.text_input(
        "Enter Engineering Mission:",
        placeholder="e.g. Build a multi-tenant API authentication router with JWT token refresh"
    )

    if st.button("🚀 Dispatch Team Alpha Sprint", type="primary"):
        if not alpha_goal:
            st.warning("Please specify an engineering goal!")
        else:
            with st.status("🏢 Team Alpha is executing sprint...", expanded=True) as status:
                st.write("👔 **Marcus (CEO)** is drafting technical specifications...")
                prd = safe_generate(f"You are Marcus Vance, CEO. Write a clean PRD & requirements for: {alpha_goal}")

                st.write("📐 **Elena (CTO)** is modeling schemas & architecture...")
                arch = safe_generate(f"You are Elena Rostova, CTO. Based on this PRD, design the database schemas, API routes, and tech stack:\n{prd}")

                st.write("💻 **Devon (Lead Dev)** is writing 100% complete working code...")
                code = safe_generate(f"You are Devon Vance, Lead Dev. Write clean, complete, working production code for:\n{arch}")

                st.write("🛡️ **Tariq (QA Auditor)** is testing & verifying edge cases...")
                qa = safe_generate(f"You are Tariq Al-Mansoor, QA Auditor. Stress test and audit this code for security, 8GB memory leaks, and syntax bugs:\n{code}")

                status.update(label="✅ Team Alpha Sprint Complete!", state="complete")

            t1, t2, t3, t4 = st.tabs(["📋 CEO PRD", "📐 CTO Architecture", "💻 Devon Code", "🛡️ QA Audit"])
            with t1: st.markdown(prd)
            with t2: st.markdown(arch)
            with t3: st.code(code, language="python")
            with t4: st.markdown(qa)

# =====================================================================
# ROOM 3: TEAM BETA (Design & Growth Marketing)
# Agents: Marcus (CEO) -> Sora (Product Designer) -> Maya (Growth & Ops)
# =====================================================================
else:
    st.subheader("🎨 Team Beta: Product Design & Growth Revenue")
    st.markdown("**Squad Roster:** 👔 Marcus (CEO) → 🎨 Sora (UI/UX Designer) → 📈 Maya (Growth & Copywriting)")
    
    beta_goal = st.text_input(
        "Enter Design / Growth Mission:",
        placeholder="e.g. Design a dark-mode pricing page and write a viral Twitter/LinkedIn launch sequence"
    )

    if st.button("🎨 Dispatch Team Beta Sprint", type="primary"):
        if not beta_goal:
            st.warning("Please specify a design/marketing goal!")
        else:
            with st.status("🏢 Team Beta is executing sprint...", expanded=True) as status:
                st.write("👔 **Marcus (CEO)** is defining value proposition & target audience...")
                positioning = safe_generate(f"You are Marcus Vance, CEO. Define the target audience, pricing tiers, and value proposition for: {beta_goal}")

                st.write("🎨 **Sora (Product Designer)** is crafting design tokens & UI components...")
                design = safe_generate(f"You are Sora Takahashi, Product Designer. Create UI wireframe specs, Tailwind tokens, and layout guidelines for:\n{positioning}")

                st.write("📈 **Maya (Growth & Ops)** is drafting launch copy & email sequences...")
                marketing = safe_generate(f"You are Maya Lin, Head of Growth. Write high-converting viral launch copy, a 5-part email welcome sequence, and social posts for:\n{positioning}")

                status.update(label="✅ Team Beta Sprint Complete!", state="complete")

            b1, b2, b3 = st.tabs(["🎯 Positioning (Marcus)", "🎨 UI/UX Design System (Sora)", "📈 Growth & Copy (Maya)"])
            with b1: st.markdown(positioning)
            with b2: st.markdown(design)
            with b3: st.markdown(marketing)
