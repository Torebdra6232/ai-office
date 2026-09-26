"""
AutoOffice OS - Autonomous Multi-Agent Enterprise Suite (Complete Streamlit Edition)
Self-Contained Production Source Code for Streamlit Cloud and Local Deployment.

Features:
- High-Density Command Bridge Dark Widescreen Interface
- All 11 Specialized Enterprise Staff Members with strictly separated domain expertise
- 🎨 Sora: UI/UX & Design Tokens | 💻 Devon: Full-Stack Code | 🏛️ Elena: CTO Architecture
- 📱 Chloe: Social Media Command | 🎬 Liam: Video Strategy | 📈 Ray Dalton: MT5 Forex Quant
- 💰 Finley: FinOps & Treasury Ledger | 🌐 Atlas: Web Ops Bots | 🛡️ Tariq: Security QA
- ⚡ Kaelen Voss: FinTech & API Bridges | 👔 Marcus Vance: CEO & Strategy
- ⚡ STRICT WORKING MANDATE: Short, honest, results-first responses
- 🛡️ Executive Profit Vault & Treasury
- 📋 Real Dynamic Task Manager & Human Approvals Gate
- 📈 Dedicated Live Trades MT5 Terminal - DEMO/PAPER MODE
- 👥 Department Teams
- 🏢 Virtual 2D Floorplan
- 💻 Code & Deliverables Vault
- 🌐 Live Web & Tab Inspector
- 100% Fault-Tolerant Session State
"""

import streamlit as st
import json
import os
import time
import base64
import re
import ssl
import urllib.request
import urllib.error
from datetime import datetime


# ==============================================================================
# PAGE CONFIGURATION
# ==============================================================================

st.set_page_config(
    page_title="AutoOffice OS - Multi-Agent Enterprise Command Deck",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ==============================================================================
# HIGH-DENSITY COMMAND DECK CSS
# ==============================================================================

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

html, body, [class*="css"], [class*="st-"] {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
}

.stApp {
    background: radial-gradient(
        circle at 50% 0%,
        #0d1527 0%,
        #080c16 65%,
        #030509 100%
    ) !important;
    color: #f1f5f9;
}

header[data-testid="stHeader"] {
    background: rgba(8, 12, 22, 0.9) !important;
    backdrop-filter: blur(16px);
    border-bottom: 1px solid rgba(51, 65, 85, 0.4);
}

section[data-testid="stSidebar"] {
    background: #060911 !important;
    border-right: 1px solid #1e293b !important;
}

.deck-card {
    background: linear-gradient(
        135deg,
        rgba(23, 33, 54, 0.7) 0%,
        rgba(11, 18, 32, 0.9) 100%
    );
    border: 1px solid rgba(71, 85, 105, 0.35);
    border-radius: 16px;
    padding: 18px;
    box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.6);
    margin-bottom: 14px;
    transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}

.deck-card:hover {
    border-color: rgba(56, 189, 248, 0.55);
    transform: translateY(-2px);
    box-shadow: 0 14px 34px -4px rgba(6, 182, 212, 0.15);
}

.glow-emerald {
    background: linear-gradient(
        135deg,
        rgba(6, 78, 59, 0.3) 0%,
        rgba(11, 18, 32, 0.95) 100%
    ) !important;
    border: 1px solid rgba(16, 185, 129, 0.5) !important;
}

.glow-cyan {
    background: linear-gradient(
        135deg,
        rgba(8, 51, 68, 0.3) 0%,
        rgba(11, 18, 32, 0.95) 100%
    ) !important;
    border: 1px solid rgba(6, 182, 212, 0.5) !important;
}

.glow-indigo {
    background: linear-gradient(
        135deg,
        rgba(49, 46, 129, 0.3) 0%,
        rgba(11, 18, 32, 0.95) 100%
    ) !important;
    border: 1px solid rgba(99, 102, 241, 0.5) !important;
}

.glow-amber {
    background: linear-gradient(
        135deg,
        rgba(120, 53, 15, 0.3) 0%,
        rgba(11, 18, 32, 0.95) 100%
    ) !important;
    border: 1px solid rgba(245, 158, 11, 0.5) !important;
}

.badge-pill {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    padding: 2px 8px;
    border-radius: 6px;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.badge-emerald {
    background: rgba(16, 185, 129, 0.15);
    color: #34d399;
    border: 1px solid rgba(16, 185, 129, 0.4);
}

.badge-cyan {
    background: rgba(6, 182, 212, 0.15);
    color: #22d3ee;
    border: 1px solid rgba(6, 182, 212, 0.4);
}

.badge-amber {
    background: rgba(245, 158, 11, 0.15);
    color: #fbbf24;
    border: 1px solid rgba(245, 158, 11, 0.4);
}

.badge-purple {
    background: rgba(168, 85, 247, 0.15);
    color: #c084fc;
    border: 1px solid rgba(168, 85, 247, 0.4);
}

.badge-rose {
    background: rgba(244, 63, 94, 0.15);
    color: #fb7185;
    border: 1px solid rgba(244, 63, 94, 0.4);
}

.badge-blue {
    background: rgba(59, 130, 246, 0.15);
    color: #60a5fa;
    border: 1px solid rgba(59, 130, 246, 0.4);
}

.ticker-pill {
    background: rgba(15, 23, 42, 0.85);
    border: 1px solid #334155;
    border-radius: 12px;
    padding: 10px 14px;
    transition: all 0.2s ease;
}

.ticker-pill:hover {
    border-color: #38bdf8;
    background: rgba(30, 41, 59, 0.9);
}

[data-testid="stChatMessage"] {
    background: rgba(15, 23, 42, 0.8) !important;
    border: 1px solid rgba(51, 65, 85, 0.5) !important;
    border-radius: 14px !important;
    padding: 14px 18px !important;
    margin-bottom: 12px !important;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3) !important;
}

.stButton > button {
    border-radius: 10px !important;
    font-weight: 700 !important;
    letter-spacing: 0.3px !important;
    transition: all 0.2s ease !important;
}

.stDownloadButton > button {
    background: linear-gradient(
        135deg,
        #059669 0%,
        #047857 100%
    ) !important;
    color: white !important;
    border-radius: 10px !important;
    border: none !important;
    font-weight: 700 !important;
    box-shadow: 0 4px 14px rgba(5, 150, 105, 0.3) !important;
}
</style>
""",
    unsafe_allow_html=True,
)


# ==============================================================================
# NATIVE BINARY PDF GENERATOR
# ==============================================================================

def create_valid_pdf_bytes(
    title,
    text_content,
    agent_name="AutoOffice Executive Engine",
):
    clean_title = (
        str(title)
        .replace("\\", "/")
        .replace("(", "[")
        .replace(")", "]")[:60]
    )

    clean_header = f"{clean_title} — {agent_name}"[:70]

    raw_lines = [
        line.strip()
        for line in str(text_content).split("\n")
        if line.strip()
    ]

    stream_content = (
        "BT\n"
        "/F2 14 Tf\n"
        "50 740 Td\n"
        f"({clean_header}) Tj\n"
        "/F1 9.5 Tf\n"
        "0 -22 Td\n"
        f"(Generated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}) Tj\n"
        "0 -18 Td\n"
        "(--------------------------------------------------------------------------------) Tj\n"
        "0 -16 Td\n"
    )

    for line in raw_lines[:40]:
        clean = (
            line
            .replace("\\", "/")
            .replace("(", "[")
            .replace(")", "]")
        )

        while len(clean) > 78:
            part = clean[:78]
            clean = clean[78:]
            stream_content += f"({part}) Tj\n0 -13 Td\n"

        stream_content += f"({clean}) Tj\n0 -13 Td\n"

    stream_content += (
        "(--------------------------------------------------------------------------------) Tj\n"
        "0 -16 Td\n"
        "(Verified & Authenticated by AutoOffice Autonomous Enterprise OS) Tj\n"
        "ET"
    )

    stream_bytes = stream_content.encode("latin1", errors="replace")

    objects = [
        b"1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n",
        b"2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n",
        (
            b"3 0 obj\n"
            b"<< /Type /Page /Parent 2 0 R "
            b"/MediaBox [0 0 612 792] "
            b"/Contents 4 0 R "
            b"/Resources << /Font << /F1 5 0 R /F2 6 0 R >> >> >>\n"
            b"endobj\n"
        ),
        (
            f"4 0 obj\n<< /Length {len(stream_bytes)} >>\n"
            "stream\n"
        ).encode("latin1")
        + stream_bytes
        + b"\nendstream\nendobj\n",
        b"5 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>\nendobj\n",
        b"6 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>\nendobj\n",
    ]

    pdf = b"%PDF-1.4\n"
    offsets = []

    for obj in objects:
        offsets.append(len(pdf))
        pdf += obj

    xref_offset = len(pdf)

    pdf += (
        f"xref\n0 {len(objects) + 1}\n"
        "0000000000 65535 f \n"
    ).encode("latin1")

    for offset in offsets:
        pdf += f"{offset:010d} 00000 n \n".encode("latin1")

    pdf += (
        f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\n"
        f"startxref\n{xref_offset}\n"
        "%%EOF\n"
    ).encode("latin1")

    return pdf


# ==============================================================================
# STAFF ROSTER DIRECTORY
# ==============================================================================

STAFF_MEMBERS = [
    {
        "id": "agent-ceo",
        "name": "Marcus Vance",
        "role": "CEO",
        "title": "Chief Executive Officer & Strategist",
        "dept": "Executive Suite",
        "icon": "👔",
        "badge_class": "badge-amber",
        "desk": "Desk 1 (Executive Desk)",
        "skills": [
            "PRD Generation",
            "Monetization Models",
            "Product Roadmap",
            "Team Orchestration",
        ],
        "prompt": (
            "You are Marcus Vance, CEO. You report directly to your Boss "
            "(the user). STRICT MANDATE: Deliver results immediately. "
            "Keep answers short, honest, and decisive. No fluff or "
            "corporate speeches."
        ),
    },
    {
        "id": "agent-designer",
        "name": "Sora Takahashi",
        "role": "DESIGNER",
        "title": "Principal UI/UX Systems Architect",
        "dept": "Product & Design",
        "icon": "🎨",
        "badge_class": "badge-rose",
        "desk": "Desk 5 (Design Studio)",
        "skills": [
            "Design Tokens",
            "Mobile Wireframes",
            "Zero-Pill UI",
            "WCAG AA Contrast",
            "Figma Specs",
        ],
        "prompt": (
            "You are Sora Takahashi, Principal UI/UX Architect. "
            "You report directly to your Boss. STRICT MANDATE: Deliver "
            "design tokens, wireframe specs, or UI component layouts "
            "directly. Keep text concise. Never discuss trading or finances."
        ),
    },
    {
        "id": "agent-dev",
        "name": "Devon Brooks",
        "role": "DEV",
        "title": "Lead Full-Stack Systems Engineer",
        "dept": "Engineering",
        "icon": "⚡",
        "badge_class": "badge-emerald",
        "desk": "Desk 4 (Engineering Bay)",
        "skills": [
            "TypeScript",
            "Node.js",
            "React / Next.js",
            "Python Engines",
            "API Routing",
            "Bug Fixes",
        ],
        "prompt": (
            "You are Devon Brooks, Lead Full-Stack Engineer. "
            "You report directly to your Boss. STRICT MANDATE: Write "
            "and output complete, runnable code immediately. Keep the "
            "introduction minimal and focus on the implementation."
        ),
    },
    {
        "id": "agent-cto",
        "name": "Elena Rostova",
        "role": "CTO",
        "title": "Chief Technology Officer & System Architect",
        "dept": "Engineering",
        "icon": "🏛️",
        "badge_class": "badge-cyan",
        "desk": "Desk 3 (Architecture Lab)",
        "skills": [
            "Microservices",
            "Database Schemas",
            "Cloud Infrastructure",
            "System Scalability",
            "API Contracts",
        ],
        "prompt": (
            "You are Elena Rostova, CTO & Systems Architect. "
            "You report directly to your Boss. STRICT MANDATE: Deliver "
            "database schemas, API contracts, or architecture plans "
            "directly. Avoid theoretical essays."
        ),
    },
    {
        "id": "agent-social",
        "name": "Chloe",
        "role": "MARKETER",
        "title": "Head of Social Media Operations",
        "dept": "Marketing & Distribution",
        "icon": "📱",
        "badge_class": "badge-purple",
        "desk": "Desk 6 (Social Command)",
        "skills": [
            "YouTube Shorts Hooks",
            "Twitter / X Threads",
            "Instagram Carousels",
            "Viral Marketing",
            "Hashtags",
        ],
        "prompt": (
            "You are Chloe, Head of Social Media. You report directly "
            "to your Boss. STRICT MANDATE: Write ready-to-post copy "
            "for YouTube, Twitter/X, Instagram, and Facebook immediately. "
            "Short and practical."
        ),
    },
    {
        "id": "agent-media",
        "name": "Liam",
        "role": "CONTENT_PRODUCER",
        "title": "Creative Media & Video Strategist",
        "dept": "Marketing & Distribution",
        "icon": "🎬",
        "badge_class": "badge-purple",
        "desk": "Desk 7 (Creative Suite)",
        "skills": [
            "9:16 Vertical Storyboards",
            "YouTube Video Scripts",
            "Retention Pacing",
            "Visual Hooks",
        ],
        "prompt": (
            "You are Liam, Video Strategist. You report directly to "
            "your Boss. STRICT MANDATE: Deliver scene-by-scene scripts, "
            "video hooks, or storyboards directly."
        ),
    },
    {
        "id": "agent-trader",
        "name": "Ray Dalton",
        "role": "TRADER",
        "title": "Forex & Quant Trading Desk Lead",
        "dept": "Trading Desk",
        "icon": "📈",
        "badge_class": "badge-emerald",
        "desk": "Desk 8 (Trading Desk)",
        "skills": [
            "MetaTrader 5 (MT5)",
            "MQL5 Scripts",
            "Forex Technical Analysis",
            "1.0% Hard Equity Stop",
            "EUR/USD & Gold",
        ],
        "prompt": (
            "You are Ray Dalton, Forex Quant Lead. You report directly "
            "to your Boss. STRICT MANDATE: Provide analysis, educational "
            "strategy logic, or demo/paper-trading code. Never claim a "
            "real broker order was executed."
        ),
    },
    {
        "id": "agent-finops",
        "name": "Finley",
        "role": "ACCOUNTANT",
        "title": "Corporate FinOps & Token Cost Auditor",
        "dept": "Finance & Operations",
        "icon": "💰",
        "badge_class": "badge-amber",
        "desk": "Desk 2 (FinOps Bay)",
        "skills": [
            "Treasury Ledger",
            "Token Burn Auditing",
            "20% Reserve Buffer",
            "Invoice Records",
            "Disbursement Sweeps",
        ],
        "prompt": (
            "You are Finley, Corporate FinOps Accountant. You report "
            "directly to your Boss. STRICT MANDATE: Deliver verified "
            "ledger figures, expense records, or bookkeeping structures. "
            "Never invent financial records."
        ),
    },
    {
        "id": "agent-integrations",
        "name": "Kaelen Voss",
        "role": "INTEGRATIONS_SPECIALIST",
        "title": "Lead FinTech & API Integrations Architect",
        "dept": "FinTech & Operations",
        "icon": "⚡",
        "badge_class": "badge-cyan",
        "desk": "Desk 11 (Bridging Bay)",
        "skills": [
            "Webhook Gateways",
            "REST/GraphQL APIs",
            "Stripe & App Store Bridges",
            "Sub-400ms Sockets",
        ],
        "prompt": (
            "You are Kaelen Voss, FinTech & API Architect. "
            "You report directly to your Boss. STRICT MANDATE: Deliver "
            "webhook schemas, API endpoint specs, or integration code "
            "directly and concisely."
        ),
    },
    {
        "id": "agent-webops",
        "name": "Atlas",
        "role": "WEB_OPERATOR",
        "title": "Autonomous Web & Browser Operator",
        "dept": "Operations",
        "icon": "🌐",
        "badge_class": "badge-blue",
        "desk": "Desk 9 (Operations Hub)",
        "skills": [
            "Headless Browser Automation",
            "Playwright / Puppeteer",
            "Web Scraping",
            "DOM Audits",
            "Uptime Monitoring",
        ],
        "prompt": (
            "You are Atlas, Autonomous Web Operator. You report "
            "directly to your Boss. STRICT MANDATE: Deliver browser "
            "automation, Playwright/Puppeteer scripts, or web-operation "
            "plans directly."
        ),
    },
    {
        "id": "agent-qa",
        "name": "Tariq Al-Mansoor",
        "role": "QA",
        "title": "Security & Deterministic QA Lead",
        "dept": "Operations",
        "icon": "🛡️",
        "badge_class": "badge-blue",
        "desk": "Desk 10 (Security Bunker)",
        "skills": [
            "Security Penetration Audits",
            "Unit / Integration Tests",
            "API Fuzzing",
            "HMAC Verification",
            "Zero Memory Leaks",
        ],
        "prompt": (
            "You are Tariq Al-Mansoor, QA & Security Lead. You report "
            "directly to your Boss. STRICT MANDATE: Provide test suites, "
            "security audit matrices, and honest pass/fail findings."
        ),
    },
]


# ==============================================================================
# ROBUST STATE INITIALIZATION
# ==============================================================================

MEMORY_FILE = "autooffice_memory.json"


def get_default_state():
    return {
        "ceo_chat": [],
        "worker_chats": {},
        "team_chats": {},
        "treasury": {
            "balance": 0.0,
            "reserve": 0.0,
            "income": 0.0,
            "expenses": 0.0,
            "payouts": 0.0,
        },
        "tasks": [],
        "approvals": [],
        "paper_positions": [],
        "trade_history": [],
        "webhooks": [],
        "memory": [],
        "selected_worker": "Marcus Vance",
        "selected_team": "Engineering",
        "selected_url": "https://example.com",
    }


def init_state():
    defaults = get_default_state()

    for key, default_value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = default_value

    if not isinstance(st.session_state.get("worker_chats"), dict):
        st.session_state.worker_chats = {}

    if not isinstance(st.session_state.get("team_chats"), dict):
        st.session_state.team_chats = {}

    if not isinstance(st.session_state.get("tasks"), list):
        st.session_state.tasks = []

    if not isinstance(st.session_state.get("approvals"), list):
        st.session_state.approvals = []

    if not isinstance(st.session_state.get("paper_positions"), list):
        st.session_state.paper_positions = []

    if not isinstance(st.session_state.get("trade_history"), list):
        st.session_state.trade_history = []

    if not isinstance(st.session_state.get("webhooks"), list):
        st.session_state.webhooks = []

    if not isinstance(st.session_state.get("memory"), list):
        st.session_state.memory = []

# ==============================================================================
# PERSISTENT MEMORY + FILE / WEB UTILITIES
# ==============================================================================

def save_persistent_memory(data):
    try:
        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump(
                data,
                f,
                indent=2,
                ensure_ascii=False,
                default=str,
            )
    except Exception:
        # Persistence failure must never crash the Streamlit app.
        pass


def read_real_app_file(num_lines=150):
    try:
        if os.path.exists("app.py"):
            with open("app.py", "r", encoding="utf-8") as f:
                content = f.read()

            lines = content.splitlines()
            shown = min(num_lines, len(lines))
            snippet = "\n".join(lines[:shown])

            return (
                f"// REAL SOURCE CODE FROM DISK "
                f"(app.py - showing first {shown} of {len(lines)} lines):\n\n"
                f"{snippet}"
            )

    except Exception as exc:
        return f"// Error reading app.py: {exc}"

    return "// app.py file not found on disk."


def fetch_live_web_url(url):
    """
    Fetch a public webpage for basic connectivity/title inspection.

    This does NOT pretend to perform browser clicks, logins, purchases,
    or other actions. It only performs an HTTP GET.
    """
    if not url:
        return "No URL provided."

    target_url = (
        url.strip()
        if str(url).strip().startswith(("http://", "https://"))
        else f"https://{str(url).strip()}"
    )

    try:
        ctx = ssl.create_default_context()

        request = urllib.request.Request(
            target_url,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 "
                    "(KHTML, like Gecko) "
                    "Chrome/120.0.0.0 Safari/537.36"
                )
            },
        )

        with urllib.request.urlopen(
            request,
            timeout=8,
            context=ctx,
        ) as response:
            html = response.read().decode(
                "utf-8",
                errors="ignore",
            )

            title_match = re.search(
                r"<title[^>]*>(.*?)</title>",
                html,
                re.IGNORECASE | re.DOTALL,
            )

            page_title = (
                re.sub(r"\s+", " ", title_match.group(1)).strip()
                if title_match
                else "Live Webpage"
            )

            return (
                f"✓ Atlas Web Inspector connected.\n"
                f"URL: {target_url}\n"
                f"Page title: {page_title}\n"
                f"HTTP status: {getattr(response, 'status', 'unknown')}\n"
                f"Content size: {len(html):,} bytes"
            )

    except Exception as exc:
        return (
            f"⚠️ Could not fetch {target_url}\n"
            f"Reason: {exc}"
        )


def render_copy_button(text_to_copy, button_key):
    """
    Small browser-side copy button.

    The button is cosmetic only; failure to copy must not crash the app.
    """
    safe_key = re.sub(r"[^a-zA-Z0-9_-]", "_", str(button_key))
    clean_text = json.dumps(str(text_to_copy))

    html_code = f"""
    <div style="margin-top:2px;margin-bottom:6px;">
        <button
            id="btn_{safe_key}"
            onclick='
                navigator.clipboard.writeText({clean_text})
                .then(function() {{
                    var btn = document.getElementById("btn_{safe_key}");
                    if (btn) {{
                        btn.innerHTML = "✓ Copied!";
                        setTimeout(function() {{
                            btn.innerHTML = "📋 Copy Message";
                        }}, 1800);
                    }}
                }})
                .catch(function(err) {{
                    console.error("Copy error:", err);
                }});
            '
            style="
                background:rgba(255,255,255,0.08);
                color:#94a3b8;
                border:1px solid rgba(255,255,255,0.2);
                border-radius:6px;
                padding:3px 9px;
                font-size:11px;
                cursor:pointer;
                font-weight:600;
                font-family:sans-serif;
            "
        >
            📋 Copy Message
        </button>
    </div>
    """

    st.components.v1.html(
        html_code,
        height=34,
    )


# ==============================================================================
# TASK RECORDING
# ==============================================================================

def record_auto_task(
    agent_name,
    dept_name,
    task_title,
    deliverable_text="",
):
    """
    Record an office task.

    IMPORTANT:
    Recording a task is not the same thing as actually executing it.
    The status therefore remains 'recorded' unless a real tool/result
    confirms completion.
    """
    office = st.session_state.office_data
    tasks = office.setdefault("tasks", [])

    task_id = f"TASK-{len(tasks) + 101}"
    now_str = datetime.now().strftime("%H:%M:%S")

    exec_logs = [
        (
            f"[{now_str}] 👔 Marcus Vance: "
            f"Objective received: \"{str(task_title)[:60]}\"."
        ),
        (
            f"[{now_str}] ⚡ {agent_name} ({dept_name}): "
            "Task assigned and deliverable workspace prepared."
        ),
        (
            f"[{now_str}] 🛡️ Tariq Al-Mansoor: "
            "Validation is pending until evidence is available."
        ),
        (
            f"[{now_str}] 💰 Finley: "
            "Task recorded in the office ledger; no financial execution implied."
        ),
    ]

    if not deliverable_text:
        lower_title = str(task_title).lower()

        if any(
            word in lower_title
            for word in (
                "web",
                "site",
                "url",
                "click",
                "fill",
                "form",
            )
        ):
            deliverable_text = f"""# Atlas Web Automation Draft

