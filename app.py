# import streamlit as st

# st.set_page_config(layout="wide")

# # ---------------- DATA ---------------- #

# records = [
#     {
#         "id": "TPA-001",
#         "claim": "CLM-10021",
#         "insured": "ABC Logistics",
#         "lossDate": "2024-01-12",
#         "incurred": 125000,
#         "status": "Yet to Review",
#         "fields": [
#             {"key": "Claim Number", "value": "CLM-10021", "confidence": 98},
#             {"key": "Insured Name", "value": "ABC Logistics", "confidence": 95},
#             {"key": "Loss Date", "value": "2024-01-12", "confidence": 92},
#             {"key": "Paid Amount", "value": "85,000", "confidence": 88},
#             {"key": "Reserve Amount", "value": "40,000", "confidence": 85},
#             {"key": "Incurred", "value": "125,000", "confidence": 90},
#             {"key": "Claim Status", "value": "Open", "confidence": 93},
#             {"key": "LOB", "value": "Auto Liability", "confidence": 87},
#         ],
#     },
#     {
#         "id": "TPA-002",
#         "claim": "CLM-10045",
#         "insured": "Delta Transport",
#         "lossDate": "2024-02-03",
#         "incurred": 78000,
#         "status": "Review in Progress",
#         "fields": [
#             {"key": "Claim Number", "value": "CLM-10045", "confidence": 97},
#             {"key": "Insured Name", "value": "Delta Transport", "confidence": 94},
#             {"key": "Loss Date", "value": "2024-02-03", "confidence": 91},
#             {"key": "Paid Amount", "value": "50,000", "confidence": 84},
#             {"key": "Reserve Amount", "value": "28,000", "confidence": 82},
#             {"key": "Incurred", "value": "78,000", "confidence": 88},
#             {"key": "Claim Status", "value": "Open", "confidence": 92},
#             {"key": "LOB", "value": "Workers Comp", "confidence": 86},
#         ],
#     },
# ]

# if "selected" not in st.session_state:
#     st.session_state.selected = records[0]

# # ---------------- CSS ---------------- #

# st.markdown("""
# <style>
# .card {border:1px solid #ddd;border-radius:12px;padding:12px;margin-bottom:10px;cursor:pointer;}
# .card:hover {box-shadow:0 2px 8px rgba(0,0,0,.1)}
# .badge {padding:4px 8px;border-radius:8px;font-size:12px;}
# .gray{background:#eee}
# .yellow{background:#fde68a}
# .green{background:#bbf7d0}
# .field{display:grid;grid-template-columns:2fr 4fr 3fr;gap:12px;margin-bottom:8px}
# .progress{height:8px;background:#eee;border-radius:6px}
# .bar{height:8px;background:#3b82f6;border-radius:6px}
# </style>
# """, unsafe_allow_html=True)

# l,r = st.columns([1,2])

# # ---------------- LEFT ---------------- #

# with l:
#     st.markdown("### TPA Records")

#     for rcd in records:
#         if st.button(rcd["claim"], key=rcd["id"]):
#             st.session_state.selected = rcd

#         color = "gray"
#         if rcd["status"]=="Review in Progress": color="yellow"
#         if rcd["status"]=="Submitted": color="green"

#         st.markdown(f"""
# <div class="card">
# <b>{rcd['claim']}</b>
# <span class="badge {color}">{rcd['status']}</span><br>
# {rcd['insured']}<br>
# <small>Loss: {rcd['lossDate']}</small>
# </div>
# """, unsafe_allow_html=True)

# # ---------------- RIGHT ---------------- #

# with r:
#     st.markdown("### Review Details")

#     sel = st.session_state.selected

#     for f in sel["fields"]:
#         st.markdown(f"""
# <div class="field">
# <div>{f['key']}</div>
# <input value="{f['value']}" readonly />
# <div>
# <div class="progress">
# <div class="bar" style="width:{f['confidence']}%"></div>
# </div>
# {f['confidence']}%
# </div>
# </div>
# """, unsafe_allow_html=True)

#     c1,c2 = st.columns(2)

#     if c1.button("Mark In Progress"):
#         sel["status"]="Review in Progress"

#     if c2.button("Submit Record"):
#         sel["status"]="Submitted"






import streamlit as st

st.set_page_config(layout="wide", page_title="TPA Review Portal", page_icon="🛡️")

# ---------------- DATA ----------------

