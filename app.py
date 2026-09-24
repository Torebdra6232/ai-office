import streamlit as st
import os
from dotenv import load_dotenv
from google import genai
from PIL import Image

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key) if api_key else None
MODEL = "gemma-4-26b-a4b-it"

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

# Top Bar
st.title("🏢 AutoOffice OS · Multi-Team Autonomous Fleet")
st.caption("6 Autonomous Agents · 2 Operating Squads · 8GB RAM Cloud Orchestration")

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
    
    if uploaded_file:
        if uploaded_file.type.startswith("image/"):
            img = Image.open(uploaded_file)
            st.image(img, caption=f"Attached: {uploaded_file.name}", width=280)
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
                    "You are Marcus Vance, charismatic CEO of AutoOffice OS. "
                    "Talk directly to the user as your Co-Founder. Be sharp, visionary, and pragmatic. "
                    "If they ask about writing/applying code, explain that Devon writes the code in the Vault, "
                    "and we keep human guardrails before pushing to production."
                )
                
                # If image attached, review with multimodal
                content_payload = [f"{sys_prompt}\nCo-Founder: {user_prompt}"]
                if uploaded_file and uploaded_file.type.startswith("image/"):
                    content_payload.append(Image.open(uploaded_file))

                if client:
                    try:
                        res = client.models.generate_content(
                            model="gemini-2.5-flash",
                            contents=content_payload
                        ).text
                    except Exception:
                        res = client.models.generate_content(
                            model=MODEL,
                            contents=f"{sys_prompt}\nUser prompt: {user_prompt}"
                        ).text
                else:
                    res = f"Executive Advisory: I have registered your strategy request for '{user_prompt}'. Let's dispatch Team Alpha to architect and code the solution."

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
                prd = client.models.generate_content(
                    model=MODEL,
                    contents=f"You are Marcus Vance, CEO. Write a clean PRD & requirements for: {alpha_goal}"
                ).text if client else "Mock PRD generated."

                st.write("📐 **Elena (CTO)** is modeling schemas & architecture...")
                arch = client.models.generate_content(
                    model=MODEL,
                    contents=f"You are Elena Rostova, CTO. Based on this PRD, design the database schemas, API routes, and tech stack:\n{prd}"
                ).text if client else "Mock Architecture generated."

                st.write("💻 **Devon (Lead Dev)** is writing 100% complete working code...")
                code = client.models.generate_content(
                    model=MODEL,
                    contents=f"You are Devon Vance, Lead Dev. Write clean, complete, working production code for:\n{arch}"
                ).text if client else "# Devon Code Generated"

                st.write("🛡️ **Tariq (QA Auditor)** is testing & verifying edge cases...")
                qa = client.models.generate_content(
                    model=MODEL,
                    contents=f"You are Tariq Al-Mansoor, QA Auditor. Stress test and audit this code for security, 8GB memory leaks, and syntax bugs:\n{code}"
                ).text if client else "QA Audit passed."

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
                positioning = client.models.generate_content(
                    model=MODEL,
                    contents=f"You are Marcus Vance, CEO. Define the target audience, pricing tiers, and value proposition for: {beta_goal}"
                ).text if client else "Mock Value Prop generated."

                st.write("🎨 **Sora (Product Designer)** is crafting design tokens & UI components...")
                design = client.models.generate_content(
                    model=MODEL,
                    contents=f"You are Sora Takahashi, Product Designer. Create UI wireframe specs, Tailwind tokens, and layout guidelines for:\n{positioning}"
                ).text if client else "Mock Design Tokens generated."

                st.write("📈 **Maya (Growth & Ops)** is drafting launch copy & email sequences...")
                marketing = client.models.generate_content(
                    model=MODEL,
                    contents=f"You are Maya Lin, Head of Growth. Write high-converting viral launch copy, a 5-part email welcome sequence, and social posts for:\n{positioning}"
                ).text if client else "Mock Marketing Copy generated."

                status.update(label="✅ Team Beta Sprint Complete!", state="complete")

            b1, b2, b3 = st.tabs(["🎯 Positioning (Marcus)", "🎨 UI/UX Design System (Sora)", "📈 Growth & Copy (Maya)"])
            with b1: st.markdown(positioning)
            with b2: st.markdown(design)
            with b3: st.markdown(marketing)