Objective:
{task_title}

Suggested implementation:

from playwright.sync_api import sync_playwright

def run_web_workflow():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()

        # Replace with the actual authorized target URL.
        page.goto("https://example.com", wait_until="domcontentloaded")

        print("Page loaded:", page.title())

        browser.close()


if __name__ == "__main__":
    run_web_workflow()
"""

        elif any(
            word in lower_title
            for word in (
                "clipboard",
                "copy",
                "chat",
                "code",
            )
        ):
            deliverable_text = """// Clipboard utility draft

export async function copyChatToClipboard(
  text: string
): Promise<boolean> {
  try {
    if (
      navigator.clipboard &&
      window.isSecureContext
    ) {
      await navigator.clipboard.writeText(text);
      return true;
    }

    const textArea = document.createElement("textarea");
    textArea.value = text;
    textArea.style.position = "fixed";
    textArea.style.opacity = "0";

    document.body.appendChild(textArea);
    textArea.select();

    document.execCommand("copy");
    document.body.removeChild(textArea);

    return true;
  } catch (error) {
    console.error("Clipboard copy failed:", error);
    return false;
  }
}
"""

        else:
            deliverable_text = (
                f"Task workspace prepared for: **{task_title}**\n\n"
                f"Assigned specialist: **{agent_name}**\n"
                "Execution status: **Not independently verified**."
            )

    new_task = {
        "id": task_id,
        "title": str(task_title)[:120],
        "agent": agent_name,
        "dept": dept_name,
        "status": "recorded",
        "progress": 0,
        "priority": "normal",
        "deliverable": deliverable_text,
        "exec_logs": exec_logs,
        "timestamp": now_str,
    }

    tasks.insert(0, new_task)
    office["tasks"] = tasks

    save_persistent_memory(office)

    return new_task


# ==============================================================================
# GEMINI API HELPER
# ==============================================================================

def get_gemini_api_key():
    """
    Resolve the Gemini API key without exposing it in the interface.
    """
    try:
        secret_key = st.secrets.get(
            "GEMINI_API_KEY",
            "",
        )
    except Exception:
        secret_key = ""

    return (
        os.environ.get("GEMINI_API_KEY", "").strip()
        or str(secret_key).strip()
        or str(
            st.session_state.get(
                "custom_api_key",
                "",
            )
        ).strip()
    )


def _extract_gemini_text(data):
    """
    Safely extract text from Gemini's REST response.
    """
    output = []

    for candidate in data.get("candidates", []) or []:
        content = candidate.get(
            "content",
            {},
        ) or {}

        for part in content.get(
            "parts",
            [],
        ) or []:
            if isinstance(part, dict):
                text_value = part.get("text")

                if text_value:
                    output.append(str(text_value))

    return "\n".join(output).strip() or None


def query_gemini_api(
    system_prompt,
    user_text,
    history_messages=None,
    temperature=0.25,
):
    """
    Gemini REST client.

    The function fails gracefully instead of crashing Streamlit.
    """
    api_key = get_gemini_api_key()

    if not api_key:
        return None

    history_messages = history_messages or []

    preferred_model = os.environ.get(
        "GEMINI_MODEL",
        "gemini-3.6-flash",
    ).strip()

    models = []

    for model_name in (
        preferred_model,
        "gemini-3.6-flash",
        "gemini-2.0-flash",
        "gemini-1.5-flash",
    ):
        if model_name and model_name not in models:
            models.append(model_name)

    contents = []

    for message in history_messages[-10:]:
        if not isinstance(message, dict):
            continue

        role = (
            "user"
            if message.get("sender") == "user"
            else "model"
        )

        text_value = str(
            message.get("text", "")
        ).strip()

        if text_value:
            contents.append(
                {
                    "role": role,
                    "parts": [
                        {
                            "text": text_value[:12000]
                        }
                    ],
                }
            )

    contents.append(
        {
            "role": "user",
            "parts": [
                {
                    "text": str(user_text)[:20000]
                }
            ],
        }
    )

    payload = {
        "contents": contents,
        "systemInstruction": {
            "parts": [
                {
                    "text": str(system_prompt)
                }
            ]
        },
        "generationConfig": {
            "temperature": float(temperature),
            "topP": 0.9,
            "maxOutputTokens": 4096,
        },
    }

    for model_name in models:
        try:
            endpoint = (
                "https://generativelanguage.googleapis.com/"
                f"v1beta/models/{model_name}:generateContent"
                f"?key={api_key}"
            )

            request = urllib.request.Request(
                endpoint,
                data=json.dumps(
                    payload
                ).encode("utf-8"),
                headers={
                    "Content-Type": "application/json"
                },
                method="POST",
            )

            with urllib.request.urlopen(
                request,
                timeout=25,
            ) as response:
                raw = response.read().decode(
                    "utf-8",
                    errors="ignore",
                )

                data = json.loads(raw)
                answer = _extract_gemini_text(data)

                if answer:
                    return answer

        except Exception:
            # Try the next supported model instead of crashing the app.
            continue

    return None


# ==============================================================================
# AUTO-OFFICE INTELLIGENCE LAYER
# ==============================================================================

BRAIN_VERSION = "2.1"

ROLE_INTELLIGENCE = {
    "agent-ceo": (
        "strategy, prioritization, delegation, product decisions, "
        "concise executive communication"
    ),
    "agent-designer": (
        "UI/UX, interaction design, design systems, accessibility, "
        "user flows"
    ),
    "agent-dev": (
        "Python, TypeScript, React, APIs, debugging, implementation"
    ),
    "agent-cto": (
        "architecture, databases, infrastructure, scalability, "
        "technical tradeoffs"
    ),
    "agent-social": (
        "social content, hooks, campaigns, platform-specific copy, "
        "distribution"
    ),
    "agent-media": (
        "video concepts, scripts, storyboards, pacing, retention"
    ),
    "agent-trader": (
        "market education, paper/demo trading analysis, "
        "MQL5 simulation and code review"
    ),
    "agent-finops": (
        "bookkeeping, budgets, cost analysis, ledgers, "
        "financial data organization"
    ),
    "agent-integrations": (
        "REST/GraphQL APIs, webhooks, authentication flows, "
        "service integration"
    ),
    "agent-webops": (
        "browser automation, Playwright, scraping, DOM inspection, "
        "web workflows"
    ),
    "agent-qa": (
        "testing, security review, failure analysis, validation, "
        "regression checks"
    ),
}


def _find_staff(staff_id):
    return next(
        (
            staff
            for staff in STAFF_MEMBERS
            if staff["id"] == staff_id
        ),
        STAFF_MEMBERS[0],
    )


def _route_staff(
    user_text,
    current_staff_id="agent-ceo",
):
    """
    Route obvious specialist requests to the appropriate worker.
    CEO remains the default coordinator.
    """
    text_value = str(user_text).lower()

    routes = [
        (
            "agent-dev",
            [
                "python",
                "javascript",
                "typescript",
                "react",
                "bug",
                "code",
                "coding",
                "app.py",
                "streamlit",
            ],
        ),
        (
            "agent-cto",
            [
                "architecture",
                "database",
                "schema",
                "scalability",
                "system design",
                "infrastructure",
            ],
        ),
        (
            "agent-designer",
            [
                "ui",
                "ux",
                "design",
                "wireframe",
                "layout",
                "figma",
                "interface",
            ],
        ),
        (
            "agent-social",
            [
                "youtube",
                "instagram",
                "facebook",
                "twitter",
                "linkedin",
                "post",
                "caption",
                "hashtag",
            ],
        ),
        (
            "agent-media",
            [
                "video",
                "reel",
                "shorts",
                "storyboard",
                "script",
                "editing",
            ],
        ),
        (
            "agent-webops",
            [
                "website",
                "browser",
                "playwright",
                "scrape",
                "scraping",
                "click",
                "form",
                "web page",
                "url",
            ],
        ),
        (
            "agent-qa",
            [
                "test",
                "testing",
                "security",
                "audit",
                "bug report",
                "verify",
                "validation",
            ],
        ),
        (
            "agent-integrations",
            [
                "api",
                "webhook",
                "stripe",
                "integration",
                "endpoint",
                "oauth",
            ],
        ),
        (
            "agent-finops",
            [
                "budget",
                "invoice",
                "expense",
                "ledger",
                "cost",
                "revenue",
                "finance",
            ],
        ),
        (
            "agent-trader",
            [
                "forex",
                "xau",
                "gold",
                "eur/usd",
                "mt5",
                "mql5",
                "trading",
                "trade",
            ],
        ),
    ]

    for staff_id, keywords in routes:
        if any(
            keyword in text_value
            for keyword in keywords
        ):
            return staff_id

    return current_staff_id or "agent-ceo"


def _memory_context(max_items=8):
    """
    Return a compact memory summary.
    Never send secrets or giant transcripts to Gemini.
    """
    office = st.session_state.get(
        "office_data",
        {},
    )

    tasks = office.get(
        "tasks",
        [],
    )[-max_items:]

    compact = []

    for task in tasks:
        compact.append(
            {
                "title": str(
                    task.get(
                        "title",
                        "",
                    )
                )[:160],
                "agent": task.get(
                    "agent",
                    "",
                ),
                "status": task.get(
                    "status",
                    "",
                ),
            }
        )

    return compact


def _brain_system(
    staff,
    user_text,
    mode="direct",
    delegation="",
):
    expertise = ROLE_INTELLIGENCE.get(
        staff["id"],
        ", ".join(
            staff.get(
                "skills",
                [],
            )
        ),
    )

    return f"""