records = [
    {
        "id": "TPA-001",
        "claim": "CLM-10021",
        "insured": "ABC Logistics",
        "lossDate": "2024-01-12",
        "incurred": 125000,
        "status": "Yet to Review",
        "fields": [
            {"key": "Claim Number", "value": "CLM-10021", "confidence": 98},
            {"key": "Insured Name", "value": "ABC Logistics", "confidence": 95},
            {"key": "Loss Date", "value": "2024-01-12", "confidence": 92},
            {"key": "Paid Amount", "value": "$85,000", "confidence": 88},
            {"key": "Reserve Amount", "value": "$40,000", "confidence": 85},
            {"key": "Incurred", "value": "$125,000", "confidence": 90},
            {"key": "Claim Status", "value": "Open", "confidence": 93},
            {"key": "LOB", "value": "Auto Liability", "confidence": 87},
        ],
    },
    {
        "id": "TPA-002",
        "claim": "CLM-10045",
        "insured": "Delta Transport",
        "lossDate": "2024-02-03",
        "incurred": 78000,
        "status": "Review in Progress",
        "fields": [
            {"key": "Claim Number", "value": "CLM-10045", "confidence": 97},
            {"key": "Insured Name", "value": "Delta Transport", "confidence": 94},
            {"key": "Loss Date", "value": "2024-02-03", "confidence": 91},
            {"key": "Paid Amount", "value": "$50,000", "confidence": 84},
            {"key": "Reserve Amount", "value": "$28,000", "confidence": 82},
            {"key": "Incurred", "value": "$78,000", "confidence": 88},
            {"key": "Claim Status", "value": "Open", "confidence": 92},
            {"key": "LOB", "value": "Workers Comp", "confidence": 86},
        ],
    },
]

if "selected_id" not in st.session_state:
    st.session_state.selected_id = "TPA-001"

if "statuses" not in st.session_state:
    st.session_state.statuses = {r["id"]: r["status"] for r in records}

if "checked_fields" not in st.session_state:
    st.session_state.checked_fields = {r["id"]: [False]*len(r["fields"]) for r in records}

def get_selected():
    for r in records:
        if r["id"] == st.session_state.selected_id:
            return r
    return records[0]

def make_badge(status):
    if status == "Review in Progress":
        return '<span class="badge badge-yellow">In Progress</span>'
    if status == "Submitted":
        return '<span class="badge badge-green">Submitted</span>'
    return '<span class="badge badge-gray">Yet to Review</span>'

def conf_cls(conf):
    return ("conf-high","conf-label-high") if conf > 90 else ("conf-mid","conf-label-mid")

# ---------------- STYLES ----------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

/* RESET */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

/* FULL TOP FIX */
html, body {
    margin: 0 !important;
    padding: 0 !important;
    background: #080c15 !important;
}

/* Kill Streamlit header */
header { visibility: hidden !important; height: 0 !important; }

[data-testid="stApp"] {
    background: #080c15 !important;
}

/* Main container */
[data-testid="stAppViewContainer"],
[data-testid="stAppViewContainer"] > .main {
    background: #080c15 !important;
    font-family: 'Inter', sans-serif !important;
    color: #e2e8f0;
    padding-top: 0 !important;
    margin-top: 0 !important;
}

/* ORIGINAL RADIAL GLOW BACKGROUND */
[data-testid="stAppViewContainer"]::before {
    content: '';
    position: fixed;
    inset: 0;
    background:
        radial-gradient(ellipse 70% 55% at 0% 0%, rgba(99,102,241,.26) 0%, transparent 55%),
        radial-gradient(ellipse 55% 45% at 100% 100%, rgba(16,185,129,.18) 0%, transparent 55%),
        radial-gradient(ellipse 40% 35% at 50% 50%, rgba(139,92,246,.08) 0%, transparent 60%);
    pointer-events: none;
    z-index: 0;
}

/* Content wrapper */
[data-testid="block-container"] {
    position: relative;
    z-index: 1;
    padding: 2rem 2.5rem !important;
    max-width: 100% !important;
}

/* Panels */
.panel {
    background: rgba(255,255,255,.04);
    border: 1px solid rgba(255,255,255,.08);
    border-radius: 18px;
    padding: 1.2rem;
}

.panel-header {
    font-size: .90rem;
    font-weight: 1500;
    letter-spacing: .16em;
    text-transform: uppercase;
    color: #818cf8;
    margin-bottom: .4rem;
}

/* Cards */
.record-card {
    background: rgba(255,255,255,.035);
    border: 1px solid rgba(255,255,255,.07);
    border-radius: 12px;
    padding: .85rem 1rem;
    margin-bottom: .3rem;
}
.record-card.active {
    background: rgba(99,102,241,.15);
    border-color: rgba(99,102,241,.5);
}

