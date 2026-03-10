import streamlit as st
import json
import os
from datetime import datetime
import hashlib
from streamlit_option_menu import option_menu

# ============================================================================
# PAGE CONFIG
# ============================================================================
st.set_page_config(page_title="Studio Connect",
                   page_icon="🎬",
                   layout="wide",
                   initial_sidebar_state="expanded")

# ============================================================================
# CSS STYLING
# ============================================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    /* Global Theme */
    .stApp { background-color: #0B0E16; color: #FFFFFF; font-family: 'Inter', sans-serif; }
    [data-testid="stHeader"] { background: rgba(0,0,0,0); height: 0; }

    /* Global Header Area */
    .global-header {
        display: flex;
        align-items: center;
        padding: 15px 0px;
        margin-bottom: 20px;
        gap: 20px;
    }
    .search-bar {
        background: #13161F;
        border: 1px solid #1D212B;
        border-radius: 8px;
        padding: 10px 15px;
        flex-grow: 1;
        color: #9CA3AF;
        font-size: 14px;
    }

    /* Cards */
    .ui-card {
        background-color: #13161F;
        border-radius: 12px;
        padding: 24px;
        border: 1px solid #1D212B;
        margin-bottom: 20px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #0B0E16 !important;
        border-right: 1px solid #1D212B;
    }

    /* Typography */
    h1 { font-size: 32px !important; font-weight: 700 !important; margin-bottom: 5px !important; }
    h2 { font-size: 24px !important; font-weight: 600 !important; margin-top: 10px !important; }
    h3 { font-size: 18px !important; font-weight: 600 !important; color: #FFFFFF !important; }
    .subtitle { color: #9CA3AF; font-size: 14px; margin-bottom: 30px; }

    /* Metrics */
    .metric-title { color: #9CA3AF; font-size: 13px; font-weight: 500; margin-bottom: 8px; }
    .metric-value { font-size: 28px; font-weight: 700; color: #FFFFFF; }
    .metric-delta { font-size: 12px; font-weight: 600; margin-top: 4px; }
    .delta-up { color: #10B981; }

    /* Badges */
    .badge { padding: 4px 10px; border-radius: 6px; font-size: 11px; font-weight: 600; }
    .badge-blue { background: rgba(59, 130, 246, 0.1); color: #60A5FA; border: 1px solid rgba(59, 130, 246, 0.3); }
    .badge-green { background: rgba(16, 185, 129, 0.1); color: #34D399; border: 1px solid rgba(16, 185, 129, 0.3); }
    .badge-yellow { background: rgba(245, 158, 11, 0.1); color: #FBBF24; border: 1px solid rgba(245, 158, 11, 0.3); }

    /* Progress */
    .progress-track { background: #1F2937; border-radius: 10px; height: 6px; width: 100%; margin: 15px 0; }
    .progress-fill { background: #E50914; height: 100%; border-radius: 10px; transition: width 0.5s; }

    /* Default button styling */
    .stButton > button {
        background-color: #E50914 !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 6px !important;
        font-weight: 600 !important;
        padding: 10px !important;
    }

    /* Form Elements */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea, .stSelectbox>div>div>select {
        background-color: #1A1F2E !important;
        border: 1px solid #2D3748 !important;
        border-radius: 8px !important;
        color: #FFFFFF !important;
        padding: 10px !important;
    }

    .stTextInput>label, .stTextArea>label, .stSelectbox>label {
        color: #E5E7EB !important;
        font-weight: 500 !important;
        font-size: 14px !important;
    }

    /* Activity Feed */
    .activity-item { padding: 12px 0; border-bottom: 1px solid #1D212B; }
    .activity-time { color: #6B7280; font-size: 12px; }
</style>
""",
            unsafe_allow_html=True)


# ============================================================================
# DATA UTILITIES
# ============================================================================
def load_json(f):
    if os.path.exists(f):
        with open(f, 'r') as file:
            return json.load(file)
    return {}


def save_json(f, d):
    with open(f, 'w') as file:
        json.dump(d, file, indent=2)


def hash_txt(t):
    return hashlib.sha256(t.encode()).hexdigest()


def top_header():
    st.markdown("""
    <div class='global-header'>
        <div class='search-bar'>🔍 &nbsp; Search projects, pitches, or messages...</div>
        <div style='font-size: 20px; cursor: pointer;'>🔔</div>
    </div>
    """,
                unsafe_allow_html=True)


# ============================================================================
# DASHBOARD
# ============================================================================
def screen_dashboard():
    top_header()
    st.markdown(
        "<h1>Dashboard</h1><p class='subtitle'>Welcome back! Here's an overview of your studio's activity.</p>",
        unsafe_allow_html=True)

    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown(
            "<div class='ui-card'><p class='metric-title'>Active Pitches</p><div class='metric-value'>8</div><p class='metric-delta delta-up'>+2 this month</p></div>",
            unsafe_allow_html=True)
    with m2:
        st.markdown(
            "<div class='ui-card'><p class='metric-title'>In Production</p><div class='metric-value'>4</div><p class='metric-delta'>On schedule</p></div>",
            unsafe_allow_html=True)
    with m3:
        st.markdown(
            "<div class='ui-card'><p class='metric-title'>Total Views (30d)</p><div class='metric-value'>24.8M</div><p class='metric-delta delta-up'>+12.3% vs last month</p></div>",
            unsafe_allow_html=True)
    with m4:
        st.markdown(
            "<div class='ui-card'><p class='metric-title'>Revenue (YTD)</p><div class='metric-value'>$8.4M</div><p class='metric-delta delta-up'>+18.2% vs last year</p></div>",
            unsafe_allow_html=True)

    col_left, col_right = st.columns([2, 1])

    with col_left:
        st.markdown("<h3>Active Projects</h3>", unsafe_allow_html=True)
        projects = load_json('projects.json')
        for pid, p in projects.items():
            st.markdown(f"""
            <div class='ui-card'>
                <div style='display:flex; justify-content:space-between; align-items:start;'>
                    <div><b style='font-size:16px;'>{p.get('name')}</b><br><small style='color:#9CA3AF;'>{p.get('phase')}</small></div>
                    <span class='badge badge-blue'>In Production</span>
                </div>
                <div class='progress-track'><div class='progress-fill' style='width:{p.get('progress')}%'></div></div>
                <div style='display:flex; justify-content:space-between; font-size:12px;'>
                    <span>Due: {p.get('due')}</span><span>{p.get('progress')}%</span>
                </div>
            </div>
            """,
                        unsafe_allow_html=True)

    with col_right:
        st.markdown("<h3>Recent Activity</h3>", unsafe_allow_html=True)
        st.markdown("""
        <div class='ui-card'>
            <div class='activity-item'>
                <span class='badge badge-green'>Success</span> <span style='font-size:13px; color:#E5E7EB;'>Pitch 'Midnight Chronicles' approved</span><br>
                <span class='activity-time'>2 hours ago</span>
            </div>
            <div class='activity-item'>
                <span class='badge badge-blue'>Info</span> <span style='font-size:13px; color:#E5E7EB;'>New feedback on 'Desert Storm' pilot</span><br>
                <span class='activity-time'>5 hours ago</span>
            </div>
            <div class='activity-item'>
                <span class='badge badge-green'>Success</span> <span style='font-size:13px; color:#E5E7EB;'>'Ocean's Edge' Episode 3 delivered</span><br>
                <span class='activity-time'>1 day ago</span>
            </div>
        </div>
        """,
                    unsafe_allow_html=True)


# ============================================================================
# PITCH PORTAL
# ============================================================================
def screen_pitches():
    top_header()

    # Add pitch-specific CSS
    st.markdown("""
    <style>
    /* Pitch card styling */
    .pitch-card-button button {
        background-color: #1A1F2E !important;
        border: 2px solid #4A5568 !important;
        border-radius: 10px !important;
        padding: 16px !important;
        text-align: left !important;
        height: auto !important;
        white-space: normal !important;
        transition: all 0.2s ease !important;
        color: #FFFFFF !important;
    }

    .pitch-card-button button:hover {
        border-color: #E50914 !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 12px rgba(229, 9, 20, 0.2) !important;
    }

    .pitch-card-button button[kind="primary"] {
        background-color: rgba(229, 9, 20, 0.08) !important;
        border: 2px solid #E50914 !important;
    }
    </style>
    """,
                unsafe_allow_html=True)

    # Header with New Pitch button
    col_header = st.columns([4, 1])
    with col_header[0]:
        st.markdown(
            "<h1>Pitch Portal</h1><p class='subtitle'>Submit new pitches and track their progress through Netflix's review process.</p>",
            unsafe_allow_html=True)

    # Initialize modal state
    if 'show_new_pitch_modal' not in st.session_state:
        st.session_state.show_new_pitch_modal = False

    with col_header[1]:
        if st.button("➕ New Pitch"):
            st.session_state.show_new_pitch_modal = True
            st.rerun()

    # New Pitch Modal
    if st.session_state.show_new_pitch_modal:
        # Add close button at the very top
        top_row = st.columns([5, 1])
        with top_row[1]:
            if st.button("✕ Close Modal", key="close_btn_top"):
                st.session_state.show_new_pitch_modal = False
                st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)

        # Modal container
        m1, m2, m3 = st.columns([1, 3, 1])
        with m2:
            # Decorative header
            st.markdown("""
            <div style='background: linear-gradient(135deg, #1a1d29 0%, #13161f 100%); 
                        border: 2px solid #E50914; 
                        border-radius: 16px; 
                        padding: 30px; 
                        text-align: center;
                        box-shadow: 0 10px 40px rgba(229, 9, 20, 0.3);'>
                <div style='font-size: 50px; margin-bottom: 10px;'>🎬</div>
                <h2 style='color: #FFFFFF; margin: 10px 0; font-size: 28px;'>Submit New Pitch</h2>
                <p style='color: #9CA3AF; font-size: 14px;'>Share your creative vision with Netflix</p>
            </div>
            """,
                        unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            # Form starts here - OUTSIDE the decorative box
            with st.form("pitch_submission_form"):
                st.markdown("### 📝 Pitch Details")

                title = st.text_input("Project Title *",
                                      placeholder="Enter your project title")

                c1, c2 = st.columns(2)
                with c1:
                    genre = st.selectbox("Genre *", [
                        "Sci-Fi Thriller", "Drama", "Comedy", "Action",
                        "Horror", "Documentary", "Romance", "Adventure",
                        "Psychological Thriller", "Mystery"
                    ])
                with c2:
                    target = st.selectbox("Target Audience", [
                        "Adults 18-49", "Young Adults 18-34", "Family",
                        "Teens", "International"
                    ])

                logline = st.text_area(
                    "Logline",
                    placeholder=
                    "One compelling sentence that captures your story",
                    height=80)
                synopsis = st.text_area(
                    "Synopsis *",
                    placeholder=
                    "Detailed description of story, characters, and narrative",
                    height=150)

                st.markdown("<br>", unsafe_allow_html=True)

                # Form buttons
                btn1, btn2 = st.columns(2)
                with btn1:
                    cancel_btn = st.form_submit_button(
                        "Cancel", use_container_width=True)
                with btn2:
                    submit_btn = st.form_submit_button(
                        "Submit Pitch", use_container_width=True)

                # Handle form submission
                if cancel_btn:
                    st.session_state.show_new_pitch_modal = False
                    st.rerun()

                if submit_btn:
                    if title and genre and synopsis:
                        pitches = load_json('pitches.json')
                        new_id = str(len(pitches) + 1)
                        pitches[new_id] = {
                            "title": title,
                            "genre": genre,
                            "logline": logline,
                            "description": synopsis,
                            "target": target,
                            "studio": st.session_state.user['studio'],
                            "status": "Under Review",
                            "submitted": datetime.now().strftime("%b %d, %Y"),
                            "days_ago": "Just now"
                        }
                        save_json('pitches.json', pitches)
                        st.session_state.show_new_pitch_modal = False
                        st.session_state.sel_p = new_id
                        st.success("✅ Pitch submitted successfully!")
                        st.rerun()
                    else:
                        st.error(
                            "Please fill in all required fields marked with *")

    # Main content - Two columns
    col1, col2 = st.columns([1.2, 2.3])
    pitches = load_json('pitches.json')

    # Initialize selection to first pitch if not set
    if 'sel_p' not in st.session_state and pitches:
        st.session_state.sel_p = next(iter(pitches))

    # Status badge helper
    def get_status_badge(status):
        if status == "Under Review": return "badge-yellow"
        elif status == "Approved": return "badge-green"
        elif status == "Feedback Received": return "badge-blue"
        else: return "badge-yellow"

    # Default data
    status_map = {
        "1": "Under Review",
        "2": "Approved",
        "3": "Feedback Received",
        "4": "Under Review"
    }
    days_ago_map = {
        "1": "2 days ago",
        "2": "5 days ago",
        "3": "1 week ago",
        "4": "3 days ago"
    }

    # Left Column - Pitch List
    with col1:
        # Apply custom CSS for this column and clickable cards
        st.markdown("""
        <style>
        div[data-testid="column"]:first-child > div {
            background: #13161F !important;
            border: 1px solid #6B7280 !important;
            border-radius: 12px !important;
            padding: 20px !important;
            min-height: 700px !important;
        }

        /* Make pitch card buttons transparent and overlay */
        .pitch-card-wrapper {
            position: relative;
            margin-bottom: 15px;
        }

        .pitch-card-wrapper .stButton {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 10;
        }

        .pitch-card-wrapper .stButton > button {
            width: 100%;
            height: 100%;
            background: transparent !important;
            border: none !important;
            padding: 0 !important;
            cursor: pointer !important;
        }

        .pitch-card-wrapper .stButton > button:hover {
            background: transparent !important;
        }
        </style>
        """,
                    unsafe_allow_html=True)

        st.markdown("<h3 style='margin: 0 0 20px 0;'>Your Pitches</h3>",
                    unsafe_allow_html=True)

        # Render pitch cards
        for pid, p in pitches.items():
            selected = st.session_state.get('sel_p') == pid
            status = p.get('status', status_map.get(pid, "Under Review"))
            days_ago = str(p.get('days_ago', days_ago_map.get(pid,
                                                              "Recently")))

            # Get badge color
            if status == "Under Review":
                badge_color = "#FBBF24"
            elif status == "Approved":
                badge_color = "#34D399"
            else:
                badge_color = "#60A5FA"

            # Determine card styling
            if selected:
                card_bg = "rgba(229, 9, 20, 0.08)"
                card_border = "#E50914"
            else:
                card_bg = "#1A1F2E"
                card_border = "#4A5568"

            # Wrapper for card + button
            st.markdown('<div class="pitch-card-wrapper">',
                        unsafe_allow_html=True)

            # Render card as HTML
            st.markdown(f"""
            <div style='background: {card_bg}; border: 2px solid {card_border}; border-radius: 10px; padding: 16px; transition: all 0.2s ease; cursor: pointer; position: relative;'>
                <div style='display: flex; justify-content: space-between; align-items: start; margin-bottom: 8px;'>
                    <h4 style='margin: 0; font-size: 16px; color: #FFFFFF;'>{p['title']}</h4>
                    <span style='background: rgba(245, 158, 11, 0.1); color: {badge_color}; padding: 4px 8px; border-radius: 6px; font-size: 10px; font-weight: 600;'>{status}</span>
                </div>
                <p style='color: #9CA3AF; font-size: 13px; margin: 5px 0;'>{p['genre']}</p>
                <div style='display: flex; align-items: center; color: #6B7280; font-size: 12px; margin-top: 8px;'>
                    <span>🕒</span>
                    <span style='margin-left: 5px;'>{days_ago}</span>
                </div>
            </div>
            """,
                        unsafe_allow_html=True)

            # Transparent button overlay
            if st.button("", key=f"pitch_{pid}"):
                st.session_state.sel_p = pid
                st.rerun()

            st.markdown('</div>', unsafe_allow_html=True)

    # Right Column - Pitch Details
    with col2:
        sid = st.session_state.get('sel_p', next(iter(pitches), None))
        if sid and sid in pitches:
            p = pitches[sid]
            status = p.get('status', status_map.get(sid, "Under Review"))
            badge_class = get_status_badge(status)
            submitted_date = p.get('submitted', 'Nov 1, 2024')
            title = p.get('title', '')
            genre = p.get('genre', '')
            description = p.get('description', '')

            # Build HTML using string concatenation
            right_html = "<div style='background: #13161F; border: 1px solid #6B7280; border-radius: 12px; padding: 30px; min-height: 700px;'>"
            right_html += "<div style='display:flex; justify-content:space-between; align-items: start; margin-bottom: 15px;'>"
            right_html += "<div>"
            right_html += "<h2 style='margin: 0; font-size: 28px;'>" + title + "</h2>"
            right_html += "<p style='color: #9CA3AF; font-size: 14px; margin-top: 5px;'>" + genre + "</p>"
            right_html += "</div>"
            right_html += "<span class='badge " + badge_class + "'>" + status + "</span>"
            right_html += "</div>"
            right_html += "<hr style='border:0; border-top:1px solid #4A5568; margin:25px 0;'>"
            right_html += "<h3 style='font-size: 18px; margin-bottom: 20px;'>Review Timeline</h3>"
            right_html += "<div style='margin-bottom: 20px;'>"
            right_html += "<div style='display: flex; align-items: center; margin-bottom: 15px;'>"
            right_html += "<div style='width: 12px; height: 12px; background: #10B981; border-radius: 50%; margin-right: 15px;'></div>"
            right_html += "<div><b style='color: #FFFFFF; font-size: 15px;'>Submitted</b><br>"
            right_html += "<small style='color: #9CA3AF;'>" + submitted_date + "</small></div></div>"
            right_html += "<div style='border-left: 2px solid #4A5568; margin-left: 5px; padding-left: 22px; margin-bottom: 15px;'>"
            right_html += "<div style='display: flex; align-items: center; margin-top: -5px;'>"
            right_html += "<div style='width: 12px; height: 12px; background: #3B82F6; border-radius: 50%; margin-right: 15px; margin-left: -28px;'></div>"
            right_html += "<div><b style='color: #FFFFFF; font-size: 15px;'>Treatment Review</b><br>"
            right_html += "<small style='color: #9CA3AF;'>In progress</small></div></div></div>"
            right_html += "<div style='border-left: 2px solid #4A5568; margin-left: 5px; padding-left: 22px;'>"
            right_html += "<div style='display: flex; align-items: center; margin-top: -5px;'>"
            right_html += "<div style='width: 12px; height: 12px; background: #4B5563; border-radius: 50%; margin-right: 15px; margin-left: -28px;'></div>"
            right_html += "<div><b style='color: #6B7280; font-size: 15px;'>Decision</b><br>"
            right_html += "<small style='color: #6B7280;'>Pending</small></div></div></div></div>"
            right_html += "<hr style='border:0; border-top:1px solid #4A5568; margin:25px 0;'>"
            right_html += "<h3 style='font-size: 18px; margin-bottom: 15px;'>Synopsis</h3>"
            right_html += "<p style='font-size: 14px; line-height: 1.8; color: #D1D5DB;'>" + description + "</p>"
            right_html += "<div style='display: flex; gap: 15px; margin-top: 30px;'>"
            right_html += "<button style='flex: 1; background: #1A1F2E; border: 1px solid #4A5568; color: #FFFFFF; padding: 12px; border-radius: 8px; font-weight: 600;'>"
            right_html += "👁 View Full Pitch</button>"
            right_html += "<button style='flex: 1; background: #1A1F2E; border: 1px solid #4A5568; color: #FFFFFF; padding: 12px; border-radius: 8px; font-weight: 600;'>"
            right_html += "💬 Message Netflix Team</button></div></div>"

            st.markdown(right_html, unsafe_allow_html=True)


# ============================================================================
# PRODUCTION SUITE
# ============================================================================
def screen_production():
    top_header()
    st.markdown(
        "<h1>Production Suite</h1><p class='subtitle'>Manage your active productions and track deliverables.</p>",
        unsafe_allow_html=True)

    projects = load_json('projects.json')
    p = projects.get('1', {})

    c1, c2, c3 = st.columns([1.5, 1.5, 1])
    with c1:
        st.markdown(f"""
        <div class='ui-card' style='height:280px;'>
            <div style='display:flex; justify-content:space-between;'>
                <h3>{p.get('name', 'Project')}</h3>
                <span class='badge badge-blue'>In Production</span>
            </div>
            <p style='font-size:13px; margin-top:20px;'>Overall Progress</p>
            <div class='progress-track'><div class='progress-fill' style='width:{p.get('progress', 0)}%'></div></div>
            <p style='text-align:right; font-weight:700;'>{p.get('progress', 0)}%</p>
            <br>
            <button style='width:100%; background:#E50914; border:none; color:white; padding:10px; border-radius:6px; font-weight:600;'>⬆ Upload Deliverable</button>
        </div>
        """,
                    unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class='ui-card' style='height:280px;'>
            <h3>Budget Tracking</h3>
            <div style='display:flex; justify-content:space-between; margin-top:30px;'>
                <span style='font-size:14px;'>Spent</span><b style='font-size:20px;'>$7.8M</b>
            </div>
            <div style='display:flex; justify-content:space-between; margin-top:5px;'>
                <span style='font-size:14px;'>Total Budget</span><b style='font-size:14px; color:#9CA3AF;'>$12.0M</b>
            </div>
            <div class='progress-track'><div class='progress-fill' style='width:65%'></div></div>
            <p style='font-size:13px; color:#9CA3AF;'>$4.2M remaining</p>
        </div>
        """,
                    unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class='ui-card' style='height:280px;'>
            <h3>Quick Stats</h3>
            <p style='font-size:14px; margin-top:25px;'>Episodes Completed <span style='float:right; color:white;'>2/8</span></p>
            <p style='font-size:14px;'>Days Until Milestone <span style='float:right; color:white;'>6</span></p>
            <p style='font-size:14px;'>Open Issues <span style='float:right; color:#FBBF24;'>3</span></p>
        </div>
        """,
                    unsafe_allow_html=True)

    st.markdown("<h3>Deliverables Timeline</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class='ui-card'>
        <div style='display:flex; justify-content:space-between; align-items:center; padding:10px 0;'>
            <span>✅ Episode 1 - Final Cut <br><small style='color:#6B7280;'>Due: Nov 5</small></span>
            <span class='badge badge-green'>completed</span>
        </div>
        <hr style='border:0; border-top:1px solid #1D212B;'>
        <div style='display:flex; justify-content:space-between; align-items:center; padding:10px 0;'>
            <span>✅ Episode 2 - Final Cut <br><small style='color:#6B7280;'>Due: Nov 12</small></span>
            <span class='badge badge-green'>completed</span>
        </div>
        <hr style='border:0; border-top:1px solid #1D212B;'>
        <div style='display:flex; justify-content:space-between; align-items:center; padding:10px 0;'>
            <span>⚠️ Episode 3 - Rough Cut <br><small style='color:#6B7280;'>Due: Nov 20</small></span>
            <span class='badge badge-yellow'>in progress</span>
        </div>
    </div>
    """,
                unsafe_allow_html=True)


# ============================================================================
# ANALYTICS HUB
# ============================================================================
def screen_analytics():
    top_header()
    st.markdown(
        "<h1>Analytics Hub</h1><p class='subtitle'>Track the performance of your content on Netflix.</p>",
        unsafe_allow_html=True)

    a1, a2, a3, a4 = st.columns(4)
    a1.markdown(
        "<div class='ui-card'><small>Total Views (30d)</small><div class='metric-value'>24.8M</div><p class='metric-delta delta-up'>+12.3% vs last month</p></div>",
        unsafe_allow_html=True)
    a2.markdown(
        "<div class='ui-card'><small>Unique Viewers</small><div class='metric-value'>18.2M</div><p class='metric-delta delta-up'>+8.7% vs last month</p></div>",
        unsafe_allow_html=True)
    a3.markdown(
        "<div class='ui-card'><small>Avg. Watch Time</small><div class='metric-value'>42 min</div><p class='metric-delta delta-up'>+5.2% vs last month</p></div>",
        unsafe_allow_html=True)
    a4.markdown(
        "<div class='ui-card'><small>Top Region</small><div class='metric-value'>USA</div><p style='font-size:12px;'>38% of total views</p></div>",
        unsafe_allow_html=True)

    st.markdown("<h3>Content Performance</h3>", unsafe_allow_html=True)

    perf_data = [{
        "name": "Midnight Chronicles",
        "views": "8.2M",
        "rate": "87%",
        "time": "42 min",
        "region": "United States"
    }, {
        "name": "Desert Storm",
        "views": "5.6M",
        "rate": "91%",
        "time": "38 min",
        "region": "United Kingdom"
    }]

    for item in perf_data:
        st.markdown(f"""
        <div class='ui-card'>
            <div style='display:flex; justify-content:space-between; align-items:start;'>
                <b style='font-size:16px;'>{item['name']}</b>
                <div style='text-align:right;'><b style='font-size:18px;'>{item['views']}</b><br><small style='color:#9CA3AF;'>Total Views</small></div>
            </div>
            <div style='display:flex; gap:15px; margin-top:20px;'>
                <div style='flex:1; background:#1A1F2E; padding:15px; border-radius:10px; text-align:center;'>
                    <small style='color:#9CA3AF;'>Completion Rate</small><br><b style='color:#10B981; font-size:18px;'>{item['rate']}</b>
                </div>
                <div style='flex:1; background:#1A1F2E; padding:15px; border-radius:10px; text-align:center;'>
                    <small style='color:#9CA3AF;'>Avg. Watch Time</small><br><b style='color:#FFFFFF; font-size:18px;'>{item['time']}</b>
                </div>
                <div style='flex:1; background:#1A1F2E; padding:15px; border-radius:10px; text-align:center;'>
                    <small style='color:#9CA3AF;'>Top Region</small><br><b style='color:#FFFFFF; font-size:18px;'>{item['region']}</b>
                </div>
            </div>
        </div>
        """,
                    unsafe_allow_html=True)


# ============================================================================
# MAIN APP FLOW
# ============================================================================
def main():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        # Login Page
        c1, c2, c3 = st.columns([1, 1.5, 1])
        with c2:
            st.markdown(
                "<br><br><br><h1 style='text-align:center;'>Studio Connect</h1>",
                unsafe_allow_html=True)
            with st.form("login_form"):
                u = st.text_input("Username")
                p = st.text_input("Password", type="password")
                if st.form_submit_button("Sign In", use_container_width=True):
                    users = load_json('users.json')
                    if u in users and users[u]['password'] == hash_txt(p):
                        st.session_state.logged_in = True
                        st.session_state.user = users[u]
                        st.rerun()
                    else:
                        st.error("Access Denied")
    else:
        # Sidebar Navigation
        with st.sidebar:
            st.markdown(
                "<h2 style='color:#E50914; padding-left:10px;'>Studio Connect</h2><br>",
                unsafe_allow_html=True)
            sel = option_menu(menu_title=None,
                              options=[
                                  "Dashboard", "Pitch Portal", "Production",
                                  "Analytics", "Settings"
                              ],
                              icons=[
                                  "grid", "lightbulb", "camera-reels",
                                  "bar-chart", "gear"
                              ],
                              default_index=0,
                              styles={
                                  "container": {
                                      "background-color": "#0B0E16",
                                      "padding": "5px"
                                  },
                                  "nav-link": {
                                      "color": "#9CA3AF",
                                      "font-size": "14px",
                                      "padding": "12px",
                                      "margin": "5px 0px"
                                  },
                                  "nav-link-selected": {
                                      "background-color":
                                      "rgba(229, 9, 20, 0.1)",
                                      "color": "#E50914",
                                      "border-radius": "8px",
                                      "font-weight": "600"
                                  },
                              })

            st.markdown("<br><br><br><br><br><br>", unsafe_allow_html=True)
            st.markdown(f"""
            <div style='padding:15px; background:#13161F; border-radius:12px; border:1px solid #1D212B;'>
                <small style='color:#9CA3AF;'>User</small><br>
                <b>{st.session_state.user['name']}</b><br>
                <small style='color:#6B7280;'>{st.session_state.user['studio']}</small>
            </div>
            """,
                        unsafe_allow_html=True)

            if st.button("Logout", use_container_width=True):
                st.session_state.logged_in = False
                st.rerun()

        # Route to screens
        if sel == "Dashboard":
            screen_dashboard()
        elif sel == "Pitch Portal":
            screen_pitches()
        elif sel == "Production":
            screen_production()
        elif sel == "Analytics":
            screen_analytics()
        else:
            st.title("Settings")


# ============================================================================
# INITIALIZATION
# ============================================================================
def init():
    if not os.path.exists('users.json'):
        save_json(
            'users.json', {
                "studio_exec": {
                    "password": hash_txt("studio123"),
                    "name": "Phoenix Studios",
                    "studio": "Phoenix Studios"
                }
            })

    if not os.path.exists('projects.json'):
        save_json(
            'projects.json', {
                "1": {
                    "name": "Midnight Chronicles",
                    "phase": "Post-Production",
                    "progress": 65,
                    "due": "Dec 15, 2024",
                    "studio": "Phoenix Studios"
                }
            })

    if not os.path.exists('pitches.json'):
        save_json(
            'pitches.json', {
                "1": {
                    "title": "Midnight Chronicles",
                    "genre": "Sci-Fi Thriller",
                    "description":
                    "In a future where dreams can be recorded and shared, a rogue dream detective uncovers a conspiracy that threatens the fabric of reality itself. As she delves deeper into the mystery, she must confront her own buried memories and decide what's real and what's fabricated.",
                    "studio": "Phoenix Studios",
                    "status": "Under Review",
                    "submitted": "Nov 1, 2024",
                    "days_ago": "2 days ago"
                },
                "2": {
                    "title": "The Last Horizon",
                    "genre": "Drama",
                    "description":
                    "An astronaut confronts her past during humanity's first mission to Mars, discovering that the journey to another world requires confronting the demons she left behind on Earth.",
                    "studio": "Phoenix Studios",
                    "status": "Approved",
                    "submitted": "Oct 25, 2024",
                    "days_ago": "5 days ago"
                },
                "3": {
                    "title": "Echo Chamber",
                    "genre": "Psychological Thriller",
                    "description":
                    "A true crime podcaster discovers that her listeners' anonymous confessions are connected to a series of unsolved murders. As the line between storyteller and investigator blurs, she becomes the next target.",
                    "studio": "Phoenix Studios",
                    "status": "Feedback Received",
                    "submitted": "Oct 22, 2024",
                    "days_ago": "1 week ago"
                },
                "4": {
                    "title": "Starlight Runners",
                    "genre": "Adventure",
                    "description":
                    "In a colonized solar system, a crew of charismatic smugglers navigate dangerous trade routes while evading corporate authorities and space pirates, all while uncovering a conspiracy that could change humanity's future among the stars.",
                    "studio": "Phoenix Studios",
                    "status": "Under Review",
                    "submitted": "Oct 28, 2024",
                    "days_ago": "3 days ago"
                }
            })


if __name__ == "__main__":
    init()
    main()