You are {staff['name']}, {staff['title']} in AutoOffice OS.

Your domain:
{expertise}

You are an AI worker inside a real software office.
Do not role-play unnecessarily.

USER REQUEST:
{user_text}

MODE:
{mode}

{delegation}

OPERATING RULES:

1. Answer the user's actual request first.

2. Simple questions get simple answers.
   Do not announce meetings, teams, delegations, or workflows
   for a one-line question.

3. Never invent information, files, test results, web results,
   deployments, approvals, trades, payments, or completed actions.

4. If information is missing, clearly say what is missing.

5. For coding requests, provide complete runnable code when
   appropriate.

6. For complex work, use:
   Goal -> Plan -> Deliverable -> Checks.

7. Only mention another worker when that worker materially
   contributes to the requested task.

8. Never use fake status language such as:
   "100% verified",
   "deployed",
   "executed",
   "live",
   unless the application has actual evidence.

9. Trading-related requests are educational/demo/paper-analysis
   only. Never claim to place or execute real-money trades.

10. Keep the final answer concise and useful.
"""


def office_brain(
    user_text,
    current_staff_id="agent-ceo",
    history_messages=None,
    mode="auto",
):
    """
    Main AutoOffice intelligence router.
    """
    history_messages = history_messages or []

    chosen_id = _route_staff(
        user_text,
        current_staff_id,
    )

    chosen = _find_staff(chosen_id)
    text_value = str(user_text).strip()

    simple_patterns = [
        r"^what(?:'s| is) the time\b",
        r"^what day is it\b",
        r"^hello\b",
        r"^hi\b",
        r"^hey\b",
        r"^who are you\b",
        r"^thanks\b",
        r"^thank you\b",
        r"^what can you do\b",
    ]

    is_simple = any(
        re.search(
            pattern,
            text_value.lower(),
        )
        for pattern in simple_patterns
    )

    if mode == "direct" or is_simple:
        system = _brain_system(
            chosen,
            text_value,
            mode="direct",
        )

        return (
            query_gemini_api(
                system,
                text_value,
                history_messages,
                temperature=0.2,
            )
            or _intelligent_fallback(
                chosen,
                text_value,
            )
        )

    complex_signals = [
        "build",
        "create",
        "develop",
        "implement",
        "design",
        "analyze",
        "research",
        "plan",
        "fix",
        "debug",
        "automate",
        "compare",
        "project",
        "system",
        "app",
        "code",
    ]

    is_complex = (
        len(text_value) > 140
        or sum(
            1
            for signal in complex_signals
            if signal in text_value.lower()
        ) >= 2
    )

    memory = _memory_context()

    if not is_complex:
        system = _brain_system(
            chosen,
            text_value,
            mode="direct",
        )

        return (
            query_gemini_api(
                system,
                text_value,
                history_messages,
                temperature=0.25,
            )
            or _intelligent_fallback(
                chosen,
                text_value,
            )
        )

    delegation = f"""
For this complex request, {chosen['name']} is the primary specialist.

A supporting specialist may be useful if the task genuinely requires it.

Recent operational memory:
{json.dumps(memory, ensure_ascii=False)}

Do the reasoning internally.
Return only the useful plan, answer, or deliverable.
Do not reveal private chain-of-thought.
"""

    system = _brain_system(
        chosen,
        text_value,
        mode="complex",
        delegation=delegation,
    )

    result = query_gemini_api(
        system,
        text_value,
        history_messages,
        temperature=0.3,
    )

    if result:
        return result

    return _intelligent_fallback(
        chosen,
        text_value,
    )


def _intelligent_fallback(
    staff,
    user_text,
):
    """
    Honest fallback when Gemini is unavailable.
    """
    return (
        f"**{staff['name']} — {staff['role']}**\n\n"
        f"I can handle: "
        f"{', '.join(staff.get('skills', [])[:5])}.\n\n"
        f"Request received: **{str(user_text)[:300]}**\n\n"
        "Gemini is not available right now, so I won't pretend "
        "this task was executed. Check GEMINI_API_KEY and "
        "GEMINI_MODEL, then retry."
    )
init_state()
# ==============================================================================
# PERSISTENT MEMORY + FILE / WEB UTILITIES
# ==============================================================================

def save_persistent_memory(data):
    try:
        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump(
                data,
                f,
                indent=2,
                ensure_ascii=False,
                default=str,
            )
    except Exception:
        # Persistence failure must never crash the Streamlit app.
        pass


def read_real_app_file(num_lines=150):
    try:
        if os.path.exists("app.py"):
            with open("app.py", "r", encoding="utf-8") as f:
                content = f.read()

            lines = content.splitlines()
            shown = min(num_lines, len(lines))
            snippet = "\n".join(lines[:shown])

            return (
                f"// REAL SOURCE CODE FROM DISK "
                f"(app.py - showing first {shown} of {len(lines)} lines):\n\n"
                f"{snippet}"
            )

    except Exception as exc:
        return f"// Error reading app.py: {exc}"

    return "// app.py file not found on disk."


def fetch_live_web_url(url):
    """
    Fetch a public webpage for basic connectivity/title inspection.

    This does NOT pretend to perform browser clicks, logins, purchases,
    or other actions. It only performs an HTTP GET.
    """
    if not url:
        return "No URL provided."

    target_url = (
        url.strip()
        if str(url).strip().startswith(("http://", "https://"))
        else f"https://{str(url).strip()}"
    )

    try:
        ctx = ssl.create_default_context()

        request = urllib.request.Request(
            target_url,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 "
                    "(KHTML, like Gecko) "
                    "Chrome/120.0.0.0 Safari/537.36"
                )
            },
        )

        with urllib.request.urlopen(
            request,
            timeout=8,
            context=ctx,
        ) as response:
            html = response.read().decode(
                "utf-8",
                errors="ignore",
            )

            title_match = re.search(
                r"<title[^>]*>(.*?)</title>",
                html,
                re.IGNORECASE | re.DOTALL,
            )

            page_title = (
                re.sub(r"\s+", " ", title_match.group(1)).strip()
                if title_match
                else "Live Webpage"
            )

            return (
                f"✓ Atlas Web Inspector connected.\n"
                f"URL: {target_url}\n"
                f"Page title: {page_title}\n"
                f"HTTP status: {getattr(response, 'status', 'unknown')}\n"
                f"Content size: {len(html):,} bytes"
            )

    except Exception as exc:
        return (
            f"⚠️ Could not fetch {target_url}\n"
            f"Reason: {exc}"
        )


def render_copy_button(text_to_copy, button_key):
    """
    Small browser-side copy button.

    The button is cosmetic only; failure to copy must not crash the app.
    """
    safe_key = re.sub(r"[^a-zA-Z0-9_-]", "_", str(button_key))
    clean_text = json.dumps(str(text_to_copy))

    html_code = f"""
    <div style="margin-top:2px;margin-bottom:6px;">
        <button
            id="btn_{safe_key}"
            onclick='
                navigator.clipboard.writeText({clean_text})
                .then(function() {{
                    var btn = document.getElementById("btn_{safe_key}");
                    if (btn) {{
                        btn.innerHTML = "✓ Copied!";
                        setTimeout(function() {{
                            btn.innerHTML = "📋 Copy Message";
                        }}, 1800);
                    }}
                }})
                .catch(function(err) {{
                    console.error("Copy error:", err);
                }});
            '
            style="
                background:rgba(255,255,255,0.08);
                color:#94a3b8;
                border:1px solid rgba(255,255,255,0.2);
                border-radius:6px;
                padding:3px 9px;
                font-size:11px;
                cursor:pointer;
                font-weight:600;
                font-family:sans-serif;
            "
        >
            📋 Copy Message
        </button>
    </div>
    """

    st.components.v1.html(
        html_code,
        height=34,
    )


# ==============================================================================
# TASK RECORDING
# ==============================================================================

def record_auto_task(
    agent_name,
    dept_name,
    task_title,
    deliverable_text="",
):
    """
    Record an office task.

    IMPORTANT:
    Recording a task is not the same thing as actually executing it.
    The status therefore remains 'recorded' unless a real tool/result
    confirms completion.
    """
    office = st.session_state.office_data
    tasks = office.setdefault("tasks", [])

    task_id = f"TASK-{len(tasks) + 101}"
    now_str = datetime.now().strftime("%H:%M:%S")

    exec_logs = [
        (
            f"[{now_str}] 👔 Marcus Vance: "
            f"Objective received: \"{str(task_title)[:60]}\"."
        ),
        (
            f"[{now_str}] ⚡ {agent_name} ({dept_name}): "
            "Task assigned and deliverable workspace prepared."
        ),
        (
            f"[{now_str}] 🛡️ Tariq Al-Mansoor: "
            "Validation is pending until evidence is available."
        ),
        (
            f"[{now_str}] 💰 Finley: "
            "Task recorded in the office ledger; no financial execution implied."
        ),
    ]

    if not deliverable_text:
        lower_title = str(task_title).lower()

        if any(
            word in lower_title
            for word in (
                "web",
                "site",
                "url",
                "click",
                "fill",
                "form",
            )
        ):
            deliverable_text = f"""# Atlas Web Automation Draft

Objective:
{task_title}

Suggested implementation:

from playwright.sync_api import sync_playwright

def run_web_workflow():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()

        # Replace with the actual authorized target URL.
        page.goto("https://example.com", wait_until="domcontentloaded")

        print("Page loaded:", page.title())

        browser.close()


if __name__ == "__main__":
    run_web_workflow()
"""

        elif any(
            word in lower_title
            for word in (
                "clipboard",
                "copy",
                "chat",
                "code",
            )
        ):
            deliverable_text = """// Clipboard utility draft

