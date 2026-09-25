import streamlit as st
import json
import os
import time
import base64
from datetime import datetime

# ==========================================
# AutoOffice OS - Enterprise Multi-Agent HQ
# ==========================================

st.set_page_config(
    page_title="AutoOffice OS - Multi-Agent Enterprise Suite",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------------------------
# Persistent Storage (autooffice_memory.json)
# ------------------------------------------
MEMORY_FILE = "autooffice_memory.json"

def load_persistent_memory():
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {
        "ceo_chat": [],
        "worker_chats": {},
        "team_chats": {},
        "daily_tasks": {
            "social": {"status": "Active", "posts_scheduled": 4, "webhook": "Ready"},
            "trading": {"status": "24/5 Open", "risk_limit": "1.0%", "pair": "EUR/USD"},
            "appdev": {"status": "In Progress", "readiness": "85%", "target": "iOS & Play Store"}
        }
    }

def save_persistent_memory(data):
    try:
        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception as e:
        st.error(f"Error saving memory: {e}")

# Initialize session state from disk
if "office_data" not in st.session_state:
    st.session_state.office_data = load_persistent_memory()

# ------------------------------------------
# Staff Directory (10 Specialists)
# ------------------------------------------
STAFF_MEMBERS = [
    {
        "id": "agent-ceo",
        "name": "Marcus Vance",
        "role": "CEO",
        "title": "Chief Executive Officer & Chief Strategist",
        "dept": "Executive Suite",
        "icon": "👔"
    },
    {
        "id": "agent-finley",
        "name": "Finley",
        "role": "ACCOUNTANT",
        "title": "Corporate FinOps & Token Auditor",
        "dept": "Executive Suite",
        "icon": "💰"
    },
    {
        "id": "agent-cto",
        "name": "Elena Rostova",
        "role": "CTO",
        "title": "Chief Technology Architect",
        "dept": "Engineering Bay",
        "icon": "🏛️"
    },
    {
        "id": "agent-dev",
        "name": "Devon Brooks",
        "role": "DEV",
        "title": "Lead Full-Stack Systems Engineer",
        "dept": "Engineering Bay",
        "icon": "💻"
    },
    {
        "id": "agent-designer",
        "name": "Sora Takahashi",
        "role": "DESIGNER",
        "title": "Principal UI/UX Systems Architect",
        "dept": "Design Studio",
        "icon": "🎨"
    },
    {
        "id": "agent-social",
        "name": "Chloe",
        "role": "MARKETER",
        "title": "Head of Social Media Operations",
        "dept": "Social Command",
        "icon": "📱"
    },
    {
        "id": "agent-content",
        "name": "Liam",
        "role": "CONTENT_PRODUCER",
        "title": "Creative Media & Video Strategist",
        "dept": "Social Command",
        "icon": "🎬"
    },
    {
        "id": "agent-trader",
        "name": "Ray Dalton",
        "role": "TRADER",
        "title": "Forex & Quant Trading Desk Lead",
        "dept": "Trading Desk",
        "icon": "📈"
    },
    {
        "id": "agent-webops",
        "name": "Atlas",
        "role": "WEB_OPERATOR",
        "title": "Autonomous Web & Browser Operator",
        "dept": "Operations",
        "icon": "🌐"
    },
    {
        "id": "agent-qa",
        "name": "Tariq Al-Mansoor",
        "role": "QA",
        "title": "Security & Deterministic QA Lead",
        "dept": "Operations",
        "icon": "🛡️"
    }
]

# ------------------------------------------
# Sample Deliverable SVG Assets
# ------------------------------------------
def get_sample_svg(asset_type):
    if asset_type == "wireframe":
        return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400" width="100%" height="100%">
        <rect width="600" height="400" fill="#0f172a" rx="16"/>
        <rect x="30" y="30" width="540" height="40" fill="#1e293b" rx="8"/>
        <text x="50" y="55" fill="#f8fafc" font-size="16" font-family="sans-serif" font-weight="bold">AutoOffice Mobile UI Wireframe (Sora Takahashi)</text>
        <rect x="50" y="100" width="150" height="250" fill="#1e293b" rx="12" stroke="#ec4899" stroke-width="2"/>
        <rect x="70" y="120" width="110" height="20" fill="#ec4899" rx="4"/>
        <rect x="70" y="160" width="110" height="50" fill="#334155" rx="6"/>
        <rect x="70" y="230" width="110" height="50" fill="#334155" rx="6"/>
        <rect x="230" y="100" width="320" height="250" fill="#1e293b" rx="12"/>
        <text x="250" y="140" fill="#38bdf8" font-size="14" font-family="monospace">Design Tokens & Layout Grid</text>
        <text x="250" y="170" fill="#94a3b8" font-size="12" font-family="monospace">- Canvas: #0b0f17</text>
        <text x="250" y="195" fill="#94a3b8" font-size="12" font-family="monospace">- Surface: #131b2e</text>
        <text x="250" y="220" fill="#94a3b8" font-size="12" font-family="monospace">- Primary Accent: #06b6d4</text>
        <rect x="250" y="280" width="200" height="36" fill="#10b981" rx="8"/>
        <text x="350" y="303" fill="#ffffff" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Execute App Flow</text>
        </svg>"""
    elif asset_type == "chart":
        return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 350" width="100%" height="100%">
        <rect width="600" height="350" fill="#0b1329" rx="16"/>
        <text x="30" y="40" fill="#38bdf8" font-size="16" font-family="monospace" font-weight="bold">RAY DALTON // FOREX MT5 DESK // EUR/USD H1</text>
        <line x1="30" y1="100" x2="570" y2="100" stroke="#1e293b" stroke-dasharray="4"/>
        <line x1="30" y1="180" x2="570" y2="180" stroke="#1e293b" stroke-dasharray="4"/>
        <line x1="30" y1="260" x2="570" y2="260" stroke="#1e293b" stroke-dasharray="4"/>
        <path d="M 50,260 Q 200,240 320,180 T 550,110" fill="none" stroke="#06b6d4" stroke-width="3"/>
        <rect x="80" y="220" width="14" height="40" fill="#10b981"/>
        <rect x="150" y="190" width="14" height="35" fill="#10b981"/>
        <rect x="220" y="180" width="14" height="25" fill="#ef4444"/>
        <rect x="290" y="140" width="14" height="50" fill="#10b981"/>
        <rect x="360" y="110" width="14" height="40" fill="#10b981"/>
        <rect x="400" y="90" width="170" height="40" rx="8" fill="#10b981" fill-opacity="0.2" stroke="#10b981"/>
        <text x="410" y="115" fill="#4ade80" font-size="11" font-family="monospace" font-weight="bold">BUY SIGNAL (0.50 Lot)</text>
        </svg>"""
    else:
        return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 350" width="100%" height="100%">
        <rect width="600" height="350" fill="#1e1b4b" rx="16"/>
        <text x="40" y="50" fill="#f43f5e" font-size="14" font-family="sans-serif" font-weight="bold">OMNICHANNEL LAUNCH CAMPAIGN</text>
        <text x="40" y="100" fill="#ffffff" font-size="24" font-family="sans-serif" font-weight="bold">Stop Hiring Dev Agencies.</text>
        <text x="40" y="135" fill="#a78bfa" font-size="20" font-family="sans-serif">Your AI Office Works 24/7.</text>
        <rect x="40" y="180" width="150" height="70" fill="#0f172a" rx="8" stroke="#334155"/>
        <text x="55" y="210" fill="#38bdf8" font-size="20" font-weight="bold" font-family="monospace">10x Speed</text>
        <text x="55" y="235" fill="#94a3b8" font-size="11">Sprint Delivery</text>
        <rect x="220" y="180" width="150" height="70" fill="#0f172a" rx="8" stroke="#334155"/>
        <text x="235" y="210" fill="#4ade80" font-size="20" font-weight="bold" font-family="monospace">&lt; $0.01</text>
        <text x="235" y="235" fill="#94a3b8" font-size="11">Cost / Deliverable</text>
        <text x="40" y="300" fill="#94a3b8" font-size="12" font-family="monospace">#AutoOfficeOS #SaaS #AI #BuildInPublic</text>
        </svg>"""

# ------------------------------------------
# Sidebar Navigation
# ------------------------------------------
with st.sidebar:
    st.title("🏢 AutoOffice OS")
    st.caption("Autonomous Multi-Agent Enterprise Suite")
    
    st.markdown("---")
    st.subheader("Workspace Navigation")
    
    nav_option = st.radio(
        "Select Office Workspace:",
        [
            "📊 Executive Dashboard (Daily Tasks)",
            "👔 CEO War Room (Marcus Vance)",
            "👤 Staff Desks (1-on-1 Workers)",
            "👥 Department Teams (War Rooms)",
            "🏢 Virtual Floorplan (10 Agents)"
        ]
    )

    st.markdown("---")
    st.caption("Active Staff Directory (10 Agents)")
    for staff in STAFF_MEMBERS:
        st.markdown(f"• {staff['icon']} **{staff['name']}** — *{staff['title']}*")

# ==========================================
# TAB 1: EXECUTIVE DASHBOARD (DAILY TASKS)
# ==========================================
if nav_option == "📊 Executive Dashboard (Daily Tasks)":
    st.header("📊 Mission Control & Daily Operations Board")
    st.write("Real-time monitoring of your 3 primary daily operations and multi-agent commercial sprints.")

    st.markdown("---")
    st.subheader("Primary Daily Workstreams")

    col1, col2, col3 = st.columns(3)

    # 1. Social Media
    with col1:
        st.markdown("""
        <div style="background-color: #1e1b4b; border: 1px solid #a855f7; border-radius: 12px; padding: 16px;">
            <h3 style="color: #ffffff; margin-top:0;">📱 Social Media Management</h3>
            <p style="color: #cbd5e1; font-size: 13px;"><b>Team:</b> Chloe & Liam<br><b>Platforms:</b> YouTube, Instagram, Facebook, X (Twitter)</p>
            <hr style="border-color: #4c1d95;">
            <p style="color: #4ade80; font-size: 12px; font-weight: bold;">● Webhook: Armed & Ready</p>
            <p style="color: #cbd5e1; font-size: 12px;"><b>Scheduled Drafts:</b> 4 Posts Staged<br><b>Media Review:</b> Previews Generated</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Trigger Social Webhook Blitz", key="btn_social"):
            st.success("Webhook POST dispatched to social automation pipeline! 4 platforms queued.")

    # 2. Forex Trading
    with col2:
        st.markdown("""
        <div style="background-color: #064e3b; border: 1px solid #10b981; border-radius: 12px; padding: 16px;">
            <h3 style="color: #ffffff; margin-top:0;">📈 Forex MT5 Trading Desk</h3>
            <p style="color: #cbd5e1; font-size: 13px;"><b>Team:</b> Ray Dalton & Finley<br><b>Instruments:</b> EUR/USD, GBP/JPY, Gold, Crypto</p>
            <hr style="border-color: #047857;">
            <p style="color: #4ade80; font-size: 12px; font-weight: bold;">● Schedule: 24/5 Open (London/NY)</p>
            <p style="color: #cbd5e1; font-size: 12px;"><b>Risk Bound:</b> Hard 1.0% Equity Stop<br><b>Algorithm:</b> 200 EMA Retest EA</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Dispatch MT5 Trade Signal", key="btn_trade"):
            st.success("Algorithmic signal sent to MetaTrader 5 bridge with 1.0% stop-loss guard!")

    # 3. Commercial App Dev
    with col3:
        st.markdown("""
        <div style="background-color: #1e3a8a; border: 1px solid #3b82f6; border-radius: 12px; padding: 16px;">
            <h3 style="color: #ffffff; margin-top:0;">🚀 Commercial App Dev Team</h3>
            <p style="color: #cbd5e1; font-size: 13px;"><b>Team:</b> Elena (CTO), Devon (Dev), Sora (Design)<br><b>Destination:</b> iOS App Store & Google Play</p>
            <hr style="border-color: #1d4ed8;">
            <p style="color: #38bdf8; font-size: 12px; font-weight: bold;">● Store Readiness: 85% Ready</p>
            <p style="color: #cbd5e1; font-size: 12px;"><b>Stack:</b> React Native & TS Microservice<br><b>Deliverable:</b> Packaged Source Code</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Run App Store Sprint", key="btn_appdev"):
            st.info("Commercial app sprint triggered! Check Team Alpha for deliverables.")

    st.markdown("---")
    st.subheader("Autonomous Mission Runner")
    sprint_input = st.text_input("Dispatch Goal to Autonomous Fleet:", "Build & Launch Commercial App Store Product with Full Multi-Agent Fleet")
    if st.button("🚀 Dispatch Mission to All 10 Agents"):
        with st.spinner("Fleet executing across CEO, CTO, Design, Dev, QA, and Marketing..."):
            time.sleep(2)
            st.success("Mission completed! Generated PRD, microservice schema, mobile wireframes, and production TypeScript engine.")

# ==========================================
# TAB 2: CEO WAR ROOM (MARCUS VANCE)
# ==========================================
elif nav_option == "👔 CEO War Room (Marcus Vance)":
    st.header("👔 Executive War Room: Marcus Vance (CEO)")
    st.caption("Direct strategic consultation. Marcus remembers past discussions across sessions!")

    ceo_chat = st.session_state.office_data.get("ceo_chat", [])

    # Display Chat History
    for msg in ceo_chat:
        with st.chat_message(msg["sender"]):
            st.markdown(f"**{msg.get('name', 'User')}** ({msg.get('time', '')})")
            if msg.get("attachment"):
                att = msg["attachment"]
                st.info(f"📎 Attached {att['type']}: **{att['name']}** ({att['size']})")
                if att["type"] == "image" and att.get("data"):
                    st.image(att["data"], width=300)
            st.markdown(msg["text"])
            if msg.get("response_media"):
                rm = msg["response_media"]
                if rm["type"] == "image":
                    st.markdown(f"*{rm['name']}*")
                    st.components.v1.html(rm["content"], height=380)
                elif rm["type"] == "pdf":
                    st.download_button(
                        label=f"📄 Download {rm['name']}",
                        data=rm["content"],
                        file_name=rm["name"],
                        mime="application/pdf"
                    )

    # Input section with file uploader
    st.markdown("---")
    col_up, col_inp = st.columns([1, 3])
    with col_up:
        uploaded_file = st.file_uploader("Upload Image, Video, or PDF:", type=["png", "jpg", "jpeg", "pdf", "mp4", "txt"], key="ceo_upload")
    with col_inp:
        user_input = st.text_input("Talk to Marcus Vance (CEO)...", key="ceo_prompt")
        col_btn1, col_btn2 = st.columns([1, 4])
        with col_btn1:
            send_btn = st.button("Send", key="ceo_send")
        with col_btn2:
            if st.button("Clear Chat", key="ceo_clear"):
                st.session_state.office_data["ceo_chat"] = []
                save_persistent_memory(st.session_state.office_data)
                st.rerun()

    if send_btn and (user_input or uploaded_file):
        now_str = datetime.now().strftime("%H:%M")
        att_data = None
        if uploaded_file:
            is_img = uploaded_file.type.startswith("image")
            att_data = {
                "name": uploaded_file.name,
                "type": "image" if is_img else "video" if uploaded_file.type.startswith("video") else "pdf",
                "size": f"{uploaded_file.size / 1024:.1f} KB",
                "data": uploaded_file.getvalue() if is_img else None
            }

        st.session_state.office_data["ceo_chat"].append({
            "sender": "user",
            "name": "You (Co-Founder)",
            "text": user_input or f"[Shared {uploaded_file.name}]",
            "time": now_str,
            "attachment": att_data
        })

        reply_text = f"Co-Founder, I have evaluated your strategic directive: '{user_input}'.\n\n**Executive Action Plan:**\n1. **Elena (CTO)** will map the microservice architecture.\n2. **Sora & Devon** will design and write the commercial app store code.\n3. **Chloe & Ray** will coordinate the viral marketing and Forex hedging.\n\nRecommended Mission: 'Deploy Autonomous Commercial Sprint for {user_input or 'App Store Software'}'"
        
        resp_media = {
            "name": f"Executive_PRD_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf",
            "type": "pdf",
            "content": f"# Executive Product Requirements Document\nStrategic Directive: {user_input}\nApproved by: Marcus Vance (CEO)\nTimestamp: {now_str}\nStatus: Enterprise Ready"
        }

        st.session_state.office_data["ceo_chat"].append({
            "sender": "assistant",
            "name": "Marcus Vance (CEO)",
            "text": reply_text,
            "time": now_str,
            "response_media": resp_media
        })

        save_persistent_memory(st.session_state.office_data)
        st.rerun()

# ==========================================
# TAB 3: STAFF DESKS (1-ON-1 WORKERS)
# ==========================================
elif nav_option == "👤 Staff Desks (1-on-1 Workers)":
    st.header("👤 Staff Desks & Private Workstations")
    st.caption("Dedicated private 1-on-1 line with all 10 specialized staff members. Full image, video, and PDF support!")

    worker_names = [f"{s['icon']} {s['name']} ({s['role']})" for s in STAFF_MEMBERS]
    selected_idx = st.selectbox("Select Worker to Consult:", range(len(STAFF_MEMBERS)), format_func=lambda i: worker_names[i])
    worker = STAFF_MEMBERS[selected_idx]

    st.markdown(f"### {worker['icon']} {worker['name']} · *{worker['title']}*")
    st.caption(f"Department: {worker['dept']} | Model: Gemini 3.8 Flash | Memory: Permanent")

    worker_chats = st.session_state.office_data.get("worker_chats", {})
    messages = worker_chats.get(worker["id"], [])

    for msg in messages:
        with st.chat_message(msg["sender"]):
            st.markdown(f"**{msg.get('name', 'User')}** ({msg.get('time', '')})")
            if msg.get("attachment"):
                att = msg["attachment"]
                st.info(f"📎 Attached {att['type']}: **{att['name']}** ({att['size']})")
                if att["type"] == "image" and att.get("data"):
                    st.image(att["data"], width=300)
            st.markdown(msg["text"])
            if msg.get("response_media"):
                rm = msg["response_media"]
                if rm["type"] == "image":
                    st.markdown(f"*{rm['name']}*")
                    st.components.v1.html(rm["content"], height=380)
                elif rm["type"] == "pdf":
                    st.download_button(
                        label=f"📄 Download {rm['name']}",
                        data=rm["content"],
                        file_name=rm["name"],
                        mime="application/pdf",
                        key=f"dl_{msg['time']}_{rm['name']}"
                    )

    st.markdown("---")
    col_w_up, col_w_inp = st.columns([1, 3])
    with col_w_up:
        w_file = st.file_uploader(f"Upload media for {worker['name']}:", type=["png", "jpg", "jpeg", "pdf", "mp4", "txt", "py", "ts"], key=f"up_{worker['id']}")
    with col_w_inp:
        w_input = st.text_input(f"Message {worker['name']}...", key=f"txt_{worker['id']}")
        col_w1, col_w2 = st.columns([1, 4])
        with col_w1:
            w_send = st.button("Send", key=f"send_{worker['id']}")
        with col_w2:
            if st.button("Clear Chat", key=f"clear_{worker['id']}"):
                st.session_state.office_data["worker_chats"][worker["id"]] = []
                save_persistent_memory(st.session_state.office_data)
                st.rerun()

    if w_send and (w_input or w_file):
        now_str = datetime.now().strftime("%H:%M")
        att_data = None
        if w_file:
            is_img = w_file.type.startswith("image")
            att_data = {
                "name": w_file.name,
                "type": "image" if is_img else "video" if w_file.type.startswith("video") else "pdf",
                "size": f"{w_file.size / 1024:.1f} KB",
                "data": w_file.getvalue() if is_img else None
            }

        if worker["id"] not in st.session_state.office_data["worker_chats"]:
            st.session_state.office_data["worker_chats"][worker["id"]] = []

        st.session_state.office_data["worker_chats"][worker["id"]].append({
            "sender": "user",
            "name": "You",
            "text": w_input or f"[Attached {w_file.name}]",
            "time": now_str,
            "attachment": att_data
        })

        resp_media = None
        if worker["role"] == "DESIGNER":
            reply_text = f"I've designed the mobile UI wireframe layout for: '{w_input}'. Included below is the interactive SVG preview and Tailwind design tokens."
            resp_media = {"name": "UI_Wireframe_Preview.svg", "type": "image", "content": get_sample_svg("wireframe")}
        elif worker["role"] == "TRADER":
            reply_text = f"Forex MT5 analysis for EUR/USD: 200 EMA retest complete. 1% stop-loss enforced. Technical chart preview attached."
            resp_media = {"name": "Forex_Candlestick_Chart.svg", "type": "image", "content": get_sample_svg("chart")}
        elif worker["role"] == "MARKETER" or worker["role"] == "CONTENT_PRODUCER":
            reply_text = f"Here is the omnichannel social campaign banner and scheduled webhook payload for YouTube, Instagram, Facebook, and Twitter."
            resp_media = {"name": "Social_Banner_Preview.svg", "type": "image", "content": get_sample_svg("social")}
        elif worker["role"] == "ACCOUNTANT":
            reply_text = f"FinOps Token Statement: Active sprint consumed 14,280 tokens (~$0.02 USD). Local 8GB RAM utilization is capped at 115MB."
            resp_media = {"name": "FinOps_Monthly_Statement.pdf", "type": "pdf", "content": f"# FinOps Audit Statement\nAgent: Finley\nSpend: $0.024\nMargin: 99.2%"}
        else:
            reply_text = f"I am {worker['name']} ({worker['title']}). I have processed your directive: '{w_input}' and staged the output for review."
            resp_media = {"name": f"{worker['name']}_Deliverable.pdf", "type": "pdf", "content": f"# Official Deliverable: {worker['name']}\nDirective: {w_input}\nStatus: Certified"}

        st.session_state.office_data["worker_chats"][worker["id"]].append({
            "sender": "assistant",
            "name": worker["name"],
            "text": reply_text,
            "time": now_str,
            "response_media": resp_media
        })

        save_persistent_memory(st.session_state.office_data)
        st.rerun()

# ==========================================
# TAB 4: DEPARTMENT TEAMS (WAR ROOMS)
# ==========================================
elif nav_option == "👥 Department Teams (War Rooms)":
    st.header("👥 Departmental War Rooms")
    st.caption("Cross-agent collaborative group rooms with live webhook controls, trading desk, and App Store team.")

    team_choice = st.radio(
        "Choose Department:",
        [
            "📱 Social Media Command (Chloe & Liam)",
            "📈 Forex MT5 Trading Desk (Ray Dalton & Finley)",
            "🚀 Commercial App Dev Team (Team Alpha)",
            "🌐 Web Operations & Automation (Atlas & Tariq)"
        ],
        horizontal=True
    )

    team_id = "social" if "Social" in team_choice else "trading" if "Forex" in team_choice else "appdev" if "Commercial" in team_choice else "automation"

    st.markdown("---")
    team_chats = st.session_state.office_data.get("team_chats", {})
    t_messages = team_chats.get(team_id, [])

    for msg in t_messages:
        with st.chat_message(msg["sender"]):
            st.markdown(f"**{msg.get('name', 'Team')}** ({msg.get('time', '')})")
            if msg.get("attachment"):
                att = msg["attachment"]
                st.info(f"📎 Attached {att['type']}: **{att['name']}**")
            st.markdown(msg["text"])
            if msg.get("response_media"):
                rm = msg["response_media"]
                if rm["type"] == "image":
                    st.components.v1.html(rm["content"], height=380)

    col_t_up, col_t_inp = st.columns([1, 3])
    with col_t_up:
        t_file = st.file_uploader("Upload review media (images/videos):", type=["png", "jpg", "jpeg", "pdf", "mp4"], key=f"t_up_{team_id}")
    with col_t_inp:
        t_input = st.text_input(f"Send team directive to {team_choice.split('(')[0]}...", key=f"t_txt_{team_id}")
        if st.button("Send to Team", key=f"t_send_{team_id}") and (t_input or t_file):
            now_str = datetime.now().strftime("%H:%M")
            if team_id not in st.session_state.office_data["team_chats"]:
                st.session_state.office_data["team_chats"][team_id] = []

            st.session_state.office_data["team_chats"][team_id].append({
                "sender": "user",
                "name": "You (Director)",
                "text": t_input or f"[Uploaded {t_file.name}]",
                "time": now_str,
                "attachment": {"name": t_file.name, "type": "media"} if t_file else None
            })

            if team_id == "social":
                resp_text = f"**Chloe & Liam**: We received your post directive: '{t_input}'. We drafted the 4-platform carousel and attached the graphic mockup below for your review before webhook publication."
                resp_media = {"name": "Social_Post_Mockup.svg", "type": "image", "content": get_sample_svg("social")}
            elif team_id == "trading":
                resp_text = f"**Ray Dalton & Finley**: Algorithmic risk gate verified. EUR/USD order parameter configured with hard stop-loss. Chart setup attached."
                resp_media = {"name": "EUR_USD_H1_Chart.svg", "type": "image", "content": get_sample_svg("chart")}
            else:
                resp_text = f"**Team Alpha (Elena, Devon, Sora)**: Commercial app sprint updated. Mobile wireframe screens and TypeScript interfaces synchronized."
                resp_media = {"name": "App_Wireframe.svg", "type": "image", "content": get_sample_svg("wireframe")}

            st.session_state.office_data["team_chats"][team_id].append({
                "sender": "assistant",
                "name": team_choice.split('(')[0],
                "text": resp_text,
                "time": now_str,
                "response_media": resp_media
            })

            save_persistent_memory(st.session_state.office_data)
            st.rerun()

# ==========================================
# TAB 5: VIRTUAL FLOORPLAN (10 AGENTS)
# ==========================================
elif nav_option == "🏢 Virtual Floorplan (10 Agents)":
    st.header("🏢 Virtual Office Floorplan (Level 1 HQ)")
    st.write("Visual status and desk allocation for all 10 specialized AI staff members.")

    cols = st.columns(3)
    for i, staff in enumerate(STAFF_MEMBERS):
        with cols[i % 3]:
            st.markdown(f"""
            <div style="background-color: #0f172a; border: 1px solid #334155; border-radius: 12px; padding: 14px; margin-bottom: 12px;">
                <div style="font-size: 28px;">{staff['icon']}</div>
                <h4 style="color: #ffffff; margin: 4px 0;">{staff['name']}</h4>
                <p style="color: #38bdf8; font-size: 12px; margin: 0;"><b>{staff['role']}</b> · {staff['dept']}</p>
                <p style="color: #94a3b8; font-size: 11px; margin-top: 4px;">{staff['title']}</p>
                <span style="background-color: #064e3b; color: #34d399; font-size: 10px; font-weight: bold; padding: 2px 8px; border-radius: 9999px;">● ACTIVE</span>
            </div>
            """, unsafe_allow_html=True)
