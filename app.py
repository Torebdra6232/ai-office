import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
MODEL = "gemma-4-26b-a4b-it"

# 1. Page Configuration
st.set_page_config(
    page_title="AutoOffice OS · Autonomous AI Command",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Sleek Dark Cyber-Executive Theme CSS
st.markdown("""
<style>
    /* Dark Theme Background */
    .stApp {
        background: radial-gradient(circle at 50% 0%, #0f172a 0%, #020617 100%);
        color: #f8fafc;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    
    /* Executive Agent Cards */
    .agent-card {
        background: rgba(15, 23, 42, 0.7);
        border: 1px solid rgba(56, 189, 248, 0.2);
        border-radius: 16px;
        padding: 18px;
        backdrop-filter: blur(10px);
        margin-bottom: 12px;
        transition: all 0.2s ease-in-out;
    }
    .agent-card:hover {
        border-color: rgba(56, 189, 248, 0.5);
        box-shadow: 0 0 20px rgba(56, 189, 248, 0.15);
    }
    
    /* Glowing Badges */
    .badge-ceo { background: rgba(245, 158, 11, 0.2); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.4); border-radius: 9999px; padding: 2px 10px; font-size: 11px; font-weight: bold; }
    .badge-cto { background: rgba(59, 130, 246, 0.2); color: #60a5fa; border: 1px solid rgba(59, 130, 246, 0.4); border-radius: 9999px; padding: 2px 10px; font-size: 11px; font-weight: bold; }
    .badge-dev { background: rgba(16, 185, 129, 0.2); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.4); border-radius: 9999px; padding: 2px 10px; font-size: 11px; font-weight: bold; }
    
    /* Custom Input Box */
    .stTextInput > div > div > input {
        background-color: #0b0f19 !important;
        border: 1px solid #1e293b !important;
        color: #f1f5f9 !important;
        border-radius: 12px !important;
        padding: 12px 16px !important;
    }
    .stTextInput > div > div > input:focus {
        border-color: #38bdf8 !important;
        box-shadow: 0 0 10px rgba(56, 189, 248, 0.2) !important;
    }

    /* Primary Launch Button */
    .stButton > button {
        background: linear-gradient(135deg, #2563eb, #4f46e5) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 10px 24px !important;
        font-weight: 700 !important;
        box-shadow: 0 4px 14px rgba(37, 99, 235, 0.3) !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Header Banner
st.markdown("""
<div style="display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #1e293b; padding-bottom: 20px; margin-bottom: 24px;">
    <div>
        <span style="background: rgba(56, 189, 248, 0.1); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.3); font-size: 11px; font-weight: 800; padding: 4px 12px; border-radius: 20px; text-transform: uppercase;">AutoOffice OS · v2.4</span>
        <h1 style="color: #f8fafc; font-size: 32px; font-weight: 800; margin: 8px 0 4px 0; letter-spacing: -0.5px;">Autonomous AI Headquarters</h1>
        <p style="color: #94a3b8; font-size: 13px; margin: 0;">Multi-Agent Orchestration Engine · Powered by Google Gemma on 8GB Hardware</p>
    </div>
    <div style="background: #090d16; border: 1px solid #1e293b; padding: 10px 16px; border-radius: 14px; text-align: right;">
        <span style="color: #10b981; font-size: 11px; font-weight: bold;">● Active & Ready</span><br/>
        <span style="color: #64748b; font-family: monospace; font-size: 12px;">RAM: 64 MB / 8.0 GB</span>
    </div>
</div>
""", unsafe_allow_html=True)

# 4. Live Agent Roster Preview
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("""
    <div class="agent-card">
        <span class="badge-ceo">EXECUTIVE</span>
        <h4 style="margin: 8px 0 2px 0; color: #f8fafc;">Marcus Vance</h4>
        <p style="color: #94a3b8; font-size: 12px; margin: 0;">CEO & Strategy Orchestrator</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="agent-card">
        <span class="badge-cto">ARCHITECTURE</span>
        <h4 style="margin: 8px 0 2px 0; color: #f8fafc;">Elena Rostova</h4>
        <p style="color: #94a3b8; font-size: 12px; margin: 0;">Chief Systems Architect</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="agent-card">
        <span class="badge-dev">ENGINEERING</span>
        <h4 style="margin: 8px 0 2px 0; color: #f8fafc;">Devon Vance</h4>
        <p style="color: #94a3b8; font-size: 12px; margin: 0;">Lead Full-Stack Developer</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# 5. Mission Input Bar
goal = st.text_input(
    "🎯 Dispatch Business Mission:", 
    placeholder="e.g. Build an automated YouTube script generator with viral hooks and SEO metadata..."
)

if st.button("🚀 Kickoff Autonomous Sprint", use_container_width=True):
    if not goal:
        st.warning("Please enter a mission first!")
    else:
        with st.status("⚡ AutoOffice Autonomous Pipeline Active...", expanded=True) as status:
            
            # Step 1: CEO
            st.write("👔 **Marcus Vance (CEO)** is structuring the Product Requirements Document (PRD)...")
            ceo_res = client.models.generate_content(
                model=MODEL,
                contents=f"You are Marcus Vance, CEO. Formulate a comprehensive, structured PRD for: {goal}"
            ).text
            
            # Step 2: CTO
            st.write("📐 **Elena Rostova (CTO)** is generating database schema and API architecture...")
            cto_res = client.models.generate_content(
                model=MODEL,
                contents=f"You are Elena Rostova, CTO. Review this PRD and design the technical schema:\n{ceo_res}"
            ).text

            # Step 3: Lead Developer
            st.write("💻 **Devon Vance (Lead Dev)** is writing full production-ready code...")
            dev_res = client.models.generate_content(
                model=MODEL,
                contents=f"You are Devon Vance, Lead Engineer. Write clean, complete code fulfilling this architecture:\n{cto_res}"
            ).text
            
            status.update(label="🎉 SPRINT COMPLETE: All Deliverables Vaulted!", state="complete", expanded=False)

        # 6. Deliverables Vault Tabs
        st.markdown("### 🗄️ Deliverables Vault")
        tab1, tab2, tab3 = st.tabs(["📋 Executive PRD", "🏗️ Technical Blueprint", "💻 Full Source Code"])
        
        with tab1:
            st.markdown(ceo_res)
        with tab2:
            st.markdown(cto_res)
        with tab3:
            st.code(dev_res, language="python")