export async function copyChatToClipboard(
  text: string
): Promise<boolean> {
  try {
    if (
      navigator.clipboard &&
      window.isSecureContext
    ) {
      await navigator.clipboard.writeText(text);
      return true;
    }

    const textArea = document.createElement("textarea");
    textArea.value = text;
    textArea.style.position = "fixed";
    textArea.style.opacity = "0";

    document.body.appendChild(textArea);
    textArea.select();

    document.execCommand("copy");
    document.body.removeChild(textArea);

    return true;
  } catch (error) {
    console.error("Clipboard copy failed:", error);
    return false;
  }
}
"""

        else:
            deliverable_text = (
                f"Task workspace prepared for: **{task_title}**\n\n"
                f"Assigned specialist: **{agent_name}**\n"
                "Execution status: **Not independently verified**."
            )

    new_task = {
        "id": task_id,
        "title": str(task_title)[:120],
        "agent": agent_name,
        "dept": dept_name,
        "status": "recorded",
        "progress": 0,
        "priority": "normal",
        "deliverable": deliverable_text,
        "exec_logs": exec_logs,
        "timestamp": now_str,
    }

    tasks.insert(0, new_task)
    office["tasks"] = tasks

    save_persistent_memory(office)

    return new_task


# ==============================================================================
# GEMINI API HELPER
# ==============================================================================

def get_gemini_api_key():
    """
    Resolve the Gemini API key without exposing it in the interface.
    """
    try:
        secret_key = st.secrets.get(
            "GEMINI_API_KEY",
            "",
        )
    except Exception:
        secret_key = ""

    return (
        os.environ.get("GEMINI_API_KEY", "").strip()
        or str(secret_key).strip()
        or str(
            st.session_state.get(
                "custom_api_key",
                "",
            )
        ).strip()
    )


def _extract_gemini_text(data):
    """
    Safely extract text from Gemini's REST response.
    """
    output = []

    for candidate in data.get("candidates", []) or []:
        content = candidate.get(
            "content",
            {},
        ) or {}

        for part in content.get(
            "parts",
            [],
        ) or []:
            if isinstance(part, dict):
                text_value = part.get("text")

                if text_value:
                    output.append(str(text_value))

    return "\n".join(output).strip() or None


def query_gemini_api(
    system_prompt,
    user_text,
    history_messages=None,
    temperature=0.25,
):
    """
    Gemini REST client.

    The function fails gracefully instead of crashing Streamlit.
    """
    api_key = get_gemini_api_key()

    if not api_key:
        return None

    history_messages = history_messages or []

    preferred_model = os.environ.get(
        "GEMINI_MODEL",
        "gemini-3.6-flash",
    ).strip()

    models = []

    for model_name in (
        preferred_model,
        "gemini-3.6-flash",
        "gemini-2.0-flash",
        "gemini-1.5-flash",
    ):
        if model_name and model_name not in models:
            models.append(model_name)

    contents = []

    for message in history_messages[-10:]:
        if not isinstance(message, dict):
            continue

        role = (
            "user"
            if message.get("sender") == "user"
            else "model"
        )

        text_value = str(
            message.get("text", "")
        ).strip()

        if text_value:
            contents.append(
                {
                    "role": role,
                    "parts": [
                        {
                            "text": text_value[:12000]
                        }
                    ],
                }
            )

    contents.append(
        {
            "role": "user",
            "parts": [
                {
                    "text": str(user_text)[:20000]
                }
            ],
        }
    )

    payload = {
        "contents": contents,
        "systemInstruction": {
            "parts": [
                {
                    "text": str(system_prompt)
                }
            ]
        },
        "generationConfig": {
            "temperature": float(temperature),
            "topP": 0.9,
            "maxOutputTokens": 4096,
        },
    }

    for model_name in models:
        try:
            endpoint = (
                "https://generativelanguage.googleapis.com/"
                f"v1beta/models/{model_name}:generateContent"
                f"?key={api_key}"
            )

            request = urllib.request.Request(
                endpoint,
                data=json.dumps(
                    payload
                ).encode("utf-8"),
                headers={
                    "Content-Type": "application/json"
                },
                method="POST",
            )

            with urllib.request.urlopen(
                request,
                timeout=25,
            ) as response:
                raw = response.read().decode(
                    "utf-8",
                    errors="ignore",
                )

                data = json.loads(raw)
                answer = _extract_gemini_text(data)

                if answer:
                    return answer

        except Exception:
            # Try the next supported model instead of crashing the app.
            continue

    return None


# ==============================================================================
# AUTO-OFFICE INTELLIGENCE LAYER
# ==============================================================================

BRAIN_VERSION = "2.1"

ROLE_INTELLIGENCE = {
    "agent-ceo": (
        "strategy, prioritization, delegation, product decisions, "
        "concise executive communication"
    ),
    "agent-designer": (
        "UI/UX, interaction design, design systems, accessibility, "
        "user flows"
    ),
    "agent-dev": (
        "Python, TypeScript, React, APIs, debugging, implementation"
    ),
    "agent-cto": (
        "architecture, databases, infrastructure, scalability, "
        "technical tradeoffs"
    ),
    "agent-social": (
        "social content, hooks, campaigns, platform-specific copy, "
        "distribution"
    ),
    "agent-media": (
        "video concepts, scripts, storyboards, pacing, retention"
    ),
    "agent-trader": (
        "market education, paper/demo trading analysis, "
        "MQL5 simulation and code review"
    ),
    "agent-finops": (
        "bookkeeping, budgets, cost analysis, ledgers, "
        "financial data organization"
    ),
    "agent-integrations": (
        "REST/GraphQL APIs, webhooks, authentication flows, "
        "service integration"
    ),
    "agent-webops": (
        "browser automation, Playwright, scraping, DOM inspection, "
        "web workflows"
    ),
    "agent-qa": (
        "testing, security review, failure analysis, validation, "
        "regression checks"
    ),
}


def _find_staff(staff_id):
    return next(
        (
            staff
            for staff in STAFF_MEMBERS
            if staff["id"] == staff_id
        ),
        STAFF_MEMBERS[0],
    )


def _route_staff(
    user_text,
    current_staff_id="agent-ceo",
):
    """
    Route obvious specialist requests to the appropriate worker.
    CEO remains the default coordinator.
    """
    text_value = str(user_text).lower()

    routes = [
        (
            "agent-dev",
            [
                "python",
                "javascript",
                "typescript",
                "react",
                "bug",
                "code",
                "coding",
                "app.py",
                "streamlit",
            ],
        ),
        (
            "agent-cto",
            [
                "architecture",
                "database",
                "schema",
                "scalability",
                "system design",
                "infrastructure",
            ],
        ),
        (
            "agent-designer",
            [
                "ui",
                "ux",
                "design",
                "wireframe",
                "layout",
                "figma",
                "interface",
            ],
        ),
        (
            "agent-social",
            [
                "youtube",
                "instagram",
                "facebook",
                "twitter",
                "linkedin",
                "post",
                "caption",
                "hashtag",
            ],
        ),
        (
            "agent-media",
            [
                "video",
                "reel",
                "shorts",
                "storyboard",
                "script",
                "editing",
            ],
        ),
        (
            "agent-webops",
            [
                "website",
                "browser",
                "playwright",
                "scrape",
                "scraping",
                "click",
                "form",
                "web page",
                "url",
            ],
        ),
        (
            "agent-qa",
            [
                "test",
                "testing",
                "security",
                "audit",
                "bug report",
                "verify",
                "validation",
            ],
        ),
        (
            "agent-integrations",
            [
                "api",
                "webhook",
                "stripe",
                "integration",
                "endpoint",
                "oauth",
            ],
        ),
        (
            "agent-finops",
            [
                "budget",
                "invoice",
                "expense",
                "ledger",
                "cost",
                "revenue",
                "finance",
            ],
        ),
        (
            "agent-trader",
            [
                "forex",
                "xau",
                "gold",
                "eur/usd",
                "mt5",
                "mql5",
                "trading",
                "trade",
            ],
        ),
    ]

    for staff_id, keywords in routes:
        if any(
            keyword in text_value
            for keyword in keywords
        ):
            return staff_id

    return current_staff_id or "agent-ceo"


def _memory_context(max_items=8):
    """
    Return a compact memory summary.
    Never send secrets or giant transcripts to Gemini.
    """
    office = st.session_state.get(
        "office_data",
        {},
    )

    tasks = office.get(
        "tasks",
        [],
    )[-max_items:]

    compact = []

    for task in tasks:
        compact.append(
            {
                "title": str(
                    task.get(
                        "title",
                        "",
                    )
                )[:160],
                "agent": task.get(
                    "agent",
                    "",
                ),
                "status": task.get(
                    "status",
                    "",
                ),
            }
        )

    return compact


def _brain_system(
    staff,
    user_text,
    mode="direct",
    delegation="",
):
    expertise = ROLE_INTELLIGENCE.get(
        staff["id"],
        ", ".join(
            staff.get(
                "skills",
                [],
            )
        ),
    )

    return f"""
You are {staff['name']}, {staff['title']} in AutoOffice OS.

Your domain:
{expertise}

You are an AI worker inside a real software office.
Do not role-play unnecessarily.

USER REQUEST:
{user_text}

MODE:
{mode}

{delegation}

OPERATING RULES:

1. Answer the user's actual request first.

2. Simple questions get simple answers.
   Do not announce meetings, teams, delegations, or workflows
   for a one-line question.

3. Never invent information, files, test results, web results,
   deployments, approvals, trades, payments, or completed actions.

4. If information is missing, clearly say what is missing.

5. For coding requests, provide complete runnable code when
   appropriate.

6. For complex work, use:
   Goal -> Plan -> Deliverable -> Checks.

7. Only mention another worker when that worker materially
   contributes to the requested task.

8. Never use fake status language such as:
   "100% verified",
   "deployed",
   "executed",
   "live",
   unless the application has actual evidence.

9. Trading-related requests are educational/demo/paper-analysis
   only. Never claim to place or execute real-money trades.

10. Keep the final answer concise and useful.
"""


def office_brain(
    user_text,
    current_staff_id="agent-ceo",
    history_messages=None,
    mode="auto",
):
    """
    Main AutoOffice intelligence router.
    """
    history_messages = history_messages or []

    chosen_id = _route_staff(
        user_text,
        current_staff_id,
    )

    chosen = _find_staff(chosen_id)
    text_value = str(user_text).strip()

    simple_patterns = [
        r"^what(?:'s| is) the time\b",
        r"^what day is it\b",
        r"^hello\b",
        r"^hi\b",
        r"^hey\b",
        r"^who are you\b",
        r"^thanks\b",
        r"^thank you\b",
        r"^what can you do\b",
    ]

    is_simple = any(
        re.search(
            pattern,
            text_value.lower(),
        )
        for pattern in simple_patterns
    )

    if mode == "direct" or is_simple:
        system = _brain_system(
            chosen,
            text_value,
            mode="direct",
        )

        return (
            query_gemini_api(
                system,
                text_value,
                history_messages,
                temperature=0.2,
            )
            or _intelligent_fallback(
                chosen,
                text_value,
            )
        )

    complex_signals = [
        "build",
        "create",
        "develop",
        "implement",
        "design",
        "analyze",
        "research",
        "plan",
        "fix",
        "debug",
        "automate",
        "compare",
        "project",
        "system",
        "app",
        "code",
    ]

    is_complex = (
        len(text_value) > 140
        or sum(
            1
            for signal in complex_signals
            if signal in text_value.lower()
        ) >= 2
    )

    memory = _memory_context()

    if not is_complex:
        system = _brain_system(
            chosen,
            text_value,
            mode="direct",
        )

        return (
            query_gemini_api(
                system,
                text_value,
                history_messages,
                temperature=0.25,
            )
            or _intelligent_fallback(
                chosen,
                text_value,
            )
        )

    delegation = f"""
For this complex request, {chosen['name']} is the primary specialist.

A supporting specialist may be useful if the task genuinely requires it.

Recent operational memory:
{json.dumps(memory, ensure_ascii=False)}

Do the reasoning internally.
Return only the useful plan, answer, or deliverable.
Do not reveal private chain-of-thought.
"""

    system = _brain_system(
        chosen,
        text_value,
        mode="complex",
        delegation=delegation,
    )

    result = query_gemini_api(
        system,
        text_value,
        history_messages,
        temperature=0.3,
    )

    if result:
        return result

    return _intelligent_fallback(
        chosen,
        text_value,
    )


def _intelligent_fallback(
    staff,
    user_text,
):
    """
    Honest fallback when Gemini is unavailable.
    """
    return (
        f"**{staff['name']} — {staff['role']}**\n\n"
        f"I can handle: "
        f"{', '.join(staff.get('skills', [])[:5])}.\n\n"
        f"Request received: **{str(user_text)[:300]}**\n\n"
        "Gemini is not available right now, so I won't pretend "
        "this task was executed. Check GEMINI_API_KEY and "
        "GEMINI_MODEL, then retry."
    )
    # ==============================================================================
# OFFICE DATA BRIDGE
# ==============================================================================

if "office_data" not in st.session_state:
    st.session_state.office_data = {
        "tasks": st.session_state.get("tasks", []),
        "approvals": st.session_state.get("approvals", []),
        "paper_positions": st.session_state.get("paper_positions", []),
        "trade_history": st.session_state.get("trade_history", []),
        "webhooks": st.session_state.get("webhooks", []),
        "memory": st.session_state.get("memory", []),
        "treasury": st.session_state.get(
            "treasury",
            {
                "balance": 0.0,
                "reserve": 0.0,
                "income": 0.0,
                "expenses": 0.0,
                "payouts": 0.0,
            },
        ),
    }


def sync_office_data():
    """
    Keep the compatibility office_data dictionary synchronized with
    Streamlit session state.
    """
    office = st.session_state.office_data

    st.session_state.tasks = office.get(
        "tasks",
        st.session_state.get("tasks", []),
    )

    st.session_state.approvals = office.get(
        "approvals",
        st.session_state.get("approvals", []),
    )

    st.session_state.paper_positions = office.get(
        "paper_positions",
        st.session_state.get("paper_positions", []),
    )

    st.session_state.trade_history = office.get(
        "trade_history",
        st.session_state.get("trade_history", []),
    )

    st.session_state.webhooks = office.get(
        "webhooks",
        st.session_state.get("webhooks", []),
    )

    st.session_state.memory = office.get(
        "memory",
        st.session_state.get("memory", []),
    )

    st.session_state.treasury = office.get(
        "treasury",
        st.session_state.get("treasury", {}),
    )


sync_office_data()


# ==============================================================================
# SIDEBAR COMMAND NAVIGATION
# ==============================================================================

st.sidebar.markdown(
    """
    <div style="
        padding:8px 4px 16px 4px;
        border-bottom:1px solid rgba(71,85,105,0.35);
        margin-bottom:14px;
    ">
        <div style="
            font-size:22px;
            font-weight:900;
            color:#f8fafc;
        ">
            🏢 AutoOffice OS
        </div>

        <div style="
            font-size:11px;
            color:#64748b;
            margin-top:3px;
            letter-spacing:0.6px;
            text-transform:uppercase;
        ">
            Autonomous Multi-Agent Command Deck
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

api_key_present = bool(get_gemini_api_key())

if api_key_present:
    st.sidebar.success(
        "🟢 Gemini Intelligence: Connected",
        icon="🧠",
    )
else:
    st.sidebar.warning(
        "🟡 Gemini API key not detected",
        icon="⚠️",
    )

st.sidebar.caption(
    f"Brain Engine v{BRAIN_VERSION}"
)

nav_options = [
    "📈 Live Trades & MT5 Terminal",
    "🛡️ Profit Vault & Treasury",
    "📋 Approvals & Daily Tasks",
    "👔 CEO War Room (Marcus)",
    "👤 1-on-1 Workers Desks (11 Staff)",
    "👥 Department Teams",
    "🏢 Virtual 2D Floorplan",
    "💻 Code & Deliverables Vault",
    "🌐 Live Web & Tab Inspector",
]

nav_option = st.sidebar.radio(
    "COMMAND CENTER",
    nav_options,
    key="main_navigation",
)

st.sidebar.markdown("---")

st.sidebar.markdown(
    """
    <div style="
        font-size:10px;
        color:#475569;
        line-height:1.6;
    ">
        <b>SECURITY MODE</b><br>
        Demo / Paper Trading Only<br>
        No real broker execution<br>
        No automatic financial transfers
    </div>
    """,
    unsafe_allow_html=True,
)


# ==============================================================================
# TAB 1 — LIVE TRADES & MT5 TERMINAL
# ==============================================================================

