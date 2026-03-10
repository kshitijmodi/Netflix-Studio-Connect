import streamlit as st

# ============================================================
# App Config
# ============================================================
st.set_page_config(
    page_title="Studio Connect",
    layout="wide",
)

# ============================================================
# Netflix-style CSS
# ============================================================
st.markdown("""
<style>
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #0B1220;
    color: #E5E7EB;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0B1220 0%, #070B14 100%);
    border-right: 1px solid #1F2937;
}

.card {
    background: linear-gradient(180deg, #0F172A 0%, #0B1220 100%);
    border: 1px solid #1F2937;
    border-radius: 14px;
    padding: 20px;
}

.metric-value {
    font-size: 32px;
    font-weight: 700;
}

.positive { color: #22C55E; }

.pill {
    padding: 4px 10px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 600;
}

.pill-blue { background: rgba(59,130,246,0.15); color: #60A5FA; }
.pill-green { background: rgba(34,197,94,0.15); color: #22C55E; }
.pill-yellow { background: rgba(234,179,8,0.15); color: #EAB308; }

.progress-container {
    background: #1F2937;
    border-radius: 999px;
    height: 8px;
    margin-top: 6px;
}

.progress-bar {
    background: #E50914;
    height: 8px;
    border-radius: 999px;
}

.stButton > button {
    background-color: #E50914;
    color: white;
    border-radius: 10px;
    padding: 10px 16px;
    font-weight: 600;
    border: none;
}
.stButton > button:hover { background-color: #F6121D; }
</style>
""", unsafe_allow_html=True)

# ============================================================
# Session State
# ============================================================
if "role" not in st.session_state:
    st.session_state.role = "Studio Executive"

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

# ============================================================
# Sidebar
# ============================================================
with st.sidebar:
    st.markdown("## 🎬 Studio Connect")

    st.session_state.role = st.selectbox(
        "User Persona",
        ["Studio Executive", "Netflix Executive"]
    )

    st.divider()

    st.session_state.page = st.radio(
        "Navigation",
        ["Dashboard", "Pitch Portal", "Production", "Contracts"]
    )

    st.divider()
    st.markdown("**Phoenix Studios**  \nStudio Executive")

# ============================================================
# Pages
# ============================================================
def dashboard():
    st.title("Dashboard")
    st.caption("Welcome back! Here's an overview of your studio's activity.")

    col1, col2, col3, col4 = st.columns(4)

    def metric(col, title, value, delta):
        with col:
            st.markdown(f"""
            <div class="card">
                <div>{title}</div>
                <div class="metric-value">{value}</div>
                <div class="positive">{delta}</div>
            </div>
            """, unsafe_allow_html=True)

    metric(col1, "Active Pitches", "8", "+2 this month")
    metric(col2, "In Production", "4", "On schedule")
    metric(col3, "Total Views (30d)", "24.8M", "+12.3% vs last month")
    metric(col4, "Revenue (YTD)", "$8.4M", "+18.2% vs last year")

    st.markdown("### Active Projects")

    st.markdown("""
    <div class="card">
        <strong>Midnight Chronicles</strong>
        <span class="pill pill-blue" style="float:right;">In Production</span>
        <p>Post-Production</p>
        <div class="progress-container">
            <div class="progress-bar" style="width:65%;"></div>
        </div>
        <p>Due: Dec 15, 2024</p>
    </div>
    """, unsafe_allow_html=True)

def pitch_portal():
    st.title("Pitch Portal")
    st.caption("Submit new pitches and track their progress through Netflix's review process.")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("""
        <div class="card">
            <strong>Midnight Chronicles</strong>
            <span class="pill pill-yellow" style="float:right;">Under Review</span>
            <p>Sci-Fi Thriller</p>
            <p>⏱ 2 days ago</p>
        </div>
        """, unsafe_allow_html=True)

        st.button("+ New Pitch")

    with col2:
        st.markdown("""
        <div class="card">
            <h4>Review Timeline</h4>
            <p><span class="pill pill-green">Submitted</span> Nov 1, 2024</p>
            <p><span class="pill pill-blue">Treatment Review</span> In progress</p>
            <p><span class="pill">Decision</span> Pending</p>

            <h4>Synopsis</h4>
            <p>
            In a future where dreams can be recorded and shared, a rogue dream detective
            uncovers a conspiracy that threatens reality itself.
            </p>
        </div>
        """, unsafe_allow_html=True)

def production():
    st.title("Production Suite")
    st.caption("Manage your active productions and track deliverables.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
            <strong>Midnight Chronicles</strong>
            <span class="pill pill-blue" style="float:right;">In Production</span>
            <p>Overall Progress: 65%</p>
            <div class="progress-container">
                <div class="progress-bar" style="width:65%;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <strong>Budget Tracking</strong>
            <p>Spent: <strong>$7.8M</strong></p>
            <p>Total Budget: $12.0M</p>
            <div class="progress-container">
                <div class="progress-bar" style="width:65%;"></div>
            </div>
            <p>$4.2M remaining</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <strong>Quick Stats</strong>
            <p>Episodes Completed: 2 / 8</p>
            <p>Days Until Next Milestone: 6</p>
            <p>Open Issues: <span style="color:#EAB308;">3</span></p>
        </div>
        """, unsafe_allow_html=True)

def contracts():
    st.title("Contracts")

    st.markdown("""
    <div class="card">
        <strong>Midnight Chronicles</strong>
        <p>Deal Type: Exclusive</p>
        <p>Status: Signed</p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# Router
# ============================================================
if st.session_state.page == "Dashboard":
    dashboard()
elif st.session_state.page == "Pitch Portal":
    pitch_portal()
elif st.session_state.page == "Production":
    production()
elif st.session_state.page == "Contracts":
    contracts()