.claim-id { font-weight: 700; }
.insured-name { font-size: .78rem; color: #94a3b8; }

/* Badges */
.badge { font-size: .62rem; padding: .18rem .5rem; border-radius: 20px; }
.badge-gray { background: rgba(100,116,139,.18); color: #94a3b8; }
.badge-yellow { background: rgba(245,158,11,.14); color: #fbbf24; }
.badge-green { background: rgba(52,211,153,.14); color: #34d399; }

/* Fields */
.field-row {
    display: flex;
    align-items: center;
    gap: .8rem;
    background: rgba(255,255,255,.03);
    border-radius: 10px;
    padding: .72rem 1rem;
}

.field-key { font-size: .68rem; width: 125px; color: #64748b; }
.field-value { flex: 1; font-weight: 600; }

.conf-bar-bg { width: 72px; height: 4px; background: #1f2933; border-radius: 99px; }
.conf-high { background: #34d399; height: 100%; }
.conf-mid { background: #f59e0b; height: 100%; }

.detail-header {
    margin-top: -.6rem !important;
    border-bottom: 1px solid rgba(255,255,255,.07);
    padding-bottom: .7rem;
}

.incurred-value { font-size: 1.4rem; font-weight: 800; color: #34d399; }

/* Select button */
.stButton > button {
    background: rgba(99,102,241,.15) !important;
    color: #c7d2fe !important;
    border: 1px solid rgba(99,102,241,.35) !important;
    border-radius: 10px !important;
    font-size: .75rem !important;
    padding: .45rem !important;
}

/* Action buttons */
.btn-progress button,
.btn-submit button {
    color: white !important;
}

.btn-progress button { background: linear-gradient(135deg,#4f46e5,#7c3aed)!important; }
.btn-submit button { background: linear-gradient(135deg,#059669,#10b981)!important; }

/* Hide Streamlit junk */
#MainMenu, footer { visibility: hidden; }
/* Prevent button text wrapping */
.stButton > button {
    white-space: nowrap !important;
    min-width: 160px !important;
}

/* Improved field label visibility */
.field-key {
    font-size: 0.8rem !important;          /* slightly bigger */
    color: #cbd5f5 !important;             /* lighter indigo-slate */
    font-weight: 600 !important;
    letter-spacing: 0.08em !important;
    text-transform: uppercase;
    opacity: 0.95;
}

</style>
""", unsafe_allow_html=True)

st.markdown("## 🛡️ TPA Claims Review Portal")

left,right=st.columns([1,2.2],gap="large")

# LEFT PANEL
with left:
    st.markdown('<div class="panel"><div class="panel-header">TPA Records</div>',unsafe_allow_html=True)

    for r in records:
        active=st.session_state.selected_id==r["id"]
        st.markdown(f"""
        <div class="record-card {'active' if active else ''}">
        <div class="claim-id">{r['claim']}</div>
        <div class="insured-name">{r['insured']}</div>
        {make_badge(st.session_state.statuses[r['id']])}
        </div>
        """,unsafe_allow_html=True)

        if st.button("Select",key=r["id"],use_container_width=True):
            st.session_state.selected_id=r["id"]
            st.rerun()

    st.markdown("</div>",unsafe_allow_html=True)

# RIGHT PANEL
with right:
    st.markdown('<div class="panel"><div class="panel-header">Review Details</div>',unsafe_allow_html=True)

    sel=get_selected()

    st.markdown(f"""
    <div class="detail-header">
    <div>
    <h2>{sel['claim']}</h2>
    <div>{sel['insured']} · {sel['lossDate']}</div>
    {make_badge(st.session_state.statuses[sel['id']])}
    </div>
    <div>
    <div>Total Incurred</div>
    <div class="incurred-value">${sel['incurred']:,}</div>
    </div>
    </div>
    """,unsafe_allow_html=True)

    checked=st.session_state.checked_fields[sel["id"]]

    for i,f in enumerate(sel["fields"]):
        col1,col2=st.columns([1,.08])
        with col1:
            bar,lbl=conf_cls(f["confidence"])
            st.markdown(f"""
            <div class="field-row">
            <div class="field-key">{f['key']}</div>
            <div class="field-value">{f['value']}</div>
            <div class="conf-bar-bg"><div class="{bar}" style="width:{f['confidence']}%"></div></div>
            <div>{f['confidence']}%</div>
            </div>
            """,unsafe_allow_html=True)

        with col2:
            cb=st.checkbox("",checked[i],key=f"{sel['id']}_{i}")
            st.session_state.checked_fields[sel["id"]][i]=cb

    left_btn, spacer, right_btn = st.columns([1, 3, 1])

    with left_btn:
        st.markdown('<div class="btn-progress">', unsafe_allow_html=True)
        if st.button("⚙️ Mark In Progress"):
            st.session_state.statuses[sel["id"]] = "Review in Progress"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    with right_btn:
        st.markdown('<div class="btn-submit">', unsafe_allow_html=True)
        if st.button("✅ Submit Record"):
            st.session_state.statuses[sel["id"]] = "Submitted"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("</div>",unsafe_allow_html=True)