if nav_option == "📈 Live Trades & MT5 Terminal":

    st.markdown(
        """
        <div class="deck-card glow-emerald">
            <div style="
                display:flex;
                justify-content:space-between;
                align-items:center;
                gap:15px;
            ">
                <div>
                    <div style="
                        font-size:25px;
                        font-weight:900;
                    ">
                        📈 Live Trades & MT5 Terminal
                    </div>

                    <div style="
                        color:#94a3b8;
                        margin-top:5px;
                        font-size:13px;
                    ">
                        Market-analysis workspace with paper/demo
                        position simulation.
                    </div>
                </div>

                <span class="badge-pill badge-emerald">
                    🟢 DEMO / PAPER MODE
                </span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.warning(
        "⚠️ This terminal is a simulation workspace. "
        "It does not place real broker orders."
    )

    # --------------------------------------------------------------------------
    # MARKET TICKERS
    # --------------------------------------------------------------------------

    ticker_columns = st.columns(5)

    ticker_data = [
        ("XAU/USD", "Gold", "2,650.00"),
        ("EUR/USD", "Euro / Dollar", "1.1050"),
        ("GBP/USD", "Pound / Dollar", "1.3200"),
        ("USD/JPY", "Dollar / Yen", "148.20"),
        ("BTC/USD", "Bitcoin", "95,000"),
    ]

    for column, ticker in zip(
        ticker_columns,
        ticker_data,
    ):
        with column:
            st.markdown(
                f"""
                <div class="ticker-pill">
                    <div style="
                        font-size:11px;
                        color:#64748b;
                        font-weight:700;
                    ">
                        {ticker[0]}
                    </div>

                    <div style="
                        font-size:17px;
                        font-weight:800;
                        margin-top:3px;
                    ">
                        {ticker[2]}
                    </div>

                    <div style="
                        font-size:10px;
                        color:#94a3b8;
                        margin-top:2px;
                    ">
                        {ticker[1]}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("### 📊 Paper Market Workspace")

    chart_col, info_col = st.columns(
        [2.2, 1],
        gap="large",
    )

    with chart_col:

        # Deterministic SVG-style chart so the interface remains
        # functional without requiring an external chart package.
        svg_points = (
            "20,180 55,165 90,172 125,140 160,150 "
            "195,118 230,130 265,102 300,110 335,78 "
            "370,90 405,63 440,70 475,48 510,60 "
            "545,38 580,52 615,30"
        )

        st.markdown(
            f"""
            <div class="deck-card" style="padding:10px;">
                <div style="
                    display:flex;
                    justify-content:space-between;
                    margin-bottom:8px;
                ">
                    <span style="
                        font-weight:800;
                        font-size:15px;
                    ">
                        XAU/USD — Paper Chart
                    </span>

                    <span class="badge-pill badge-cyan">
                        1H
                    </span>
                </div>

                <svg
                    viewBox="0 0 640 220"
                    width="100%"
                    height="300"
                    preserveAspectRatio="none"
                    style="
                        background:#07101d;
                        border-radius:10px;
                        border:1px solid #1e293b;
                    "
                >
                    <defs>
                        <linearGradient
                            id="areaGradient"
                            x1="0"
                            y1="0"
                            x2="0"
                            y2="1"
                        >
                            <stop
                                offset="0%"
                                stop-color="#22c55e"
                                stop-opacity="0.28"
                            />
                            <stop
                                offset="100%"
                                stop-color="#22c55e"
                                stop-opacity="0"
                            />
                        </linearGradient>
                    </defs>

                    <line
                        x1="20"
                        y1="45"
                        x2="620"
                        y2="45"
                        stroke="#1e293b"
                    />

                    <line
                        x1="20"
                        y1="90"
                        x2="620"
                        y2="90"
                        stroke="#1e293b"
                    />

                    <line
                        x1="20"
                        y1="135"
                        x2="620"
                        y2="135"
                        stroke="#1e293b"
                    />

                    <line
                        x1="20"
                        y1="180"
                        x2="620"
                        y2="180"
                        stroke="#1e293b"
                    />

                    <polyline
                        points="{svg_points}"
                        fill="none"
                        stroke="#22c55e"
                        stroke-width="3"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                    />

                    <polyline
                        points="20,180 55,165 90,172 125,140 160,150
                                195,118 230,130 265,102 300,110 335,78
                                370,90 405,63 440,70 475,48 510,60
                                545,38 580,52 615,30 615,200 20,200"
                        fill="url(#areaGradient)"
                        stroke="none"
                    />
                </svg>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with info_col:

        st.markdown(
            """
            <div class="deck-card">
                <div style="
                    font-size:12px;
                    color:#64748b;
                    text-transform:uppercase;
                    font-weight:800;
                ">
                    Terminal Status
                </div>

                <div style="
                    font-size:22px;
                    font-weight:900;
                    margin-top:4px;
                ">
                    🟢 ONLINE
                </div>

                <div style="
                    color:#94a3b8;
                    font-size:12px;
                    margin-top:8px;
                    line-height:1.6;
                ">
                    Analysis engine ready.<br>
                    Broker execution disabled.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.metric(
            "Paper Equity",
            "$10,000.00",
            "Demo balance",
        )

        st.metric(
            "Open Paper Positions",
            len(
                st.session_state.get(
                    "paper_positions",
                    [],
                )
            ),
        )

    # --------------------------------------------------------------------------
    # PAPER TRADE SIMULATOR
    # --------------------------------------------------------------------------

    st.markdown("### 🧪 Paper Trade Simulator")

    trade_col1, trade_col2, trade_col3, trade_col4 = st.columns(4)

    with trade_col1:
        trade_symbol = st.selectbox(
            "Symbol",
            [
                "XAU/USD",
                "EUR/USD",
                "GBP/USD",
                "USD/JPY",
                "BTC/USD",
            ],
            key="paper_trade_symbol",
        )

    with trade_col2:
        trade_side = st.selectbox(
            "Direction",
            [
                "BUY",
                "SELL",
            ],
            key="paper_trade_side",
        )

    with trade_col3:
        trade_size = st.number_input(
            "Paper Position Size",
            min_value=0.01,
            max_value=100.0,
            value=0.01,
            step=0.01,
            key="paper_trade_size",
        )

    with trade_col4:
        trade_entry = st.number_input(
            "Entry Price",
            min_value=0.0001,
            value=2650.0,
            step=0.01,
            key="paper_trade_entry",
        )

    if st.button(
        "🧪 Open Simulated Position",
        type="primary",
        use_container_width=True,
        key="open_paper_trade",
    ):
        paper_position = {
            "id": f"PAPER-{len(st.session_state.paper_positions) + 1}",
            "symbol": trade_symbol,
            "side": trade_side,
            "size": float(trade_size),
            "entry": float(trade_entry),
            "status": "PAPER OPEN",
            "timestamp": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
        }

        st.session_state.paper_positions.append(
            paper_position
        )

        st.session_state.office_data[
            "paper_positions"
        ] = st.session_state.paper_positions

        save_persistent_memory(
            st.session_state.office_data
        )

        st.success(
            f"Paper {trade_side} position created for "
            f"{trade_symbol}. No broker order was sent."
        )

    # --------------------------------------------------------------------------
    # OPEN PAPER POSITIONS
    # --------------------------------------------------------------------------

    st.markdown("### 📋 Open Paper Positions")

    positions = st.session_state.get(
        "paper_positions",
        [],
    )

    if positions:

        for index, position in enumerate(
            positions
        ):
            pos_col1, pos_col2, pos_col3, pos_col4, pos_col5 = st.columns(
                [1.3, 1, 1, 1, 1]
            )

            with pos_col1:
                st.write(
                    f"**{position.get('symbol', 'N/A')}**"
                )
                st.caption(
                    position.get(
                        "id",
                        f"PAPER-{index + 1}",
                    )
                )

            with pos_col2:
                st.write(
                    position.get(
                        "side",
                        "N/A",
                    )
                )

            with pos_col3:
                st.write(
                    f"{position.get('size', 0):.2f}"
                )

            with pos_col4:
                st.write(
                    f"{position.get('entry', 0):,.2f}"
                )

            with pos_col5:
                if st.button(
                    "Close",
                    key=f"close_paper_{index}",
                ):
                    closed = dict(position)
                    closed["status"] = "PAPER CLOSED"
                    closed["closed_at"] = (
                        datetime.now().strftime(
                            "%Y-%m-%d %H:%M:%S"
                        )
                    )

                    st.session_state.trade_history.append(
                        closed
                    )

                    st.session_state.paper_positions.pop(
                        index
                    )

                    st.session_state.office_data[
                        "paper_positions"
                    ] = st.session_state.paper_positions

                    st.session_state.office_data[
                        "trade_history"
                    ] = st.session_state.trade_history

                    save_persistent_memory(
                        st.session_state.office_data
                    )

                    st.rerun()

    else:
        st.info(
            "No paper positions are currently open."
        )

    st.markdown("---")

    st.caption(
        "Ray Dalton desk: educational/demo trading workspace only. "
        "No live broker execution is connected to this interface."
    )


# ==============================================================================
# TAB 2 — PROFIT VAULT & TREASURY
# ==============================================================================

elif nav_option == "🛡️ Profit Vault & Treasury":

    st.markdown(
        """
        <div class="deck-card glow-amber">
            <div style="
                font-size:25px;
                font-weight:900;
            ">
                🛡️ Profit Vault & Treasury
            </div>

            <div style="
                color:#94a3b8;
                font-size:13px;
                margin-top:5px;
            ">
                Internal bookkeeping and treasury tracking.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    treasury = st.session_state.office_data.setdefault(
        "treasury",
        {
            "balance": 0.0,
            "reserve": 0.0,
            "income": 0.0,
            "expenses": 0.0,
            "payouts": 0.0,
        },
    )

    treasury_cols = st.columns(5)

    with treasury_cols[0]:
        st.metric(
            "Balance",
            f"${treasury.get('balance', 0.0):,.2f}",
        )

    with treasury_cols[1]:
        st.metric(
            "Reserve",
            f"${treasury.get('reserve', 0.0):,.2f}",
        )

    with treasury_cols[2]:
        st.metric(
            "Income",
            f"${treasury.get('income', 0.0):,.2f}",
        )

    with treasury_cols[3]:
        st.metric(
            "Expenses",
            f"${treasury.get('expenses', 0.0):,.2f}",
        )

    with treasury_cols[4]:
        st.metric(
            "Payouts",
            f"${treasury.get('payouts', 0.0):,.2f}",
        )

    st.markdown("### 💰 Treasury Ledger")

    income_tab, expense_tab, settlement_tab = st.tabs(
        [
            "➕ Income",
            "➖ Expense",
            "🔄 Settlement",
        ]
    )

    with income_tab:

        income_amount = st.number_input(
            "Income amount",
            min_value=0.0,
            value=0.0,
            step=10.0,
            key="treasury_income_amount",
        )

        income_note = st.text_input(
            "Income description",
            key="treasury_income_note",
        )

        if st.button(
            "Record Income",
            key="record_income",
            use_container_width=True,
        ):
            if income_amount <= 0:
                st.warning(
                    "Enter an amount greater than zero."
                )
            else:
                treasury["income"] += float(
                    income_amount
                )
                treasury["balance"] += float(
                    income_amount
                )

                st.success(
                    f"Recorded ${income_amount:,.2f} income."
                )

                save_persistent_memory(
                    st.session_state.office_data
                )

    with expense_tab:

        expense_amount = st.number_input(
            "Expense amount",
            min_value=0.0,
            value=0.0,
            step=10.0,
            key="treasury_expense_amount",
        )

        expense_note = st.text_input(
            "Expense description",
            key="treasury_expense_note",
        )

        if st.button(
            "Record Expense",
            key="record_expense",
            use_container_width=True,
        ):
            if expense_amount <= 0:
                st.warning(
                    "Enter an amount greater than zero."
                )
            elif expense_amount > treasury.get(
                "balance",
                0.
        # ==============================================================================
# OFFICE DATA BRIDGE
# ==============================================================================

def build_office_data():
    """
    Keep the older office_data interface synchronized with Streamlit state.
    This prevents older UI sections from breaking when the underlying state
    is stored in individual session-state keys.
    """
    if "office_data" not in st.session_state:
        st.session_state.office_data = {}

    office = st.session_state.office_data

    office["tasks"] = st.session_state.get(
        "tasks",
        [],
    )

    office["approvals"] = st.session_state.get(
        "approvals",
        [],
    )

    office["paper_positions"] = st.session_state.get(
        "paper_positions",
        [],
    )

    office["trade_history"] = st.session_state.get(
        "trade_history",
        [],
    )

    office["webhooks"] = st.session_state.get(
        "webhooks",
        [],
    )

    office["memory"] = st.session_state.get(
        "memory",
        [],
    )

    office["treasury"] = st.session_state.get(
        "treasury",
        {},
    )

    return office


build_office_data()


# ==============================================================================
# LOAD SAVED MEMORY
# ==============================================================================

def load_persistent_memory():
    if not os.path.exists(MEMORY_FILE):
        return

    try:
        with open(
            MEMORY_FILE,
            "r",
            encoding="utf-8",
        ) as f:
            saved = json.load(f)

        if not isinstance(saved, dict):
            return

        for key in (
            "tasks",
            "approvals",
            "paper_positions",
            "trade_history",
            "webhooks",
            "memory",
            "treasury",
        ):
            if key in saved:
                st.session_state[key] = saved[key]

        build_office_data()

    except Exception:
        # Corrupt or unavailable persistence must not stop the app.
        pass


if not st.session_state.get("_persistent_memory_loaded"):
    load_persistent_memory()
    st.session_state._persistent_memory_loaded = True


# ==============================================================================
# SESSION / PERSISTENCE SYNCHRONIZATION
# ==============================================================================

def sync_office_state():
    office = build_office_data()

    save_persistent_memory(
        {
            "tasks": office.get("tasks", []),
            "approvals": office.get("approvals", []),
            "paper_positions": office.get("paper_positions", []),
            "trade_history": office.get("trade_history", []),
            "webhooks": office.get("webhooks", []),
            "memory": office.get("memory", []),
            "treasury": office.get("treasury", {}),
        }
    )


# ==============================================================================
# UTILITY HELPERS
# ==============================================================================

def money(value):
    try:
        return f"${float(value):,.2f}"
    except Exception:
        return "$0.00"


def safe_float(value, default=0.0):
    try:
        return float(value)
    except Exception:
        return float(default)


def now_label():
    return datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


def add_memory_event(
    event_type,
    message,
):
    office = build_office_data()

    memory = office.setdefault(
        "memory",
        [],
    )

    memory.append(
        {
            "timestamp": now_label(),
            "type": str(event_type),
            "message": str(message)[:1000],
        }
    )

    # Keep persistent memory compact.
    office["memory"] = memory[-100:]

    st.session_state.memory = office["memory"]
    sync_office_state()


def add_chat_message(
    chat_key,
    sender,
    text,
):
    """
    Generic chat-history helper.
    """
    if chat_key == "ceo":
        history = st.session_state.setdefault(
            "ceo_chat",
            [],
        )
    else:
        history = st.session_state.worker_chats.setdefault(
            chat_key,
            [],
        )

    history.append(
        {
            "sender": sender,
            "text": str(text),
            "timestamp": now_label(),
        }
    )

    # Prevent giant sessions.
    if len(history) > 50:
        del history[:-50]

    return history


def chat_history_for_brain(history):
    return [
        {
            "sender": item.get("sender", ""),
            "text": item.get("text", ""),
        }
        for item in history[-12:]
    ]


# ==============================================================================
# PAPER TRADING HELPERS
# ==============================================================================

def create_paper_position(
    symbol,
    direction,
    entry_price,
    quantity,
    stop_loss=None,
    take_profit=None,
):
    """
    Create a local paper-trading position only.

    No broker API is called.
    No real order is submitted.
    """
    direction = str(direction).upper()

    if direction not in {
        "BUY",
        "SELL",
    }:
        return None

    position_id = (
        f"PAPER-{len(st.session_state.paper_positions) + 1:04d}"
    )

    position = {
        "id": position_id,
        "symbol": str(symbol).upper(),
        "direction": direction,
        "entry": safe_float(entry_price),
        "quantity": safe_float(quantity),
        "stop_loss": (
            safe_float(stop_loss)
            if stop_loss is not None
            else None
        ),
        "take_profit": (
            safe_float(take_profit)
            if take_profit is not None
            else None
        ),
        "status": "OPEN",
        "opened_at": now_label(),
        "source": "AutoOffice Paper Simulator",
    }

    st.session_state.paper_positions.append(
        position
    )

    st.session_state.trade_history.append(
        {
            **position,
            "event": "OPEN",
        }
    )

    sync_office_state()

    return position


def close_paper_position(
    position_id,
    exit_price,
):
    for position in st.session_state.paper_positions:
        if position.get("id") != position_id:
            continue

        if position.get("status") != "OPEN":
            continue

        entry = safe_float(
            position.get("entry")
        )
        exit_value = safe_float(exit_price)
        quantity = safe_float(
            position.get("quantity"),
            1,
        )

        if position.get("direction") == "BUY":
            pnl = (
                exit_value - entry
            ) * quantity
        else:
            pnl = (
                entry - exit_value
            ) * quantity

        position["status"] = "CLOSED"
        position["exit"] = exit_value
        position["pnl"] = pnl
        position["closed_at"] = now_label()

        st.session_state.trade_history.append(
            {
                **position,
                "event": "CLOSE",
            }
        )

        sync_office_state()

        return position

    return None


# ==============================================================================
# SVG PAPER MARKET CHART
# ==============================================================================

def build_demo_market_svg(
    symbol="XAU/USD",
):
    """
    Generates a lightweight illustrative chart.
    Values are explicitly labelled as simulated/demo data.
    """
    points = [
        (30, 180),
        (65, 165),
        (100, 174),
        (135, 148),
        (170, 158),
        (205, 132),
        (240, 140),
        (275, 112),
        (310, 126),
        (345, 94),
        (380, 104),
        (415, 76),
        (450, 88),
        (485, 60),
        (520, 72),
    ]

    polyline_points = " ".join(
        f"{x},{y}"
        for x, y in points
    )

    return f"""
    <div style="
        background:#050914;
        border:1px solid #1e293b;
        border-radius:14px;
        padding:14px;
        margin:8px 0 16px 0;
    ">
        <div style="
            display:flex;
            justify-content:space-between;
            align-items:center;
            margin-bottom:8px;
        ">
            <div style="
                color:#e2e8f0;
                font-weight:800;
                font-size:15px;
            ">
                {symbol} — DEMO MARKET VIEW
            </div>

            <div style="
                color:#fbbf24;
                font-size:11px;
                font-weight:700;
            ">
                SIMULATED DATA
            </div>
        </div>

        <svg
            viewBox="0 0 550 220"
            width="100%"
            height="220"
            preserveAspectRatio="none"
        >
            <line
                x1="0"
                y1="40"
                x2="550"
                y2="40"
                stroke="#1e293b"
                stroke-width="1"
            />
            <line
                x1="0"
                y1="90"
                x2="550"
                y2="90"
                stroke="#1e293b"
                stroke-width="1"
            />
            <line
                x1="0"
                y1="140"
                x2="550"
                y2="140"
                stroke="#1e293b"
                stroke-width="1"
            />
            <line
                x1="0"
                y1="190"
                x2="550"
                y2="190"
                stroke="#1e293b"
                stroke-width="1"
            />

            <polyline
                points="{polyline_points}"
                fill="none"
                stroke="#22d3ee"
                stroke-width="3"
                stroke-linejoin="round"
                stroke-linecap="round"
            />
        </svg>

        <div style="
            color:#64748b;
            font-size:10px;
            text-align:center;
            margin-top:2px;
        ">
            Paper/demo visualization only — not live market data.
        </div>
    </div>
    """


# ==============================================================================
# SIDEBAR NAVIGATION
# ==============================================================================

st.sidebar.markdown(
    """
    <div style="
        padding:8px 4px 16px 4px;
        border-bottom:1px solid #1e293b;
        margin-bottom:12px;
    ">
        <div style="
            font-size:22px;
            font-weight:900;
            color:#f8fafc;
        ">
            🏢 AutoOffice OS
        </div>

        <div style="
            font-size:11px;
            color:#64748b;
            margin-top:4px;
        ">
            Autonomous Enterprise Command Deck
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


api_key_available = bool(
    get_gemini_api_key()
)

if api_key_available:
    st.sidebar.success(
        "🟢 Gemini Intelligence: ONLINE"
    )
else:
    st.sidebar.warning(
        "🟡 Gemini Intelligence: API KEY NOT FOUND"
    )


nav_option = st.sidebar.radio(
    "COMMAND DECK",
    [
        "📈 Live Trades & MT5 Terminal",
        "🛡️ Profit Vault & Treasury",
        "📋 Approvals & Daily Tasks",
        "👔 CEO War Room (Marcus)",
        "👤 1-on-1 Workers Desks (11 Staff)",
        "👥 Department Teams",
        "🏢 Virtual 2D Floorplan",
        "💻 Code & Deliverables Vault",
        "🌐 Live Web & Tab Inspector",
    ],
    key="main_navigation",
)


st.sidebar.markdown(
    "---"
)

st.sidebar.caption(
    f"Brain version: {BRAIN_VERSION}"
)

st.sidebar.caption(
    "Execution mode: DEMO / PAPER"
)

st.sidebar.caption(
    f"Session time: {datetime.now().strftime('%H:%M:%S')}"
)


# ==============================================================================
# TAB 1 — LIVE TRADES & MT5 TERMINAL
# ==============================================================================

if nav_option == "📈 Live Trades & MT5 Terminal":

    st.title(
        "📈 Live Trades & MT5 Terminal"
    )

    st.caption(
        "Paper-trading workspace. No broker orders are submitted."
    )

    metric_a, metric_b, metric_c, metric_d = st.columns(4)

    with metric_a:
        st.metric(
            "Mode",
            "DEMO",
        )

    with metric_b:
        st.metric(
            "Open Paper Positions",
            len(
                [
                    position
                    for position in st.session_state.paper_positions
                    if position.get("status") == "OPEN"
                ]
            ),
        )

    with metric_c:
        st.metric(
            "Trade Records",
            len(
                st.session_state.trade_history
            ),
        )

    with metric_d:
        st.metric(
            "Broker Orders",
            "0",
        )

    st.markdown(
        build_demo_market_svg(
            "XAU/USD"
        ),
        unsafe_allow_html=True,
    )

    left_col, right_col = st.columns(
        [1, 1]
    )

    with left_col:
        st.subheader(
            "🧪 Paper Trade Simulator"
        )

        symbol = st.text_input(
            "Symbol",
            value="XAU/USD",
            key="paper_symbol",
        )

        direction = st.selectbox(
            "Direction",
            [
                "BUY",
                "SELL",
            ],
            key="paper_direction",
        )

        entry_price = st.number_input(
            "Entry Price",
            min_value=0.0,
            value=3000.0,
            step=0.01,
            key="paper_entry",
        )

        quantity = st.number_input(
            "Paper Quantity",
            min_value=0.01,
            value=0.01,
            step=0.01,
            key="paper_quantity",
        )

        stop_loss = st.number_input(
            "Stop Loss (optional)",
            min_value=0.0,
            value=0.0,
            step=0.01,
            key="paper_sl",
        )

        take_profit = st.number_input(
            "Take Profit (optional)",
            min_value=0.0,
            value=0.0,
            step=0.01,
            key="paper_tp",
        )

        if st.button(
            "🧪 Create Paper Position",
            use_container_width=True,
        ):
            position = create_paper_position(
                symbol=symbol,
                direction=direction,
                entry_price=entry_price,
                quantity=quantity,
                stop_loss=(
                    stop_loss
                    if stop_loss > 0
                    else None
                ),
                take_profit=(
                    take_profit
                    if take_profit > 0
                    else None
                ),
            )

            if position:
                add_memory_event(
                    "paper_trade",
                    (
                        f"Created paper {direction} position "
                        f"{position['id']} for {symbol}."
                    ),
                )

                st.success(
                    f"Paper position {position['id']} created."
                )

                st.info(
                    "This is only a local simulation. "
                    "No real broker order was sent."
                )

    with right_col:
        st.subheader(
            "📋 Open Paper Positions"
        )

        open_positions = [
            position
            for position in st.session_state.paper_positions
            if position.get("status") == "OPEN"
        ]

        if not open_positions:
            st.info(
                "No open paper positions."
            )

        for position in open_positions:
            with st.container(
                border=True
            ):
                st.markdown(
                    f"""
                    **{position.get('symbol', 'UNKNOWN')}**
                    — {position.get('direction', '')}

                    Position ID: `{position.get('id', '')}`

                    Entry:
                    `{position.get('entry', 0)}`

                    Quantity:
                    `{position.get('quantity', 0)}`
                    """
                )

                exit_price = st.number_input(
                    "Simulated Exit Price",
                    min_value=0.0,
                    value=float(
                        position.get(
                            "entry",
                            0.0,
                        )
                    ),
                    step=0.01,
                    key=f"exit_{position['id']}",
                )

                if st.button(
                    "Close Paper Position",
                    key=f"close_{position['id']}",
                    use_container_width=True,
                ):
                    closed = close_paper_position(
                        position["id"],
                        exit_price,
                    )

                    if closed:
                        st.success(
                            f"Paper position closed. "
                            f"Simulated P/L: "
                            f"{money(closed.get('pnl', 0))}"
                        )
                        st.rerun()

    st.subheader(
        "📜 Paper Trade History"
    )

    if st.session_state.trade_history:
        for record in reversed(
            st.session_state.trade_history[-20:]
        ):
            st.write(
                f"`{record.get('timestamp', '')}` "
                f"**{record.get('event', '')}** — "
                f"{record.get('symbol', '')} "
                f"{record.get('direction', '')} "
                f"— {record.get('status', '')}"
            )
    else:
        st.caption(
            "No paper-trade history yet."
        )
        # ==============================================================================
# TAB 2 — PROFIT VAULT & TREASURY
# ==============================================================================

elif nav_option == "🛡️ Profit Vault & Treasury":

    st.title("🛡️ Profit Vault & Treasury")

    st.caption(
        "Internal bookkeeping workspace. "
        "No real bank transfers or payments are executed here."
    )

    treasury = st.session_state.treasury

    # --------------------------------------------------------------------------
    # TREASURY METRICS
    # --------------------------------------------------------------------------

    balance = safe_float(
        treasury.get("balance", 0)
    )
    reserve = safe_float(
        treasury.get("reserve", 0)
    )
    income = safe_float(
        treasury.get("income", 0)
    )
    expenses = safe_float(
        treasury.get("expenses", 0)
    )
    payouts = safe_float(
        treasury.get("payouts", 0)
    )

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric(
            "Balance",
            money(balance),
        )

    with col2:
        st.metric(
            "Reserve",
            money(reserve),
        )

    with col3:
        st.metric(
            "Income",
            money(income),
        )

    with col4:
        st.metric(
            "Expenses",
            money(expenses),
        )

    with col5:
        st.metric(
            "Payouts",
            money(payouts),
        )

    st.markdown("---")

    # --------------------------------------------------------------------------
    # LEDGER CONTROLS
    # --------------------------------------------------------------------------

    income_tab, expense_tab, reserve_tab = st.tabs(
        [
            "➕ Record Income",
            "➖ Record Expense",
            "🛡️ Manage Reserve",
        ]
    )

    with income_tab:

        st.subheader("Record Income")

        income_amount = st.number_input(
            "Amount",
            min_value=0.0,
            value=0.0,
            step=10.0,
            key="vault_income_amount",
        )

        income_description = st.text_input(
            "Description",
            key="vault_income_description",
        )

        if st.button(
            "➕ Add Income",
            key="vault_add_income",
            use_container_width=True,
        ):

            if income_amount <= 0:
                st.warning(
                    "Enter an amount greater than zero."
                )

            else:
                treasury["income"] = (
                    safe_float(
                        treasury.get("income", 0)
                    )
                    + income_amount
                )

                treasury["balance"] = (
                    safe_float(
                        treasury.get("balance", 0)
                    )
                    + income_amount
                )

                add_memory_event(
                    "treasury_income",
                    (
                        f"Recorded internal income of "
                        f"{money(income_amount)}"
                        + (
                            f" — {income_description}"
                            if income_description
                            else ""
                        )
                    ),
                )

                st.success(
                    f"Recorded {money(income_amount)} income."
                )

                st.rerun()

    with expense_tab:

        st.subheader("Record Expense")

        expense_amount = st.number_input(
            "Amount",
            min_value=0.0,
            value=0.0,
            step=10.0,
            key="vault_expense_amount",
        )

        expense_description = st.text_input(
            "Description",
            key="vault_expense_description",
        )

        if st.button(
            "➖ Add Expense",
            key="vault_add_expense",
            use_container_width=True,
        ):

            if expense_amount <= 0:
                st.warning(
                    "Enter an amount greater than zero."
                )

            elif expense_amount > balance:
                st.warning(
                    "The recorded treasury balance is "
                    "not sufficient for this simulated expense."
                )

            else:
                treasury["expenses"] = (
                    safe_float(
                        treasury.get("expenses", 0)
                    )
                    + expense_amount
                )

                treasury["balance"] = (
                    safe_float(
                        treasury.get("balance", 0)
                    )
                    - expense_amount
                )

                add_memory_event(
                    "treasury_expense",
                    (
                        f"Recorded internal expense of "
                        f"{money(expense_amount)}"
                        + (
                            f" — {expense_description}"
                            if expense_description
                            else ""
                        )
                    ),
                )

                st.success(
                    f"Recorded {money(expense_amount)} expense."
                )

                st.rerun()

    with reserve_tab:

        st.subheader("Reserve Allocation")

        reserve_action = st.radio(
            "Action",
            [
                "Move balance → reserve",
                "Move reserve → balance",
            ],
            key="reserve_action",
        )

        reserve_amount = st.number_input(
            "Amount",
            min_value=0.0,
            value=0.0,
            step=10.0,
            key="reserve_amount",
        )

        if st.button(
            "🔄 Update Reserve",
            key="update_reserve",
            use_container_width=True,
        ):

            if reserve_amount <= 0:
                st.warning(
                    "Enter an amount greater than zero."
                )

            elif (
                reserve_action
                == "Move balance → reserve"
            ):

                if reserve_amount > balance:
                    st.warning(
                        "Not enough recorded balance."
                    )
                else:
                    treasury["balance"] -= reserve_amount
                    treasury["reserve"] += reserve_amount

                    add_memory_event(
                        "reserve_transfer",
                        (
                            f"Moved {money(reserve_amount)} "
                            "from balance to reserve."
                        ),
                    )

                    st.success(
                        "Reserve updated."
                    )

                    st.rerun()

            else:

                if reserve_amount > reserve:
                    st.warning(
                        "Not enough recorded reserve."
                    )
                else:
                    treasury["reserve"] -= reserve_amount
                    treasury["balance"] += reserve_amount

                    add_memory_event(
                        "reserve_transfer",
                        (
                            f"Moved {money(reserve_amount)} "
                            "from reserve to balance."
                        ),
                    )

                    st.success(
                        "Reserve updated."
                    )

                    st.rerun()

    # --------------------------------------------------------------------------
    # TREASURY STATE
    # --------------------------------------------------------------------------

    st.markdown("---")

    st.subheader("📊 Treasury State")

    treasury_json = json.dumps(
        treasury,
        indent=2,
        ensure_ascii=False,
    )

    st.code(
        treasury_json,
        language="json",
    )

    if st.button(
        "💾 Save Treasury State",
        key="save_treasury_state",
    ):
        sync_office_state()
        st.success(
            "Treasury state saved."
        )


# ==============================================================================
# TAB 3 — APPROVALS & DAILY TASKS
# ==============================================================================

elif nav_option == "📋 Approvals & Daily Tasks":

    st.title("📋 Approvals & Daily Tasks")

    st.caption(
        "Task management and approval tracking."
    )

    # --------------------------------------------------------------------------
    # TASK CREATOR
    # --------------------------------------------------------------------------

    st.subheader("➕ Create Office Task")

    task_col1, task_col2 = st.columns(
        [2, 1]
    )

    with task_col1:
        task_title = st.text_input(
            "Task title",
            placeholder=(
                "Example: Build the landing page"
            ),
            key="new_task_title",
        )

    with task_col2:

        agent_choices = [
            staff["name"]
            for staff in STAFF_MEMBERS
        ]

        selected_agent = st.selectbox(
            "Assign to",
            agent_choices,
            key="new_task_agent",
        )

    task_priority = st.selectbox(
        "Priority",
        [
            "normal",
            "high",
            "urgent",
        ],
        key="new_task_priority",
    )

    if st.button(
        "🚀 Create Task",
        type="primary",
        use_container_width=True,
        key="create_office_task",
    ):

        if not task_title.strip():
            st.warning(
                "Enter a task title first."
            )

        else:

            selected_staff = next(
                (
                    staff
                    for staff in STAFF_MEMBERS
                    if staff["name"]
                    == selected_agent
                ),
                STAFF_MEMBERS[0],
            )

            new_task = record_auto_task(
                agent_name=selected_staff["name"],
                dept_name=selected_staff["dept"],
                task_title=task_title.strip(),
            )

            new_task["priority"] = task_priority

            add_memory_event(
                "task_created",
                (
                    f"Created task '{task_title.strip()}' "
                    f"for {selected_staff['name']}."
                ),
            )

            st.success(
                f"Task {new_task['id']} created."
            )

            st.rerun()

    st.markdown("---")

    # --------------------------------------------------------------------------
    # APPROVAL QUEUE
    # --------------------------------------------------------------------------

    st.subheader("🛡️ Approval Queue")

    approvals = st.session_state.approvals

    if not approvals:

        st.info(
            "No pending approvals."
        )

    else:

        for index, approval in enumerate(
            approvals
        ):

            with st.container(
                border=True
            ):

                st.markdown(
                    f"""
                    **{approval.get('title', 'Untitled Approval')}**

                    Requester:
                    `{approval.get('requester', 'Unknown')}`

                    Status:
                    `{approval.get('status', 'pending')}`
                    """
                )

                approve_col, reject_col = st.columns(2)

                with approve_col:

                    if st.button(
                        "✅ Approve",
                        key=f"approve_{index}",
                        use_container_width=True,
                    ):

                        approval["status"] = "approved"
                        approval["approved_at"] = now_label()

                        add_memory_event(
                            "approval",
                            (
                                f"Approved: "
                                f"{approval.get('title', 'Untitled')}"
                            ),
                        )

                        sync_office_state()
                        st.rerun()

                with reject_col:

                    if st.button(
                        "❌ Reject",
                        key=f"reject_{index}",
                        use_container_width=True,
                    ):

                        approval["status"] = "rejected"
                        approval["rejected_at"] = now_label()

                        add_memory_event(
                            "approval",
                            (
                                f"Rejected: "
                                f"{approval.get('title', 'Untitled')}"
                            ),
                        )

                        sync_office_state()
                        st.rerun()

    # --------------------------------------------------------------------------
    # TASK BOARD
    # --------------------------------------------------------------------------

    st.markdown("---")

    st.subheader("🗂️ Task Board")

    tasks = st.session_state.tasks

    if not tasks:

        st.info(
            "No office tasks have been created yet."
        )

    else:

        for task_index, task in enumerate(
            tasks[:50]
        ):

            status = str(
                task.get(
                    "status",
                    "recorded",
                )
            )

            progress = safe_float(
                task.get(
                    "progress",
                    0,
                )
            )

            with st.container(
                border=True
            ):

                title_col, status_col = st.columns(
                    [3, 1]
                )

                with title_col:

                    st.markdown(
                        f"### {task.get('title', 'Untitled Task')}"
                    )

                    st.caption(
                        f"ID: {task.get('id', 'N/A')} "
                        f"• Agent: {task.get('agent', 'Unassigned')} "
                        f"• Department: {task.get('dept', 'N/A')}"
                    )

                with status_col:

                    st.write(
                        f"**{status.upper()}**"
                    )

                    st.progress(
                        min(
                            100,
                            max(
                                0,
                                int(progress),
                            ),
                        )
                        / 100
                    )

                st.write(
                    task.get(
                        "deliverable",
                        "No deliverable recorded.",
                    )
                )

                if task.get("exec_logs"):

                    with st.expander(
                        "Execution log"
                    ):

                        for log in task[
                            "exec_logs"
                        ]:

                            st.write(
                                log
                            )


# ==============================================================================
# TAB 4 — CEO WAR ROOM
# ==============================================================================

elif nav_option == "👔 CEO War Room (Marcus)":

    st.title(
        "👔 CEO War Room — Marcus"
    )

    st.caption(
        "Direct executive AI interface."
    )

    # --------------------------------------------------------------------------
    # CEO HEADER
    # --------------------------------------------------------------------------

    ceo = _find_staff(
        "agent-ceo"
    )

    st.markdown(
        f"""
        <div style="
            border:1px solid #334155;
            border-radius:14px;
            padding:18px;
            margin-bottom:18px;
            background:rgba(15,23,42,0.65);
        ">
            <div style="
                font-size:22px;
                font-weight:900;
                color:#f8fafc;
            ">
                {ceo.get('icon', '👔')}
                {ceo.get('name', 'Marcus')}
            </div>

            <div style="
                color:#94a3b8;
                margin-top:4px;
            ">
                {ceo.get(
                    'title',
                    'Chief Executive Officer'
                )}
            </div>

            <div style="
                color:#22d3ee;
                font-size:11px;
                margin-top:10px;
                font-weight:700;
            ">
                AI BRAIN: {BRAIN_VERSION}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # --------------------------------------------------------------------------
    # CEO CHAT INITIALIZATION
    # --------------------------------------------------------------------------

    if "ceo_chat" not in st.session_state:
        st.session_state.ceo_chat = []

    # --------------------------------------------------------------------------
    # CHAT HISTORY
    # --------------------------------------------------------------------------

    for message_index, message in enumerate(
        st.session_state.ceo_chat
    ):

        sender = message.get(
            "sender",
            "assistant",
        )

        role = (
            "user"
            if sender == "user"
            else "assistant"
        )

        with st.chat_message(
            role
        ):

            st.markdown(
                message.get(
                    "text",
                    "",
                )
            )

    # --------------------------------------------------------------------------
    # CEO INPUT
    # --------------------------------------------------------------------------

    ceo_prompt = st.chat_input(
        "Talk to Marcus...",
        key="ceo_chat_input",
    )

    if ceo_prompt:

        ceo_prompt = ceo_prompt.strip()

        if ceo_prompt:

            add_chat_message(
                "ceo",
                "user",
                ceo_prompt,
            )

            with st.chat_message(
                "user"
            ):
                st.markdown(
                    ceo_prompt
                )

            with st.chat_message(
                "assistant"
            ):

                with st.spinner(
                    "Marcus is thinking..."
                ):

                    response = office_brain(
                        user_text=ceo_prompt,
                        current_staff_id="agent-ceo",
                        history_messages=chat_history_for_brain(
                            st.session_state.ceo_chat
                        ),
                        mode="auto",
                    )

                st.markdown(
                    response
                )

                render_copy_button(
                    response,
                    f"ceo_response_{len(st.session_state.ceo_chat)}",
                )

            add_chat_message(
                "ceo",
                "assistant",
                response,
            )

            add_memory_event(
                "ceo_chat",
                ceo_prompt,
            )

            st.rerun()
        # ==============================================================================
# TAB 5 — 1-ON-1 WORKER DESKS
# ==============================================================================

elif nav_option == "🧑‍💼 Worker Desks":

    st.title("🧑‍💼 Worker Desks")

    st.caption(
        "Direct access to every specialist in the AutoOffice."
    )

    # --------------------------------------------------------------------------
    # AGENT SELECTOR
    # --------------------------------------------------------------------------

    agent_names = [
        staff["name"]
        for staff in STAFF_MEMBERS
        if staff["id"] != "agent-ceo"
    ]

    selected_worker_name = st.selectbox(
        "Choose a worker",
        agent_names,
        key="selected_worker_desk",
    )

    selected_worker = next(
        (
            staff
            for staff in STAFF_MEMBERS
            if staff["name"] == selected_worker_name
        ),
        STAFF_MEMBERS[1],
    )

    st.markdown("---")

    # --------------------------------------------------------------------------
    # WORKER PROFILE
    # --------------------------------------------------------------------------

    profile_col1, profile_col2 = st.columns(
        [1, 3]
    )

    with profile_col1:

        st.markdown(
            f"""
            <div style="
                font-size:64px;
                text-align:center;
                padding:20px;
            ">
                {selected_worker.get('icon', '🤖')}
            </div>
            """,
            unsafe_allow_html=True,
        )

    with profile_col2:

        st.subheader(
            selected_worker.get(
                "name",
                "Worker",
            )
        )

        st.write(
            selected_worker.get(
                "title",
                selected_worker.get(
                    "role",
                    "Specialist",
                ),
            )
        )

        st.caption(
            f"Department: "
            f"{selected_worker.get('dept', 'N/A')}"
        )

        st.caption(
            f"Desk: "
            f"{selected_worker.get('desk', 'N/A')}"
        )

        skills = selected_worker.get(
            "skills",
            [],
        )

        if skills:

            st.write(
                "**Core skills:** "
                + " • ".join(skills)
            )

    # --------------------------------------------------------------------------
    # WORKER CHAT
    # --------------------------------------------------------------------------

    worker_chat_key = (
        f"worker_chat_{selected_worker['id']}"
    )

    if worker_chat_key not in st.session_state:

        st.session_state[
            worker_chat_key
        ] = []

    st.markdown("---")

    st.subheader(
        f"💬 Chat with {selected_worker['name']}"
    )

    worker_history = st.session_state[
        worker_chat_key
    ]

    for message in worker_history:

        sender = message.get(
            "sender",
            "assistant",
        )

        role = (
            "user"
            if sender == "user"
            else "assistant"
        )

        with st.chat_message(
            role
        ):

            st.markdown(
                message.get(
                    "text",
                    "",
                )
            )

    worker_prompt = st.chat_input(
        f"Give {selected_worker['name']} a task...",
        key=f"worker_input_{selected_worker['id']}",
    )

    if worker_prompt:

        worker_prompt = worker_prompt.strip()

        if worker_prompt:

            worker_history.append(
                {
                    "sender": "user",
                    "text": worker_prompt,
                    "timestamp": now_label(),
                }
            )

            with st.chat_message(
                "user"
            ):

                st.markdown(
                    worker_prompt
                )

            with st.chat_message(
                "assistant"
            ):

                with st.spinner(
                    f"{selected_worker['name']} is working..."
                ):

                    worker_response = office_brain(
                        user_text=worker_prompt,
                        current_staff_id=selected_worker["id"],
                        history_messages=worker_history,
                        mode="direct",
                    )

                st.markdown(
                    worker_response
                )

                render_copy_button(
                    worker_response,
                    (
                        f"worker_response_"
                        f"{selected_worker['id']}_"
                        f"{len(worker_history)}"
                    ),
                )

            worker_history.append(
                {
                    "sender": "assistant",
                    "text": worker_response,
                    "timestamp": now_label(),
                }
            )

            add_memory_event(
                "worker_chat",
                (
                    f"{selected_worker['name']}: "
                    f"{worker_prompt}"
                ),
            )

            sync_office_state()

            st.rerun()

    # --------------------------------------------------------------------------
    # WORKER RESPONSIBILITIES
    # --------------------------------------------------------------------------

    st.markdown("---")

    st.subheader(
        "🎯 Responsibilities"
    )

    worker_prompt_text = selected_worker.get(
        "prompt",
        "Specialist responsible for assigned department tasks.",
    )

    st.info(
        worker_prompt_text
    )


# ==============================================================================
# TAB 6 — FULL OFFICE / DEPARTMENT COMMAND
# ==============================================================================

elif nav_option == "🏢 Office Command Center":

    st.title(
        "🏢 Office Command Center"
    )

    st.caption(
        "Coordinate the complete AI workforce from one place."
    )

    # --------------------------------------------------------------------------
    # OFFICE OVERVIEW
    # --------------------------------------------------------------------------

    total_agents = len(
        STAFF_MEMBERS
    )

    total_tasks = len(
        st.session_state.tasks
    )

    completed_tasks = sum(
        1
        for task in st.session_state.tasks
        if str(
            task.get(
                "status",
                "",
            )
        ).lower()
        == "completed"
    )

    pending_approvals = sum(
        1
        for approval in st.session_state.approvals
        if str(
            approval.get(
                "status",
                "pending",
            )
        ).lower()
        == "pending"
    )

    metric1, metric2, metric3, metric4 = st.columns(4)

    with metric1:
        st.metric(
            "AI Staff",
            total_agents,
        )

    with metric2:
        st.metric(
            "Office Tasks",
            total_tasks,
        )

    with metric3:
        st.metric(
            "Completed",
            completed_tasks,
        )

    with metric4:
        st.metric(
            "Pending Approvals",
            pending_approvals,
        )

    st.markdown("---")

    # --------------------------------------------------------------------------
    # DEPARTMENT DIRECTORY
    # --------------------------------------------------------------------------

    st.subheader(
        "🏢 Department Directory"
    )

    departments = {}

    for staff in STAFF_MEMBERS:

        department = staff.get(
            "dept",
            "General",
        )

        departments.setdefault(
            department,
            [],
        ).append(
            staff
        )

    for department_name, members in departments.items():

        with st.expander(
            f"🏢 {department_name} "
            f"({len(members)} staff)",
            expanded=True,
        ):

            for member in members:

                member_col1, member_col2, member_col3 = st.columns(
                    [1, 3, 2]
                )

                with member_col1:

                    st.markdown(
                        f"### {member.get('icon', '🤖')}"
                    )

                with member_col2:

                    st.write(
                        f"**{member.get('name', 'Unknown')}**"
                    )

                    st.caption(
                        member.get(
                            "title",
                            member.get(
                                "role",
                                "",
                            ),
                        )
                    )

                with member_col3:

                    st.caption(
                        member.get(
                            "desk",
                            "",
                        )
                    )

    # --------------------------------------------------------------------------
    # MULTI-AGENT TASK DISPATCH
    # --------------------------------------------------------------------------

    st.markdown("---")

    st.subheader(
        "🤖 Multi-Agent Task Dispatch"
    )

    st.write(
        "Give the office one objective. "
        "The CEO brain will identify the relevant specialist."
    )

    office_goal = st.text_area(
        "Office objective",
        placeholder=(
            "Example: Build a Streamlit dashboard, "
            "test it, and prepare the launch post."
        ),
        height=120,
        key="office_goal",
    )

    if st.button(
        "🚀 Dispatch Office Objective",
        type="primary",
        use_container_width=True,
        key="dispatch_office_objective",
    ):

        if not office_goal.strip():

            st.warning(
                "Enter an objective first."
            )

        else:

            routed_agent_id = _route_staff(
                office_goal,
                "agent-ceo",
            )

            routed_agent = _find_staff(
                routed_agent_id
            )

            st.session_state.office_dispatch = {
                "objective": office_goal.strip(),
                "agent": routed_agent.get(
                    "name",
                    "CEO",
                ),
                "agent_id": routed_agent_id,
                "timestamp": now_label(),
            }

            add_memory_event(
                "office_dispatch",
                (
                    f"Objective routed to "
                    f"{routed_agent.get('name', 'CEO')}: "
                    f"{office_goal.strip()}"
                ),
            )

            st.success(
                (
                    f"Objective routed to "
                    f"{routed_agent.get('name', 'CEO')}."
                )
            )

            sync_office_state()

    # --------------------------------------------------------------------------
    # CURRENT DISPATCH
    # --------------------------------------------------------------------------

    if st.session_state.get(
        "office_dispatch"
    ):

        dispatch = st.session_state.office_dispatch

        st.markdown("---")

        st.subheader(
            "📌 Current Dispatch"
        )

        st.info(
            (
                f"**Objective:** "
                f"{dispatch.get('objective', '')}\n\n"
                f"**Assigned:** "
                f"{dispatch.get('agent', 'CEO')}\n\n"
                f"**Created:** "
                f"{dispatch.get('timestamp', '')}"
            )
        )

    # --------------------------------------------------------------------------
    # INTELLIGENCE TEST
    # --------------------------------------------------------------------------

    st.markdown("---")

    st.subheader(
        "🧠 Office Intelligence Test"
    )

    st.caption(
        "Use this to test whether the AI understands the request "
        "instead of blindly role-playing."
    )

    intelligence_test = st.text_input(
        "Test request",
        placeholder=(
            "Example: What is 25 × 4?"
        ),
        key="intelligence_test",
    )

    if st.button(
        "🧠 Test Brain",
        key="test_brain",
        use_container_width=True,
    ):

        if not intelligence_test.strip():

            st.warning(
                "Enter a test request."
            )

        else:

            test_agent_id = _route_staff(
                intelligence_test,
                "agent-ceo",
            )

            test_agent = _find_staff(
                test_agent_id
            )

            with st.spinner(
                "Testing office intelligence..."
            ):

                test_response = office_brain(
                    user_text=intelligence_test.strip(),
                    current_staff_id=test_agent_id,
                    history_messages=[],
                    mode="direct",
                )

            st.markdown(
                f"**Routed to:** "
                f"{test_agent.get('name', 'CEO')}"
            )

            st.markdown(
                test_response
            )

            render_copy_button(
                test_response,
                "office_intelligence_test",
            )


# ==============================================================================
# TAB 7 — MEMORY & AUDIT CENTER
# ==============================================================================

elif nav_option == "🧠 Memory & Audit":

    st.title(
        "🧠 Memory & Audit Center"
    )

    st.caption(
        "Inspect what the office has recorded during this session."
    )

    # --------------------------------------------------------------------------
    # MEMORY SUMMARY
    # --------------------------------------------------------------------------

    memory_events = st.session_state.memory_events

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Memory Events",
            len(memory_events),
        )

    with col2:
        st.metric(
            "Tasks",
            len(st.session_state.tasks),
        )

    with col3:
        st.metric(
            "Chat Messages",
            len(
                st.session_state.chat_history
            ),
        )

    st.markdown("---")

    # --------------------------------------------------------------------------
    # EVENT LOG
    # --------------------------------------------------------------------------

    st.subheader(
        "📜 Event Log"
    )

    if not memory_events:

        st.info(
            "No memory events recorded yet."
        )

    else:

        for event in reversed(
            memory_events[-100:]
        ):

            event_type = event.get(
                "type",
                "event",
            )

            event_time = event.get(
                "timestamp",
                "",
            )

            event_text = event.get(
                "text",
                "",
            )

            st.markdown(
                f"""
                <div style="
                    border-left:3px solid #22d3ee;
                    padding:8px 14px;
                    margin-bottom:8px;
                    background:rgba(15,23,42,0.5);
                    border-radius:6px;
                ">
                    <b>{event_type}</b>
                    <span style="color:#94a3b8;">
                        — {event_time}
                    </span>
                    <br>
                    {event_text}
                </div>
                """,
                unsafe_allow_html=True,
            )

    # --------------------------------------------------------------------------
    # PERSISTENCE CONTROLS
    # --------------------------------------------------------------------------

    st.markdown("---")

    st.subheader(
        "💾 Persistence"
    )

    persistence_col1, persistence_col2 = st.columns(2)

    with persistence_col1:

        if st.button(
            "💾 Save Memory Now",
            use_container_width=True,
            key="save_memory_now",
        ):

            sync_office_state()

            st.success(
                "Office memory saved."
            )

    with persistence_col2:

        if st.button(
            "🔄 Reload Saved Memory",
            use_container_width=True,
            key="reload_memory_now",
        ):

            load_persistent_memory()

            st.success(
                "Saved memory reloaded."
            )

            st.rerun()
        # ==============================================================================
# TAB 8 — DEPARTMENT TEAMS
# ==============================================================================

elif nav_option == "👥 Department Teams":

    st.title("👥 Department Teams")

    st.caption(
        "Coordinate specialists by department."
    )

    departments = {}

    for staff in STAFF_MEMBERS:

        department = staff.get(
            "dept",
            "General",
        )

        departments.setdefault(
            department,
            [],
        ).append(
            staff
        )

    department_names = list(
        departments.keys()
    )

    if not department_names:

        st.info(
            "No departments configured."
        )

    else:

        selected_department = st.selectbox(
            "Department",
            department_names,
            key="selected_department",
        )

        members = departments[
            selected_department
        ]

        st.subheader(
            f"🏢 {selected_department}"
        )

        for member in members:

            with st.container(
                border=True
            ):

                col1, col2, col3 = st.columns(
                    [1, 4, 2]
                )

                with col1:
                    st.markdown(
                        f"## {member.get('icon', '🤖')}"
                    )

                with col2:

                    st.write(
                        f"**{member.get('name', 'Unknown')}**"
                    )

                    st.caption(
                        member.get(
                            "title",
                            member.get(
                                "role",
                                "Specialist",
                            ),
                        )
                    )

                with col3:

                    st.caption(
                        member.get(
                            "desk",
                            "AI Desk",
                        )
                    )


# ==============================================================================
# TAB 9 — VIRTUAL 2D FLOORPLAN
# ==============================================================================

elif nav_option == "🏢 Virtual 2D Floorplan":

    st.title(
        "🏢 Virtual 2D Office Floorplan"
    )

    st.caption(
        "Visual representation of the autonomous office."
    )

    floorplan_html = """
    <div style="
        background:#020617;
        border:1px solid #1e293b;
        border-radius:16px;
        padding:18px;
        min-height:520px;
    ">

        <div style="
            text-align:center;
            font-size:22px;
            font-weight:900;
            color:#f8fafc;
            margin-bottom:18px;
        ">
            AUTOOFFICE OS — HQ
        </div>

        <div style="
            display:grid;
            grid-template-columns:repeat(4,1fr);
            gap:12px;
        ">

            <div style="
                grid-column:span 4;
                background:#111827;
                border:1px solid #334155;
                border-radius:12px;
                padding:22px;
                text-align:center;
            ">
                <div style="font-size:34px;">👔</div>
                <b>CEO WAR ROOM</b>
                <div style="
                    color:#94a3b8;
                    font-size:11px;
                    margin-top:5px;
                ">
                    Marcus — Executive Intelligence
                </div>
            </div>

            <div style="
                background:#0f172a;
                border:1px solid #334155;
                border-radius:12px;
                padding:20px;
                text-align:center;
            ">
                <div style="font-size:30px;">📣</div>
                <b>MEDIA</b>
                <div style="
                    color:#64748b;
                    font-size:10px;
                ">
                    Social / Content
                </div>
            </div>

            <div style="
                background:#0f172a;
                border:1px solid #334155;
                border-radius:12px;
                padding:20px;
                text-align:center;
            ">
                <div style="font-size:30px;">📈</div>
                <b>TRADING</b>
                <div style="
                    color:#64748b;
                    font-size:10px;
                ">
                    Market Research
                </div>
            </div>

            <div style="
                background:#0f172a;
                border:1px solid #334155;
                border-radius:12px;
                padding:20px;
                text-align:center;
            ">
                <div style="font-size:30px;">💻</div>
                <b>ENGINEERING</b>
                <div style="
                    color:#64748b;
                    font-size:10px;
                ">
                    Applications / Code
                </div>
            </div>

            <div style="
                background:#0f172a;
                border:1px solid #334155;
                border-radius:12px;
                padding:20px;
                text-align:center;
            ">
                <div style="font-size:30px;">🧠</div>
                <b>RESEARCH</b>
                <div style="
                    color:#64748b;
                    font-size:10px;
                ">
                    Intelligence / Analysis
                </div>
            </div>

            <div style="
                grid-column:span 2;
                background:#0b1220;
                border:1px solid #334155;
                border-radius:12px;
                padding:20px;
                text-align:center;
            ">
                <div style="font-size:30px;">🛡️</div>
                <b>SECURITY & CONTROL</b>
                <div style="
                    color:#64748b;
                    font-size:10px;
                ">
                    Approvals / Audit / Safety
                </div>
            </div>

            <div style="
                grid-column:span 2;
                background:#0b1220;
                border:1px solid #334155;
                border-radius:12px;
                padding:20px;
                text-align:center;
            ">
                <div style="font-size:30px;">💰</div>
                <b>TREASURY</b>
                <div style="
                    color:#64748b;
                    font-size:10px;
                ">
                    Internal Accounting
                </div>
            </div>

        </div>
    </div>
    """

    st.markdown(
        floorplan_html,
        unsafe_allow_html=True,
    )


# ==============================================================================
# TAB 10 — CODE & DELIVERABLES VAULT
# ==============================================================================

elif nav_option == "💻 Code & Deliverables Vault":

    st.title(
        "💻 Code & Deliverables Vault"
    )

    st.caption(
        "Workspace for generated code, notes and deliverables."
    )

    deliverable_title = st.text_input(
        "Deliverable name",
        key="deliverable_title",
    )

    deliverable_content = st.text_area(
        "Content",
        height=300,
        key="deliverable_content",
    )

    if st.button(
        "💾 Save Deliverable",
        type="primary",
        use_container_width=True,
        key="save_deliverable",
    ):

        if not deliverable_title.strip():

            st.warning(
                "Enter a deliverable name."
            )

        elif not deliverable_content.strip():

            st.warning(
                "Enter some content."
            )

        else:

            deliverable = {
                "title": deliverable_title.strip(),
                "content": deliverable_content,
                "created_at": now_label(),
            }

            st.session_state.deliverables.append(
                deliverable
            )

            add_memory_event(
                "deliverable_saved",
                (
                    f"Saved deliverable: "
                    f"{deliverable_title.strip()}"
                ),
            )

            st.success(
                "Deliverable saved."
            )

    st.markdown("---")

    if not st.session_state.deliverables:

        st.info(
            "No deliverables saved yet."
        )

    else:

        for index, item in enumerate(
            reversed(
                st.session_state.deliverables
            )
        ):

            with st.expander(
                (
                    f"{item.get('title', 'Untitled')} "
                    f"— {item.get('created_at', '')}"
                )
            ):

                st.code(
                    item.get(
                        "content",
                        "",
                    ),
                    language="text",
                )


# ==============================================================================
# TAB 11 — LIVE WEB & TAB INSPECTOR
# ==============================================================================

elif nav_option == "🌐 Live Web & Tab Inspector":

    st.title(
        "🌐 Live Web & Tab Inspector"
    )

    st.caption(
        "Browser workspace for the office's web-research workflow."
    )

    st.warning(
        "Browser inspection is separate from this Streamlit interface. "
        "This panel records URLs and research notes; it does not silently "
        "take control of your personal browser."
    )

    url = st.text_input(
        "Website URL",
        placeholder="https://example.com",
        key="research_url",
    )

    research_note = st.text_area(
        "Research note",
        placeholder=(
            "Record what the agent found or what should be investigated."
        ),
        height=160,
        key="research_note",
    )

    if st.button(
        "🌐 Save Research Record",
        use_container_width=True,
        key="save_research_record",
    ):

        if not url.strip():

            st.warning(
                "Enter a URL."
            )

        else:

            research_record = {
                "url": url.strip(),
                "note": research_note.strip(),
                "created_at": now_label(),
            }

            st.session_state.research_records.append(
                research_record
            )

            add_memory_event(
                "web_research",
                (
                    f"Research record created for "
                    f"{url.strip()}"
                ),
            )

            st.success(
                "Research record saved."
            )

    st.markdown("---")

    st.subheader(
        "📚 Research Records"
    )

    if not st.session_state.research_records:

        st.info(
            "No research records yet."
        )

    else:

        for record in reversed(
            st.session_state.research_records[-30:]
        ):

            with st.container(
                border=True
            ):

                st.markdown(
                    f"**{record.get('url', '')}**"
                )

                st.caption(
                    record.get(
                        "created_at",
                        "",
                    )
                )

                if record.get("note"):

                    st.write(
                        record["note"]
                    )


# ==============================================================================
# FALLBACK
# ==============================================================================

else:

    st.title(
        "🏢 AutoOffice OS"
    )

    st.info(
        "Select a workspace from the sidebar."
    )


# ==============================================================================
# GLOBAL FOOTER
# ==============================================================================

st.markdown(
    """
    <div style="
        margin-top:40px;
        padding:18px 4px;
        border-top:1px solid #1e293b;
        color:#475569;
        font-size:10px;
        text-align:center;
    ">
        AutoOffice OS • Autonomous Multi-Agent Workspace
        <br>
        Gemini-powered intelligence • Demo / Paper execution mode
    </div>
    """,
    unsafe_allow_html=True,
)


# ==============================================================================
# FINAL STATE SYNC
# ==============================================================================

try:
    build_office_data()
except Exception:
    pass
