import streamlit as st
import streamlit.components.v1 as components
import json
import os
import requests
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

    /* Global Theme - Lighter background */
    .stApp { background-color: #1A1D29; color: #FFFFFF; font-family: 'Inter', sans-serif; }
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

# ============================================================================
# CHANGE 1: NETFLIX-THEMED MODAL STYLING
# ============================================================================

# ADD THIS CSS TO YOUR MAIN CSS SECTION (around line 50-200):


/* ========== DIALOG/MODAL NETFLIX STYLING ========== */

    /* Dialog backdrop */
    [data-testid="stDialog"] {
        background: rgba(0, 0, 0, 0.85) !important;
    }

    /* Dialog container */
    [data-testid="stDialog"] > div > div {
        background: #1A1D29 !important;
        border: 1px solid #2D3748 !important;
        border-radius: 16px !important;
        padding: 0 !important;
    }

    /* Dialog header */
    [data-testid="stDialog"] h2 {
        background: linear-gradient(135deg, #E50914 0%, #B20710 100%) !important;
        color: #FFFFFF !important;
        padding: 20px 30px !important;
        margin: 0 !important;
        border-radius: 16px 16px 0 0 !important;
        font-weight: 700 !important;
        border-bottom: 2px solid #E50914 !important;
    }

    /* Dialog content area */
    [data-testid="stDialog"] [data-testid="stVerticalBlock"] {
        padding: 30px !important;
        background: #1A1D29 !important;
    }

    /* Form inputs in dialog */
    [data-testid="stDialog"] input,
    [data-testid="stDialog"] textarea,
    [data-testid="stDialog"] select {
        background-color: #242936 !important;
        border: 1px solid #2D3748 !important;
        color: #FFFFFF !important;
    }

    /* Form labels in dialog */
    [data-testid="stDialog"] label {
        color: #E5E7EB !important;
        font-weight: 500 !important;
    }

    /* Expander in dialog */
    [data-testid="stDialog"] [data-testid="stExpander"] {
        background: #242936 !important;
        border: 1px solid #2D3748 !important;
        border-radius: 8px !important;
    }

    /* Close button (X) */
    [data-testid="stDialog"] button[aria-label="Close"] {
        color: #FFFFFF !important;
    }

    [data-testid="stDialog"] button[aria-label="Close"]:hover {
        background: rgba(255, 255, 255, 0.1) !important;
    }

    /* Cards */
    .ui-card {
        background-color: #242936;
        border-radius: 12px;
        padding: 24px;
        border: 1px solid #2D3748;
        margin-bottom: 20px;
    }

    /* Sidebar - More visible chevron */
    section[data-testid="stSidebar"] {
        background-color: #0B0E16  !important;
        border-right: 1px solid #2D3748;
    }

    /* Remove the default sidebar content background to unify it */
    section[data-testid="stSidebar"] > div {
        background-color: #0B0E16 !important;
    }
    /* Make sidebar collapse button much more visible */
    [data-testid="collapsedControl"] {
        background-color: #E50914 !important;
        color: #FFFFFF !important;
        border-radius: 50% !important;
        padding: 10px !important;
        box-shadow: 0 6px 20px rgba(229, 9, 20, 0.6) !important;
        width: 55px !important;
        height: 55px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        z-index: 1000 !important;
        border: 2px solid rgba(255, 255, 255, 0.3) !important;
    }

    [data-testid="collapsedControl"]:hover {
        background-color: #F21120 !important;
        box-shadow: 0 8px 25px rgba(229, 9, 20, 0.8) !important;
        transform: scale(1.1) !important;
    }
    
    /* Also make the chevron svg icon white and visible */
    [data-testid="collapsedControl"] svg {
        fill: #FFFFFF !important;
        color: #FFFFFF !important;
        width: 32px !important;
        height: 32px !important;
    }

    /* Remove white corner borders from menu */
    .st-emotion-cache-1gulkj5, .st-emotion-cache-10oheav {
        border: none !important;
    }

    [data-testid="stSidebarNav"] > ul {
        padding: 0 !important;
    }

    [data-testid="stSidebarNav"] li {
        border-radius: 0 !important;
    }

    /* Additional selectors to catch all corner elements */
    [data-testid="stSidebarNav"] li::before,
    [data-testid="stSidebarNav"] li::after {
        display: none !important;
    }

    /* Target the nav-link corners specifically */
    .st-emotion-cache-1n76uvr, .st-emotion-cache-16tkqav {
        border: none !important;
    }

    /* Remove any box-shadow that might create white corners */
    [data-testid="stSidebarNav"] * {
        box-shadow: none !important;
    }

    .user-profile-label {
    color: #9CA3AF;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 1px;
    font-weight: 800;
    margin-bottom: 12px;
    text-align: center;
}

    .user-profile-name {
    color: #FFFFFF;
    font-size: 18px;
    font-weight: 700;
    line-height: 1.2;
    margin-bottom: 10px;
    text-align: center;
    }
    
    .user-profile-studio {
    color: #E50914;
    font-size: 14px;
    font-weight: 600;
    margin-bottom: 14px;
    text-align: center;
    }
    
    .user-profile-role {
    color: #60A5FA;
    font-size: 12px;
    font-weight: 500;
    font-style: italic;    
    margin-top: 4px;
    text-align: center;
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
    .stButton > button, div[data-testid="stFormSubmitButton"] > button, .stFormSubmitButton button {
        background: linear-gradient(90deg, #E50914 0%, #B20710 100%) !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 6px !important;
        font-weight: 600 !important;
        padding: 10px !important;
        box-shadow: 0 4px 12px rgba(229, 9, 20, 0.3) !important;
        width: 100% !important;
    }

    .stButton > button:hover, div[data-testid="stFormSubmitButton"] > button:hover, .stFormSubmitButton button:hover {
        background-color: #F21120 !important;
        background: linear-gradient(90deg, #F21120 0%, #C70813 100%) !important;
        box-shadow: 0 6px 16px rgba(229, 9, 20, 0.4) !important;
    }

    /* Style for buttons we want to hide but keep functional */
    .hidden-btn button {
        background-color: transparent !important;
        color: transparent !important;
        border: none !important;
        padding: 0 !important;
        height: 0 !important;
        min-height: 0 !important;
        margin: 0 !important;
        line-height: 0 !important;
        overflow: hidden !important;
        display: block !important;
    }

    /* Form Elements */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea, .stSelectbox>div>div>select {
        background-color: #242936 !important;
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

    /* Modal Overlay */
    .modal-overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: rgba(0, 0, 0, 0.85);
        z-index: 9999;
        display: flex;
        justify-content: center;
        align-items: flex-start;
        padding-top: 50px;
        overflow-y: auto;
    }
    .modal-content {
        background: #1A1D29;
        width: 90%;
        max-width: 1100px;
        border: 1px solid #2D3748;
        border-radius: 16px;
        padding: 40px;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
        margin-bottom: 50px;
    }
    # ============================================================================
    # ADDITIONAL CSS - ADD THIS TO YOUR EXISTING CSS SECTION
    # ============================================================================

    # Add these CSS classes to your existing st.markdown() section:

        /* Content Performance Card - Clickable */
        .content-perf-card {
            background: #242936;
            border: 2px solid #2D3748;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 15px;
            cursor: pointer;
            transition: all 0.2s ease;
        }

        .content-perf-card:hover {
            border-color: #E50914;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(229, 9, 20, 0.2);
        }

        /* Performance Badges */
        .perf-excellent { 
            background: rgba(16, 185, 129, 0.15); 
            color: #10B981; 
            padding: 6px 12px; 
            border-radius: 20px; 
            font-size: 11px; 
            font-weight: 700; 
        }
        .perf-good { 
            background: rgba(59, 130, 246, 0.15); 
            color: #3B82F6; 
            padding: 6px 12px; 
            border-radius: 20px; 
            font-size: 11px; 
            font-weight: 700; 
        }
        .perf-warning { 
            background: rgba(245, 158, 11, 0.15); 
            color: #FBBF24; 
            padding: 6px 12px; 
            border-radius: 20px; 
            font-size: 11px; 
            font-weight: 700; 
        }

        /* Chatbox Styling */
        .chat-message {
            padding: 12px 16px;
            border-radius: 12px;
            margin-bottom: 12px;
            max-width: 80%;
        }

        .user-message {
            background: #E50914;
            color: white;
            margin-left: auto;
        }

        .ai-message {
            background: #242936;
            border: 1px solid #2D3748;
            color: #E5E7EB;
        }
</style>
""",
            unsafe_allow_html=True)


# ============================================================================
# GROQ AI INTEGRATION
# ============================================================================
def generate_ai_pitch_variations(title, genre, brief_idea):
    """Generate 3 pitch variations using Groq API"""

    # Import here to avoid issues
    import urllib.request as url_request
    import json as json_module

    # Groq API endpoint
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY_2")

    if not GROQ_API_KEY:
        return {
            "error":
            "⚠️ GROQ_API_KEY not found! Please add it to Replit Secrets:\n1. Click 🔒 Secrets in left sidebar\n2. Key: GROQ_API_KEY\n3. Value: Your API key from console.groq.com\n4. Restart app",
            "variations": []
        }

    # Validate API key format
    if not GROQ_API_KEY.startswith("gsk_"):
        return {
            "error":
            f"⚠️ Invalid API key format. Groq keys start with 'gsk_'. Your key starts with '{GROQ_API_KEY[:10]}...'",
            "variations": []
        }

    prompt = f"""You are an expert entertainment pitch consultant working with major streaming platforms.

Given this basic concept:
Title: {title}
Genre: {genre}
Brief Idea: {brief_idea}

Generate 3 DISTINCT pitch variations. Each variation should feel different in tone and approach.

For EACH variation, provide:
1. Enhanced Logline (2-3 compelling sentences that hook the reader)
2. Key Characters (3 characters with names, roles, and 1-sentence descriptions)
3. Three-Act Structure (brief outline: Setup, Confrontation, Resolution)
4. Comparable Titles (3 successful shows/movies in similar vein)
5. Tagline (catchy one-liner for marketing)

Format your response as valid JSON:
{{
  "variations": [
    {{
      "variation_number": 1,
      "approach": "Brief description of this variation's unique angle",
      "logline": "...",
      "characters": ["Character 1: Name - Role - Description", "Character 2: ...", "Character 3: ..."],
      "three_act_structure": {{
        "act_1": "Setup description",
        "act_2": "Confrontation description",
        "act_3": "Resolution description"
      }},
      "comparables": ["Title 1", "Title 2", "Title 3"],
      "tagline": "..."
    }},
    ... (2 more variations)
  ]
}}

Make each variation creative, specific, and production-ready. Use different narrative approaches (e.g., character-driven vs plot-driven vs theme-driven)."""

    try:
        import requests
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            json={
                "model": "llama-3.1-8b-instant",
                "messages": [{
                    "role": "user",
                    "content": prompt
                }],
                "temperature": 0.8,
                "max_tokens": 3000,
                "response_format": {
                    "type": "json_object"
                }
            },
            headers={
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            },
            timeout=30)

        if response.status_code == 401:
            return {
                "error":
                "🚫 API Key Invalid (401). Get new key from console.groq.com/keys",
                "variations": []
            }
        elif response.status_code == 403:
            return {
                "error":
                "🚫 API Access Forbidden (403). Verify account is active.",
                "variations": []
            }
        elif response.status_code == 429:
            return {
                "error": "⏱️ Rate Limit Exceeded. Wait and try again.",
                "variations": []
            }
        elif response.status_code != 200:
            return {
                "error":
                f"API Error ({response.status_code}): {response.text}",
                "variations": []
            }

        result = response.json()
        content = result['choices'][0]['message']['content']
        return json.loads(content)

    except ImportError:
        return {
            "error": "⚠️ Install requests: pip install requests",
            "variations": []
        }
    except json.JSONDecodeError as e:
        return {"error": f"❌ JSON Parse Error: {str(e)}", "variations": []}
    except requests.exceptions.Timeout:
        return {"error": "⏱️ Request Timeout. Try again.", "variations": []}
    except requests.exceptions.ConnectionError:
        return {
            "error": "🌐 Connection Error. Check internet.",
            "variations": []
        }
    except Exception as e:
        return {"error": f"❌ {type(e).__name__}: {str(e)}", "variations": []}


def generate_ai_pitch_score(title, genre, logline, description, target_audience):
    """Generate AI-powered pitch score and feedback for Netflix executives"""

    GROQ_API_KEY = os.environ.get("GROQ_API_KEY_2")

    if not GROQ_API_KEY or not GROQ_API_KEY.startswith("gsk_"):
        return {
            "error": "API key not configured properly",
            "success_score": 0,
            "strengths": [],
            "concerns": [],
            "recommendation": "Unable to generate score"
        }

    prompt = f"""You are Netflix's AI content evaluation system. Analyze this pitch comprehensively.

PITCH DETAILS:
Title: {title}
Genre: {genre}
Logline: {logline if logline else 'Not provided'}
Synopsis: {description}
Target Audience: {target_audience}

Provide a detailed analysis in JSON format:
{{
  "success_score": <0-100 integer based on market potential, originality, audience appeal>,
  "score_breakdown": {{
    "market_fit": <0-100>,
    "originality": <0-100>,
    "audience_appeal": <0-100>,
    "production_feasibility": <0-100>
  }},
  "strengths": [
    "Specific strength 1",
    "Specific strength 2",
    "Specific strength 3"
  ],
  "concerns": [
    "Specific concern 1",
    "Specific concern 2",
    "Specific concern 3"
  ],
  "comparable_performance": {{
    "similar_titles": ["Title 1", "Title 2", "Title 3"],
    "avg_viewership": "estimated viewership based on comparables",
    "market_trend": "growing/stable/declining"
  }},
  "recommendation": "Greenlight / Greenlight with modifications / Request revision / Pass",
  "recommendation_details": "Detailed explanation of recommendation"
}}

Base your analysis on current streaming trends, genre performance, market saturation, audience demographics, and production viability."""

    try:
        import requests
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            json={
                "model": "llama-3.1-8b-instant",
                "messages": [{
                    "role": "user",
                    "content": prompt
                }],
                "temperature": 0.3,
                "max_tokens": 2000,
                "response_format": {
                    "type": "json_object"
                }
            },
            headers={
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            },
            timeout=30)

        if response.status_code == 400:
            error_detail = response.text
            return {
                "error": f"API request error (400): {error_detail[:200]}",
                "success_score": 0,
                "strengths": [],
                "concerns": [],
                "recommendation": "Error generating score"
            }
        elif response.status_code == 401:
            return {
                "error": "Invalid API key. Please check GROQ_API_KEY_2 in Secrets",
                "success_score": 0,
                "strengths": [],
                "concerns": [],
                "recommendation": "Error generating score"
            }
        elif response.status_code != 200:
            return {
                "error": f"API Error {response.status_code}: {response.text[:200]}",
                "success_score": 0,
                "strengths": [],
                "concerns": [],
                "recommendation": "Error generating score"
            }

        result = response.json()
        content = result['choices'][0]['message']['content']
        parsed_result = json.loads(content)
        return parsed_result

    except requests.exceptions.Timeout:
        return {
            "error": "Request timeout. Please try again.",
            "success_score": 0,
            "strengths": [],
            "concerns": [],
            "recommendation": "Error generating score"
        }
    except Exception as e:
        return {
            "error": f"Unexpected error: {str(e)[:200]}",
            "success_score": 0,
            "strengths": [],
            "concerns": [],
            "recommendation": "Error generating score"
        }

# ============================================================================
# AI ANALYTICS FUNCTIONS - ADD THESE AFTER generate_ai_pitch_score()
# ============================================================================

# ============================================================================
# REPLACE YOUR analytics_chatbot() FUNCTION WITH THIS
# ============================================================================

def analytics_chatbot(user_message, chat_history, user_role, analytics_data):
    """AI chatbot for analytics queries - confined to app data only"""
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY_2")

    if not GROQ_API_KEY or not GROQ_API_KEY.startswith("gsk_"):
        return "Chatbot unavailable - API key not configured"

    # Get actual content data to provide concrete facts
    content_perf = analytics_data.get('content_performance', {})

    # Build detailed content list
    content_details = []
    for cid, content in content_perf.items():
        content_details.append({
            'title': content.get('title'),
            'genre': content.get('genre'),
            'studio': content.get('studio'),
            'views': content.get('viewership_hours', 0),
            'completion': content.get('completion_rate', 0),
            'watch_time': content.get('avg_watch_time', 0),
            'region': content.get('top_region'),
            'age_group': content.get('top_age_group'),
            'trending': content.get('trending'),
            'performance': content.get('performance_badge')
        })

    # Sort by views to identify top performers
    top_content = sorted(content_details, key=lambda x: x['views'], reverse=True)

    # Calculate genre performance
    genre_stats = {}
    for content in content_details:
        genre = content['genre']
        if genre not in genre_stats:
            genre_stats[genre] = {'count': 0, 'total_views': 0, 'total_completion': 0}
        genre_stats[genre]['count'] += 1
        genre_stats[genre]['total_views'] += content['views']
        genre_stats[genre]['total_completion'] += content['completion']

    # Calculate averages
    for genre in genre_stats:
        stats = genre_stats[genre]
        stats['avg_views'] = stats['total_views'] / stats['count']
        stats['avg_completion'] = stats['total_completion'] / stats['count']

    # Build strict system context with ONLY app data
    system_context = f"""You are Netflix's Analytics AI Assistant. You can ONLY answer questions using the data provided below. DO NOT use any external knowledge or make assumptions.

**CRITICAL RULES:**
1. ONLY use the data provided in this context
2. If the answer is not in the provided data, say "I don't have that information in the current analytics data"
3. DO NOT make up numbers, trends, or information
4. DO NOT reference shows/content not in the list below
5. BE SPECIFIC - use exact numbers from the data

**AVAILABLE CONTENT DATA:**
"""

    # Add each content item with full details
    for idx, content in enumerate(top_content, 1):
        views_formatted = f"{content['views']/1000000:.1f}M" if content['views'] >= 1000000 else f"{content['views']/1000:.0f}K"
        system_context += f"""
{idx}. {content['title']}
   - Studio: {content['studio']}
   - Genre: {content['genre']}
   - Viewership: {views_formatted} hours ({content['views']} total)
   - Completion Rate: {content['completion']}%
   - Avg Watch Time: {content['watch_time']} minutes
   - Top Region: {content['region']}
   - Top Age Group: {content['age_group']}
   - Trending: {content['trending']}
   - Performance: {content['performance']}
"""

    # Add genre statistics
    system_context += "\n**GENRE PERFORMANCE:**\n"
    for genre, stats in sorted(genre_stats.items(), key=lambda x: x[1]['avg_views'], reverse=True):
        avg_views_formatted = f"{stats['avg_views']/1000000:.1f}M" if stats['avg_views'] >= 1000000 else f"{stats['avg_views']/1000:.0f}K"
        system_context += f"- {genre}: {stats['count']} titles, {avg_views_formatted} avg views, {stats['avg_completion']:.0f}% avg completion\n"

    # Add overall statistics
    total_views = sum(c['views'] for c in content_details)
    avg_completion = sum(c['completion'] for c in content_details) / len(content_details) if content_details else 0

    system_context += f"""
**OVERALL STATS:**
- Total Content: {len(content_details)} titles
- Total Viewership: {total_views/1000000:.1f}M hours
- Average Completion Rate: {avg_completion:.0f}%
- Studios: {', '.join(set(c['studio'] for c in content_details))}

**YOUR ROLE:**
- Answer questions ONLY using the data above
- Be concise (2-3 sentences max)
- Use exact numbers from the data
- If asked about content not listed above, say it's not in the current data
- If asked about future predictions or external trends, decline politely
"""

    # Build message history
    messages = [{"role": "system", "content": system_context}]

    # Add chat history (limited to last 3 exchanges)
    for msg in chat_history[-6:]:
        messages.append({"role": msg["role"], "content": msg["content"]})

    # Add current message
    messages.append({"role": "user", "content": user_message})

    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            json={
                "model": "llama-3.1-8b-instant",
                "messages": messages,
                "temperature": 0.1,  # LOWERED from 0.4 to reduce creativity/hallucination
                "max_tokens": 300,   # REDUCED from 400 to keep responses focused
                "top_p": 0.9,        # ADDED: Reduces randomness
            },
            headers={
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            },
            timeout=20)

        if response.status_code == 200:
            result = response.json()
            return result['choices'][0]['message']['content']
        else:
            return "I'm having trouble processing that request. Please try again."

    except Exception as e:
        return f"Error: {str(e)[:100]}"


# ============================================================================
# ALSO UPDATE generate_analytics_summary() FOR CONSISTENCY
# ============================================================================

def generate_analytics_summary(user_role, analytics_data):
    """Generate AI weekly summary - confined to app data only"""
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY_2")

    if not GROQ_API_KEY or not GROQ_API_KEY.startswith("gsk_"):
        return "AI summary unavailable - API key not configured"

    # Get actual content performance data
    content_perf = analytics_data.get('content_performance', {})

    # Calculate real metrics from data
    content_list = []
    total_views = 0
    total_completion = 0

    for cid, content in content_perf.items():
        content_list.append({
            'title': content.get('title'),
            'studio': content.get('studio'),
            'views': content.get('viewership_hours', 0),
            'completion': content.get('completion_rate', 0),
            'trending': content.get('trending')
        })
        total_views += content.get('viewership_hours', 0)
        total_completion += content.get('completion_rate', 0)

    avg_completion = total_completion / len(content_list) if content_list else 0

    # Sort by views to get top performers
    top_performers = sorted(content_list, key=lambda x: x['views'], reverse=True)[:3]

    # Identify trending content
    trending_up = [c['title'] for c in content_list if c['trending'] == 'up']
    trending_down = [c['title'] for c in content_list if c['trending'] == 'down']

    # Build context based on role with ACTUAL DATA
    if user_role == 'netflix_exec':
        context = f"""You are Netflix's AI analytics assistant. Summarize this week's portfolio performance using ONLY the data below:

**CONTENT OVERVIEW:**
- Total Active Content: {len(content_list)} titles
- Total Viewership: {total_views/1000000:.1f}M hours
- Average Completion Rate: {avg_completion:.0f}%

**TOP PERFORMERS:**
{chr(10).join([f"- {c['title']} ({c['studio']}): {c['views']/1000000:.1f}M views, {c['completion']}% completion" for c in top_performers[:3]])}

**TRENDING:**
- Trending Up: {', '.join(trending_up) if trending_up else 'None'}
- Trending Down: {', '.join(trending_down) if trending_down else 'None'}

Provide a 2-3 sentence executive summary highlighting key insights. Use ONLY the numbers provided above. Do NOT make up data."""

    else:
        # Studio-specific context
        studio_name = analytics_data.get('studio_name', 'your studio')
        studio_content = [c for c in content_list if c['studio'] == studio_name]

        if studio_content:
            studio_views = sum(c['views'] for c in studio_content)
            studio_completion = sum(c['completion'] for c in studio_content) / len(studio_content)
            top_title = max(studio_content, key=lambda x: x['views'])

            context = f"""You are Netflix's AI analytics assistant for studios. Summarize this week's performance using ONLY the data below:

**YOUR CONTENT:**
- Total Content: {len(studio_content)} titles
- Total Viewership: {studio_views/1000000:.1f}M hours
- Average Completion Rate: {studio_completion:.0f}%
- Top Performer: {top_title['title']} ({top_title['views']/1000000:.1f}M views)

**YOUR TRENDING:**
- Trending Up: {', '.join([c['title'] for c in studio_content if c['trending'] == 'up'])}
- Trending Down: {', '.join([c['title'] for c in studio_content if c['trending'] == 'down'])}

**PLATFORM AVERAGE:**
- Platform Avg Completion: {avg_completion:.0f}%

Provide a 2-3 sentence summary with actionable insights. Use ONLY the numbers provided above. Do NOT make up data."""
        else:
            return "No content data available for this studio."

    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            json={
                "model": "llama-3.1-8b-instant",
                "messages": [{"role": "user", "content": context}],
                "temperature": 0.2,  # LOWERED to reduce creativity
                "max_tokens": 250,
                "top_p": 0.9
            },
            headers={
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            },
            timeout=20)

        if response.status_code == 200:
            result = response.json()
            return result['choices'][0]['message']['content']
        else:
            return "Unable to generate summary at this time."

    except Exception as e:
        return f"Summary generation error: {str(e)[:100]}"


# ============================================================================
# DATA UTILITIES
# ============================================================================
def load_json(f):
    """Load JSON file with error handling for corrupted files"""
    if os.path.exists(f):
        try:
            with open(f, 'r') as file:
                content = file.read().strip()
                if content:
                    return json.loads(content)
                else:
                    # File is empty
                    return {}
        except (json.JSONDecodeError, ValueError) as e:
            # File is corrupted, delete it
            print(f"Warning: {f} is corrupted, recreating...")
            try:
                os.remove(f)
            except:
                pass
            return {}
        except Exception as e:
            print(f"Error loading {f}: {e}")
            return {}
    return {}


def save_json(f, d):
    with open(f, 'w') as file:
        json.dump(d, file, indent=2)


def hash_txt(t):
    return hashlib.sha256(t.encode()).hexdigest()

# ============================================================================
# HELPER FUNCTION - ADD THIS NEW FUNCTION
# ============================================================================

def filter_by_studio(data_dict, studio_name):
    """Filter data dictionary by studio name. Returns filtered dict."""
    if studio_name == "All Studios":
        return data_dict
    return {k: v for k, v in data_dict.items() if v.get('studio') == studio_name}


def get_studio_options(user_role, current_studio=None):
    """Get studio filter options based on user role"""
    if user_role == 'netflix_exec':
        return ["All Studios", "Phoenix Studios", "Meridian Pictures"]
    else:
        # Studio users only see their own studio
        return [current_studio] if current_studio else []

def top_header():
    # Empty header - search bar removed
    st.markdown("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)


# ============================================================================
# DASHBOARD
# ============================================================================
# ============================================================================
# UPDATED DASHBOARD - REPLACE YOUR screen_dashboard() FUNCTION
# ============================================================================

def screen_dashboard():
    top_header()

    # Get user info
    user_role = st.session_state.get('current_user_role', 'studio')
    current_studio = st.session_state.user.get('studio', '')
    is_netflix_exec = (user_role == 'netflix_exec')

    # Studio filter for Netflix exec
    if is_netflix_exec:
        col_title, col_filter = st.columns([3, 1])
        with col_title:
            st.markdown("<h1>Dashboard</h1>", unsafe_allow_html=True)
        with col_filter:
            studio_filter = st.selectbox(
                "Studio Filter",
                get_studio_options(user_role),
                key="dashboard_studio_filter",
                label_visibility="collapsed"
            )
    else:
        st.markdown("<h1>Dashboard</h1>", unsafe_allow_html=True)
        studio_filter = current_studio

    st.markdown("<p class='subtitle'>Welcome back! Here's an overview of studio activity.</p>", unsafe_allow_html=True)

    # Load and filter data
    projects = load_json('projects.json')
    pitches = load_json('pitches.json')

    if studio_filter != "All Studios":
        projects = filter_by_studio(projects, studio_filter)
        pitches = filter_by_studio(pitches, studio_filter)

    # Calculate metrics
    active_pitches = len(pitches)
    in_production = len(projects)

    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown(
            f"<div class='ui-card'><p class='metric-title'>Active Pitches</p><div class='metric-value'>{active_pitches}</div><p class='metric-delta delta-up'>+2 this month</p></div>",
            unsafe_allow_html=True)
    with m2:
        st.markdown(
            f"<div class='ui-card'><p class='metric-title'>In Production</p><div class='metric-value'>{in_production}</div><p class='metric-delta'>On schedule</p></div>",
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

        if projects:
            for pid, p in projects.items():
                st.markdown(f"""
                <div class='ui-card'>
                    <div style='display:flex; justify-content:space-between; align-items:start;'>
                        <div>
                            <b style='font-size:16px;'>{p.get('name')}</b>
                            <br><small style='color:#9CA3AF;'>{p.get('phase')}</small>
                            <br><small style='color:#6B7280;'>{p.get('studio')}</small>
                        </div>
                        <span class='badge badge-blue'>In Production</span>
                    </div>
                    <div class='progress-track'><div class='progress-fill' style='width:{p.get('progress')}%'></div></div>
                    <div style='display:flex; justify-content:space-between; font-size:12px;'>
                        <span>Due: {p.get('due')}</span><span>{p.get('progress')}%</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No active projects")

    with col_right:
        st.markdown("<h3>Recent Activity</h3>", unsafe_allow_html=True)
        st.markdown("""
        <div class='ui-card'>
            <div style='margin-bottom:15px;'>
                <span class='badge badge-green'>Success</span> <span style='font-size:13px; color:#E5E7EB;'>Pitch 'Midnight Chronicles' approved</span><br>
                <small style='color:#6B7280;'>2 hours ago</small>
            </div>
            <div style='margin-bottom:15px;'>
                <span class='badge badge-blue'>Info</span> <span style='font-size:13px; color:#E5E7EB;'>New feedback on 'Desert Storm' pilot</span><br>
                <small style='color:#6B7280;'>5 hours ago</small>
            </div>
            <div>
                <span class='badge badge-green'>Success</span> <span style='font-size:13px; color:#E5E7EB;'>'Ocean's Edge' Episode 3 delivered</span><br>
                <small style='color:#6B7280;'>1 day ago</small>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ============================================================================
# PITCH PORTAL
# ============================================================================
# ============================================================================
# COMPLETE PITCH PORTAL - REPLACE YOUR ENTIRE screen_pitches() FUNCTION
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

    .pitch-clickable-card {
        cursor: pointer;
        transition: all 0.2s ease;
        margin-bottom: 15px;
    }
    .pitch-clickable-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(229, 9, 20, 0.2);
    }
    </style>
    """, unsafe_allow_html=True)

    # Initialize modal state FIRST
    if 'show_new_pitch_modal' not in st.session_state:
        st.session_state.show_new_pitch_modal = False

    # Initialize AI state for dialog context
    if 'ai_variations' not in st.session_state:
        st.session_state.ai_variations = None
    if 'ai_generating' not in st.session_state:
        st.session_state.ai_generating = False
    if 'selected_variation' not in st.session_state:
        st.session_state.selected_variation = None

    # Check user role - STORE IN SESSION STATE so it's available everywhere
    if 'current_user_role' not in st.session_state:
        st.session_state.current_user_role = st.session_state.user.get('role', 'studio')

    user_role = st.session_state.current_user_role
    current_studio = st.session_state.user.get('studio', '')
    is_netflix_exec = (user_role == 'netflix_exec')
    is_studio_user = not is_netflix_exec

    # Header with Studio Filter and New Pitch button
    if is_netflix_exec:
        # Netflix exec gets filter dropdown
        col_title, col_filter = st.columns([3, 1])
        with col_title:
            st.markdown(
                "<h1>Pitch Portal</h1><p class='subtitle'>Submit new pitches and track their progress through Netflix's review process.</p>",
                unsafe_allow_html=True)
        with col_filter:
            studio_filter = st.selectbox(
                "Studio Filter",
                get_studio_options(user_role),
                key="pitch_studio_filter",
                label_visibility="collapsed"
            )
    else:
        # Studio users get New Pitch button
        col_header = st.columns([4, 1])
        with col_header[0]:
            st.markdown(
                "<h1>Pitch Portal</h1><p class='subtitle'>Submit new pitches and track their progress through Netflix's review process.</p>",
                unsafe_allow_html=True)
        with col_header[1]:
            if st.button("➕ New Pitch", key="new_pitch_btn_main"):
                st.session_state.show_new_pitch_modal = True
                st.rerun()
        studio_filter = current_studio

    @st.dialog("Submit New Pitch", width="large")
    def show_pitch_dialog():
        # Decorative header
        st.markdown("""
        <div style='text-align: center; margin-bottom: 20px;'>
            <div style='font-size: 40px; margin-bottom: 5px;'>🎬</div>
            <p style='color: #9CA3AF; font-size: 14px;'>Share your creative vision with Netflix</p>
        </div>
        """, unsafe_allow_html=True)

        # Two-column layout: AI Generator | Manual Form
        ai_col, spacer, form_col = st.columns([1.5, 0.1, 1.5])

        # LEFT: AI Pitch Generator
        with ai_col:
            st.markdown("### ✨ AI Pitch Generator")
            st.markdown(
                "<p style='color: #9CA3AF; font-size: 13px;'>Get AI-powered pitch ideas in seconds</p>",
                unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)

            with st.form("ai_generator_form"):
                ai_title = st.text_input(
                    "Basic Title Idea",
                    placeholder="e.g., Dark Mystery Series")
                ai_genre = st.selectbox("Genre", [
                    "Sci-Fi Thriller", "Drama", "Comedy", "Action",
                    "Horror", "Documentary", "Romance", "Adventure",
                    "Psychological Thriller", "Mystery"
                ])
                ai_brief = st.text_area(
                    "Brief Concept (2-3 sentences)",
                    placeholder="Describe your core idea...",
                    height=100)

                generate_btn = st.form_submit_button(
                    "🚀 Generate AI Variations", use_container_width=True)

                if generate_btn:
                    if ai_title and ai_brief:
                        st.session_state.ai_generating = True
                        with st.spinner(
                                "🎨 AI is crafting pitch variations..."):
                            result = generate_ai_pitch_variations(
                                ai_title, ai_genre, ai_brief)
                            st.session_state.ai_variations = result
                            st.session_state.ai_generating = False
                        st.rerun()
                    else:
                        st.error("Please provide title and brief concept")

            # Display AI variations
            if st.session_state.ai_variations:
                st.markdown("<br>", unsafe_allow_html=True)

                if 'error' in st.session_state.ai_variations:
                    st.error(st.session_state.ai_variations['error'])
                elif st.session_state.ai_variations.get('variations'):
                    st.markdown("#### 📋 AI Generated Variations")

                    for i, var in enumerate(
                            st.session_state.ai_variations['variations'],
                            1):
                        with st.expander(
                                f"Variation {i}: {var.get('approach', 'Option ' + str(i))}",
                                expanded=(i == 1)):
                            st.markdown(
                                f"**Logline:** {var.get('logline', '')}")
                            st.markdown(
                                f"**Tagline:** *{var.get('tagline', '')}*")
                            st.markdown(
                                f"**Comparables:** {', '.join(var.get('comparables', []))}"
                            )

                            if st.button(f"✓ Use This Variation",
                                         key=f"use_var_{i}"):
                                st.session_state.selected_variation = var
                                st.success(
                                    f"✓ Variation {i} selected! Fill the form on the right →"
                                )

        # RIGHT: Manual Form
        with form_col:
            st.markdown("### 📝 Pitch Details")
            st.markdown(
                "<p style='color: #9CA3AF; font-size: 13px;'>Fill manually or use AI-generated content</p>",
                unsafe_allow_html=True)

            # Pre-fill if variation selected
            default_title = ""
            default_logline = ""
            default_synopsis = ""

            if st.session_state.selected_variation:
                var = st.session_state.selected_variation
                default_title = var.get(
                    'logline',
                    '').split('.')[0][:50]  # First sentence as title
                default_logline = var.get('logline', '')

                # Build synopsis from all parts
                chars = '\n'.join(var.get('characters', []))
                acts = var.get('three_act_structure', {})
                default_synopsis = f"{default_logline}\n\nCHARACTERS:\n{chars}\n\nSTRUCTURE:\nAct 1: {acts.get('act_1', '')}\nAct 2: {acts.get('act_2', '')}\nAct 3: {acts.get('act_3', '')}"

            with st.form("pitch_submission_form"):
                title = st.text_input(
                    "Project Title *",
                    value=default_title,
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
                    value=default_logline,
                    placeholder=
                    "One compelling sentence that captures your story",
                    height=80)
                synopsis = st.text_area(
                    "Synopsis *",
                    value=default_synopsis,
                    placeholder=
                    "Detailed description of story, characters, and narrative",
                    height=200)

                st.markdown("<br>", unsafe_allow_html=True)

                # Form buttons
                submit_col1, submit_col2 = st.columns([1, 1])
                with submit_col1:
                    submitted = st.form_submit_button("Submit Pitch", use_container_width=True)
                with submit_col2:
                    cancelled = st.form_submit_button("Cancel", use_container_width=True)

                if submitted:
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
                            "submitted":
                            datetime.now().strftime("%b %d, %Y"),
                            "days_ago": "Just now"
                        }
                        save_json('pitches.json', pitches)
                        st.session_state.show_new_pitch_modal = False
                        st.session_state.ai_variations = None
                        st.session_state.selected_variation = None
                        st.session_state.sel_p = new_id
                        st.success("✅ Pitch submitted successfully!")
                        st.rerun()
                    else:
                        st.error("Please fill in all required fields marked with *")

                if cancelled:
                    st.session_state.show_new_pitch_modal = False
                    st.rerun()

    # New Pitch Modal Trigger (only for studio users)
    if st.session_state.show_new_pitch_modal and is_studio_user:
        show_pitch_dialog()

    st.markdown("---")

    # Main content - Two columns
    col1, col2 = st.columns([1.2, 2.3])

    # Load and filter pitches
    pitches = load_json('pitches.json')
    if studio_filter != "All Studios":
        pitches = filter_by_studio(pitches, studio_filter)

    # Allow selecting a pitch via query param (used by clickable HTML cards)
    try:
        qp_sel = st.query_params.get("sel_p")
    except Exception:
        qp_sel = st.experimental_get_query_params().get("sel_p", [None])[0]
    if qp_sel:
        qp_sel = str(qp_sel)
        if qp_sel in pitches:
            st.session_state.sel_p = qp_sel

    # Initialize selection to first pitch if not set; fix stale selection when filter changes
    if not pitches:
        st.session_state.sel_p = None
    elif 'sel_p' not in st.session_state or st.session_state.sel_p not in pitches:
        st.session_state.sel_p = next(iter(pitches))

    # Status badge helper
    def get_status_badge(status):
        if status == "Under Review": return "badge-yellow"
        elif status == "Approved": return "badge-green"
        elif status == "Feedback Received": return "badge-blue"
        else: return "badge-yellow"

    # Left Column - Pitch List
    with col1:
        # Apply custom CSS for this column
        st.markdown("""
        <style>
        div[data-testid="column"]:first-child > div {
            background: #13161F !important;
            border: 1px solid #6B7280 !important;
            border-radius: 12px !important;
            padding: 20px !important;
            min-height: 700px !important;
        }

        /* Pitch list as Streamlit buttons styled like cards (no navigation => no logout) */
        div[data-testid="column"]:first-child button[data-testid^="baseButton-"] {
            background: transparent !important;
            background-color: transparent !important;
            background-image: none !important;
            border: 2px solid #4A5568 !important;
            border-radius: 10px !important;
            padding: 14px 16px !important;
            width: 100% !important;
            height: auto !important;
            text-align: left !important;
            transition: all 0.18s ease !important;
            box-shadow: none !important;
        }

        div[data-testid="column"]:first-child button[data-testid^="baseButton-"]:hover {
            border-color: #E50914 !important;
            transform: translateY(-2px) !important;
            box-shadow: 0 4px 12px rgba(229, 9, 20, 0.18) !important;
        }

        /* Selected: red border only (no red fill) */
        div[data-testid="column"]:first-child button[data-testid="baseButton-primary"] {
            background: transparent !important;
            background-color: transparent !important;
            border-color: #E50914 !important;
            box-shadow: none !important;
            transform: none !important;
        }

        /* Ensure multiline label layout + readable text */
        div[data-testid="column"]:first-child button[data-testid^="baseButton-"] * {
            white-space: pre-line !important;
        }

        div[data-testid="column"]:first-child button[data-testid^="baseButton-"] span {
            color: #E5E7EB !important;
            line-height: 1.25 !important;
            text-align: left !important;
        }
        </style>
        """, unsafe_allow_html=True)

        st.markdown("<h3 style='margin: 0 0 20px 0;'>Your Pitches</h3>",
                    unsafe_allow_html=True)

        if pitches:
            for pid, p in pitches.items():
                selected = (st.session_state.get('sel_p') == pid)
                status = p.get('status', "Under Review")
                days_ago = str(p.get('days_ago', "Recently"))

                title_txt = p.get('title', '')
                genre_txt = p.get('genre', '')
                label = f"{title_txt}\n{genre_txt}\n🕒 {days_ago}   •   {status}"

                if st.button(
                    label,
                    key=f"pitch_select_{pid}",
                    help=f"Click to view {title_txt}",
                    type=("primary" if selected else "secondary"),
                    use_container_width=True,
                ):
                    st.session_state.sel_p = pid
                    st.rerun()

    # Right Column - Pitch Details
    with col2:
        sid = st.session_state.get('sel_p')
        if sid and sid in pitches:
            p = pitches[sid]
            status = p.get('status', "Under Review")
            badge_class = get_status_badge(status)
            submitted_date = p.get('submitted', 'Nov 1, 2024')
            title = p.get('title', '')
            genre = p.get('genre', '')
            description = p.get('description', '')
            logline = p.get('logline', '')
            target = p.get('target', 'Adults 18-49')

            # Get user role from session state
            current_user_role = st.session_state.current_user_role
            is_netflix_exec_here = (current_user_role == 'netflix_exec')

            # Display pitch header
            st.markdown(f"""
            <div style='margin-bottom: 20px;'>
                <div style='display:flex; justify-content:space-between; align-items: start;'>
                    <div>
                        <h2 style='margin: 0; font-size: 28px; color: #FFFFFF;'>{title}</h2>
                        <p style='color: #9CA3AF; font-size: 14px; margin-top: 5px;'>{genre}</p>
                    </div>
                    <span class='badge {badge_class}'>{status}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

            # AI PITCH SCORING - NETFLIX EXEC ONLY
            if is_netflix_exec_here:
                st.markdown("---")
                st.markdown("### 🤖 AI Pitch Analysis")
                st.write("Get AI-powered insights on this pitch's market potential and success probability")

                # Initialize scoring state
                score_key = f"ai_score_{sid}"
                if score_key not in st.session_state:
                    st.session_state[score_key] = None

                # Display results if they exist
                if st.session_state[score_key]:
                    score_data = st.session_state[score_key]

                    # Refresh button at top
                    if st.button("🔄 Regenerate Analysis", key=f"refresh_ai_{sid}"):
                        st.session_state[score_key] = None
                        st.rerun()

                    if 'error' in score_data and score_data.get('error'):
                        st.error(f"⚠️ Error: {score_data['error']}")
                    else:
                        success_score = score_data.get('success_score', 0)

                        # Score color coding
                        if success_score >= 75:
                            score_color = "#10B981"
                            score_label = "High Potential"
                        elif success_score >= 50:
                            score_color = "#FBBF24"
                            score_label = "Moderate Potential"
                        else:
                            score_color = "#EF4444"
                            score_label = "Low Potential"

                        # Main Score Display
                        st.markdown(f"""
                        <div style='background: linear-gradient(135deg, #1A1F2E 0%, #13161F 100%); 
                                    border: 2px solid {score_color}; 
                                    border-radius: 12px; 
                                    padding: 25px; 
                                    text-align: center; 
                                    margin: 20px 0;'>
                            <div style='font-size: 14px; color: #9CA3AF; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px;'>
                                AI Success Score
                            </div>
                            <div style='font-size: 56px; font-weight: 700; color: {score_color}; margin: 10px 0;'>
                                {success_score}
                            </div>
                            <div style='font-size: 16px; color: {score_color}; font-weight: 600;'>
                                {score_label}
                            </div>
                        </div>
                        """, unsafe_allow_html=True)

                        # Score Breakdown
                        if 'score_breakdown' in score_data:
                            breakdown = score_data['score_breakdown']
                            st.markdown("##### Score Breakdown")

                            cols_breakdown = st.columns(4)
                            metrics = [
                                ("Market Fit", breakdown.get('market_fit', 0)),
                                ("Originality", breakdown.get('originality', 0)),
                                ("Audience Appeal", breakdown.get('audience_appeal', 0)),
                                ("Feasibility", breakdown.get('production_feasibility', 0))
                            ]

                            for idx, (label, value) in enumerate(metrics):
                                with cols_breakdown[idx]:
                                    st.markdown(f"""
                                    <div style='background: #1A1F2E; padding: 15px; border-radius: 8px; text-align: center;'>
                                        <div style='color: #9CA3AF; font-size: 11px; margin-bottom: 5px;'>{label}</div>
                                        <div style='font-size: 24px; font-weight: 700; color: #FFFFFF;'>{value}</div>
                                    </div>
                                    """, unsafe_allow_html=True)

                        # Strengths
                        if score_data.get('strengths'):
                            st.markdown("##### ✅ Strengths")
                            strengths_html = "<ul style='color: #10B981; padding-left: 20px; margin: 10px 0;'>"
                            for strength in score_data['strengths']:
                                strengths_html += f"<li style='margin: 8px 0; line-height: 1.6;'>{strength}</li>"
                            strengths_html += "</ul>"
                            st.markdown(strengths_html, unsafe_allow_html=True)

                        # Concerns
                        if score_data.get('concerns'):
                            st.markdown("##### ⚠️ Concerns")
                            concerns_html = "<ul style='color: #FBBF24; padding-left: 20px; margin: 10px 0;'>"
                            for concern in score_data['concerns']:
                                concerns_html += f"<li style='margin: 8px 0; line-height: 1.6;'>{concern}</li>"
                            concerns_html += "</ul>"
                            st.markdown(concerns_html, unsafe_allow_html=True)

                        # Comparable Performance
                        if 'comparable_performance' in score_data:
                            comp = score_data['comparable_performance']
                            st.markdown("##### 📊 Comparable Performance")

                            st.markdown(f"""
                            <div style='background: #1A1F2E; border-radius: 8px; padding: 15px; margin: 10px 0;'>
                                <div style='margin-bottom: 10px;'>
                                    <span style='color: #9CA3AF; font-size: 13px;'>Similar Titles:</span><br>
                                    <span style='color: #FFFFFF; font-size: 14px;'>{', '.join(comp.get('similar_titles', []))}</span>
                                </div>
                                <div style='margin-bottom: 10px;'>
                                    <span style='color: #9CA3AF; font-size: 13px;'>Avg. Viewership:</span><br>
                                    <span style='color: #FFFFFF; font-size: 14px;'>{comp.get('avg_viewership', 'N/A')}</span>
                                </div>
                                <div>
                                    <span style='color: #9CA3AF; font-size: 13px;'>Market Trend:</span><br>
                                    <span style='color: #FFFFFF; font-size: 14px; text-transform: capitalize;'>{comp.get('market_trend', 'N/A')}</span>
                                </div>
                            </div>
                            """, unsafe_allow_html=True)

                        # Recommendation
                        st.markdown("##### 💡 Recommendation")
                        recommendation = score_data.get('recommendation', 'N/A')
                        rec_details = score_data.get('recommendation_details', '')

                        # Recommendation color coding
                        if 'Greenlight' in recommendation and 'modifications' not in recommendation:
                            rec_color = "#10B981"
                            rec_icon = "✅"
                        elif 'modifications' in recommendation:
                            rec_color = "#3B82F6"
                            rec_icon = "🔧"
                        elif 'revision' in recommendation:
                            rec_color = "#FBBF24"
                            rec_icon = "📝"
                        else:
                            rec_color = "#EF4444"
                            rec_icon = "❌"

                        st.markdown(f"""
                        <div style='background: linear-gradient(135deg, #1A1F2E 0%, #13161F 100%); 
                                    border-left: 4px solid {rec_color}; 
                                    border-radius: 8px; 
                                    padding: 20px; 
                                    margin: 15px 0;'>
                            <div style='font-size: 18px; font-weight: 600; color: {rec_color}; margin-bottom: 10px;'>
                                {rec_icon} {recommendation}
                            </div>
                            <div style='color: #D1D5DB; font-size: 14px; line-height: 1.7;'>
                                {rec_details}
                            </div>
                        </div>
                        """, unsafe_allow_html=True)

                else:
                    # Button to generate score (only show if no results)
                    if st.button("🎯 Generate AI Score & Feedback", 
                                key=f"gen_ai_score_{sid}", 
                                type="primary",
                                use_container_width=True):
                        with st.spinner("🤖 AI analyzing pitch..."):
                            score_result = generate_ai_pitch_score(
                                title, genre, logline, description, target
                            )
                            st.session_state[score_key] = score_result
                            st.rerun()

            # Original content continues
            st.markdown("---")
            st.markdown("### Review Timeline")

            st.markdown(f"""
            <div style='margin-bottom: 20px;'>
                <div style='display: flex; align-items: center; margin-bottom: 15px;'>
                    <div style='width: 12px; height: 12px; background: #10B981; border-radius: 50%; margin-right: 15px;'></div>
                    <div>
                        <b style='color: #FFFFFF; font-size: 15px;'>Submitted</b><br>
                        <small style='color: #9CA3AF;'>{submitted_date}</small>
                    </div>
                </div>
                <div style='border-left: 2px solid #4A5568; margin-left: 5px; padding-left: 22px; margin-bottom: 15px;'>
                    <div style='display: flex; align-items: center; margin-top: -5px;'>
                        <div style='width: 12px; height: 12px; background: #3B82F6; border-radius: 50%; margin-right: 15px; margin-left: -28px;'></div>
                        <div>
                            <b style='color: #FFFFFF; font-size: 15px;'>Treatment Review</b><br>
                            <small style='color: #9CA3AF;'>In progress</small>
                        </div>
                    </div>
                </div>
                <div style='border-left: 2px solid #4A5568; margin-left: 5px; padding-left: 22px;'>
                    <div style='display: flex; align-items: center; margin-top: -5px;'>
                        <div style='width: 12px; height: 12px; background: #4B5563; border-radius: 50%; margin-right: 15px; margin-left: -28px;'></div>
                        <div>
                            <b style='color: #6B7280; font-size: 15px;'>Decision</b><br>
                            <small style='color: #6B7280;'>Pending</small>
                        </div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("---")
            st.markdown("### Synopsis")
            st.markdown(f"<p style='font-size: 14px; line-height: 1.8; color: #D1D5DB;'>{description}</p>", unsafe_allow_html=True)

            col_btn1, col_btn2 = st.columns(2)
            with col_btn1:
                st.button("👁 View Full Pitch", key=f"view_{sid}", use_container_width=True)
            with col_btn2:
                st.button("💬 Message Netflix Team", key=f"msg_{sid}", use_container_width=True)
        else:
            if not pitches:
                st.info("No pitches to display. Submit a new pitch or adjust the studio filter.")
            else:
                st.info("Select a pitch from the list to view details.")


# ============================================================================
# PRODUCTION SUITE
# ============================================================================
# ============================================================================
# UPDATED PRODUCTION - REPLACE YOUR screen_production() FUNCTION
# ============================================================================

def screen_production():
    top_header()

    # Get user info
    user_role = st.session_state.get('current_user_role', 'studio')
    current_studio = st.session_state.user.get('studio', '')
    is_netflix_exec = (user_role == 'netflix_exec')

    # Studio filter for Netflix exec
    if is_netflix_exec:
        col_title, col_filter = st.columns([3, 1])
        with col_title:
            st.markdown("<h1>Production Suite</h1>", unsafe_allow_html=True)
        with col_filter:
            studio_filter = st.selectbox(
                "Studio Filter",
                get_studio_options(user_role),
                key="production_studio_filter",
                label_visibility="collapsed"
            )
    else:
        st.markdown("<h1>Production Suite</h1>", unsafe_allow_html=True)
        studio_filter = current_studio

    st.markdown("<p class='subtitle'>Manage active productions and track deliverables.</p>", unsafe_allow_html=True)

    # Load and filter projects
    projects = load_json('projects.json')
    if studio_filter != "All Studios":
        projects = filter_by_studio(projects, studio_filter)

    if not projects:
        st.info(f"No active projects for {studio_filter}")
        return

    # Get first project
    p = list(projects.values())[0]

    c1, c2, c3 = st.columns([1.5, 1.5, 1])
    with c1:
        st.markdown(f"""
        <div class='ui-card' style='height:280px;'>
            <div style='display:flex; justify-content:space-between;'>
                <div>
                    <h3>{p.get('name', 'Project')}</h3>
                    <small style='color:#9CA3AF;'>{p.get('studio')}</small>
                </div>
                <span class='badge badge-blue'>In Production</span>
            </div>
            <p style='font-size:13px; margin-top:20px;'>Overall Progress</p>
            <div class='progress-track'><div class='progress-fill' style='width:{p.get('progress', 0)}%'></div></div>
            <p style='text-align:right; font-weight:700;'>{p.get('progress', 0)}%</p>
            <br>
            <button style='width:100%; background:#E50914; border:none; color:white; padding:10px; border-radius:6px; font-weight:600;'>⬆ Upload Deliverable</button>
        </div>
        """, unsafe_allow_html=True)

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
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class='ui-card' style='height:280px;'>
            <h3>Quick Stats</h3>
            <p style='font-size:14px; margin-top:25px;'>Episodes Completed <span style='float:right; color:white;'>2/8</span></p>
            <p style='font-size:14px;'>Days Until Milestone <span style='float:right; color:white;'>6</span></p>
            <p style='font-size:14px;'>Open Issues <span style='float:right; color:#FBBF24;'>3</span></p>
        </div>
        """, unsafe_allow_html=True)

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
    """, unsafe_allow_html=True)



# ============================================================================
# HELPER FUNCTION - ADD THIS BEFORE screen_analytics()
# ============================================================================

def get_analytics_data():
    """Load or generate analytics mock data"""
    if not os.path.exists('analytics_data.json'):
        # Generate initial mock data
        analytics_data = {
            "content_performance": {
                "1": {
                    "title": "Midnight Chronicles",
                    "genre": "Sci-Fi Thriller",
                    "studio": "Phoenix Studios",
                    "viewership_hours": 8200000,
                    "completion_rate": 87,
                    "avg_watch_time": 42,
                    "top_region": "United States",
                    "top_age_group": "25-34",
                    "trending": "up",
                    "performance_badge": "excellent"
                },
                "2": {
                    "title": "The Last Horizon",
                    "genre": "Drama",
                    "studio": "Phoenix Studios",
                    "viewership_hours": 12500000,
                    "completion_rate": 91,
                    "avg_watch_time": 48,
                    "top_region": "United Kingdom",
                    "top_age_group": "35-44",
                    "trending": "up",
                    "performance_badge": "excellent"
                },
                "3": {
                    "title": "Echo Chamber",
                    "genre": "Psychological Thriller",
                    "studio": "Phoenix Studios",
                    "viewership_hours": 6800000,
                    "completion_rate": 78,
                    "avg_watch_time": 38,
                    "top_region": "Canada",
                    "top_age_group": "18-24",
                    "trending": "stable",
                    "performance_badge": "good"
                },
                "4": {
                    "title": "Starlight Runners",
                    "genre": "Adventure",
                    "studio": "Phoenix Studios",
                    "viewership_hours": 5200000,
                    "completion_rate": 65,
                    "avg_watch_time": 35,
                    "top_region": "Australia",
                    "top_age_group": "18-24",
                    "trending": "down",
                    "performance_badge": "warning"
                }
            }
        }
        save_json('analytics_data.json', analytics_data)
        return analytics_data
    else:
        return load_json('analytics_data.json')



# ============================================================================
# ANALYTICS HUB
# ============================================================================
# ============================================================================
# NEW ANALYTICS HUB - REPLACE YOUR screen_analytics() FUNCTION WITH THIS
# ============================================================================
# ============================================================================
# UPDATED ANALYTICS - REPLACE BEGINNING OF screen_analytics()
# ============================================================================

# ============================================================================
# FIXED screen_analytics() - REPLACE YOUR ENTIRE FUNCTION
# ============================================================================

def screen_analytics():
    """Enhanced Analytics Hub with studio filtering - FIXED VERSION"""
    top_header()

    # Get analytics mock data
    analytics_data = get_analytics_data()

    # Get user role
    user_role = st.session_state.get('current_user_role', 'studio')
    current_studio = st.session_state.user.get('studio', '')
    is_netflix_exec = (user_role == 'netflix_exec')

    # Studio filter for Netflix exec
    if is_netflix_exec:
        col_title, col_filter = st.columns([3, 1])
        with col_title:
            st.markdown("<h1>Analytics Hub</h1>", unsafe_allow_html=True)
        with col_filter:
            studio_filter = st.selectbox(
                "Studio Filter",
                get_studio_options(user_role),
                key="analytics_studio_filter",
                label_visibility="collapsed"
            )
    else:
        st.markdown("<h1>Analytics Hub</h1>", unsafe_allow_html=True)
        studio_filter = current_studio

    st.markdown("<p class='subtitle'>Track the performance of your content on Netflix.</p>", unsafe_allow_html=True)

    # Initialize chatbot history
    if 'analytics_chat_history' not in st.session_state:
        st.session_state.analytics_chat_history = []

    # *** FIX: Filter content performance data CORRECTLY ***
    all_content_perf = analytics_data.get('content_performance', {})

    # Apply filter based on studio_filter value
    if studio_filter == "All Studios":
        content_perf = all_content_perf
    else:
        # Filter to show only the selected studio's content
        content_perf = {
            cid: content for cid, content in all_content_perf.items() 
            if content.get('studio') == studio_filter
        }

    # Debug: Show what's being filtered (you can remove this later)
    # st.write(f"DEBUG - Studio Filter: {studio_filter}, Content Count: {len(content_perf)}")

    # Calculate filtered metrics
    if content_perf:
        total_views = sum(c.get('viewership_hours', 0) for c in content_perf.values())
        avg_completion = sum(c.get('completion_rate', 0) for c in content_perf.values()) / len(content_perf)
        content_count = len(content_perf)
    else:
        total_views = 0
        avg_completion = 0
        content_count = 0

    # ========== SECTION 1: TOP METRICS ==========
    if is_netflix_exec:
        # Netflix Executive View
        m1, m2, m3, m4 = st.columns(4)
        with m1:
            st.markdown(
                f"<div class='ui-card'><p class='metric-title'>Total Active Content</p><div class='metric-value'>{content_count}</div><p class='metric-delta'>{studio_filter}</p></div>",
                unsafe_allow_html=True)
        with m2:
            st.markdown(
                "<div class='ui-card'><p class='metric-title'>Platform Health Score</p><div class='metric-value'>84</div><p class='metric-delta delta-up'>+3 vs last week</p></div>",
                unsafe_allow_html=True)
        with m3:
            views_display = f"{total_views / 1000000:.1f}M" if total_views >= 1000000 else f"{total_views / 1000:.0f}K"
            st.markdown(
                f"<div class='ui-card'><p class='metric-title'>Total Hours Viewed</p><div class='metric-value'>{views_display}</div><p class='metric-delta delta-up'>+8.2% this week</p></div>",
                unsafe_allow_html=True)
        with m4:
            st.markdown(
                f"<div class='ui-card'><p class='metric-title'>Avg Completion Rate</p><div class='metric-value'>{avg_completion:.0f}%</div><p class='metric-delta delta-up'>+2.1% vs last week</p></div>",
                unsafe_allow_html=True)
    else:
        # Studio Executive View  
        m1, m2, m3, m4 = st.columns(4)
        with m1:
            st.markdown(
                f"<div class='ui-card'><p class='metric-title'>Your Active Content</p><div class='metric-value'>{content_count}</div><p class='metric-delta'>Live on platform</p></div>",
                unsafe_allow_html=True)
        with m2:
            rank = 3 if current_studio == "Phoenix Studios" else 5
            st.markdown(
                f"<div class='ui-card'><p class='metric-title'>Your Studio Rank</p><div class='metric-value'>#{rank}</div><p class='metric-delta'>of 12 studios</p></div>",
                unsafe_allow_html=True)
        with m3:
            views_display = f"{total_views / 1000000:.1f}M" if total_views >= 1000000 else f"{total_views / 1000:.0f}K"
            st.markdown(
                f"<div class='ui-card'><p class='metric-title'>Total Views (30d)</p><div class='metric-value'>{views_display}</div><p class='metric-delta delta-up'>+12.3% vs last month</p></div>",
                unsafe_allow_html=True)
        with m4:
            st.markdown(
                f"<div class='ui-card'><p class='metric-title'>Avg Completion Rate</p><div class='metric-value'>{avg_completion:.0f}%</div><p class='metric-delta delta-up'>+2% vs platform avg</p></div>",
                unsafe_allow_html=True)

    st.markdown("---")

    # ========== SECTION 2: AI INSIGHTS & CHATBOT ==========
    col_left, col_right = st.columns([2, 1])

    with col_left:
        st.markdown("### 📊 Content Performance")

        # Display content cards - NOW USING FILTERED content_perf
        if content_perf:
            for content_id, content in content_perf.items():
                # Performance badge
                perf_badge = content.get('performance_badge', 'good')
                if perf_badge == 'excellent':
                    badge_html = "<span class='perf-excellent'>🔥 Excellent</span>"
                elif perf_badge == 'good':
                    badge_html = "<span class='perf-good'>✅ Good</span>"
                else:
                    badge_html = "<span class='perf-warning'>⚠️ Needs Attention</span>"

                # Trending indicator
                trending = content.get('trending', 'stable')
                if trending == 'up':
                    trend_icon = "📈"
                    trend_color = "#10B981"
                elif trending == 'down':
                    trend_icon = "📉"
                    trend_color = "#EF4444"
                else:
                    trend_icon = "➡️"
                    trend_color = "#9CA3AF"

                # Format viewership
                views_raw = content.get('viewership_hours', 0)
                if views_raw >= 1000000:
                    views_display = f"{views_raw / 1000000:.1f}M"
                else:
                    views_display = f"{views_raw / 1000:.0f}K"

                st.markdown(f"""
                <div class='content-perf-card'>
                    <div style='display:flex; justify-content:space-between; align-items:start; margin-bottom:15px;'>
                        <div>
                            <h4 style='margin:0; font-size:18px; color:#FFFFFF;'>{content['title']}</h4>
                            <p style='color:#9CA3AF; font-size:13px; margin:5px 0 0 0;'>{content['genre']} • {content['studio']}</p>
                        </div>
                        <div style='text-align:right;'>
                            {badge_html}
                            <div style='color:{trend_color}; font-size:20px; margin-top:5px;'>{trend_icon}</div>
                        </div>
                    </div>
                    <div style='display:flex; gap:12px; margin-top:15px;'>
                        <div style='flex:1; background:#1A1F2E; padding:12px; border-radius:8px; text-align:center;'>
                            <small style='color:#9CA3AF; font-size:11px;'>Views</small><br>
                            <b style='color:#FFFFFF; font-size:16px;'>{views_display}</b>
                        </div>
                        <div style='flex:1; background:#1A1F2E; padding:12px; border-radius:8px; text-align:center;'>
                            <small style='color:#9CA3AF; font-size:11px;'>Completion</small><br>
                            <b style='color:#10B981; font-size:16px;'>{content['completion_rate']}%</b>
                        </div>
                        <div style='flex:1; background:#1A1F2E; padding:12px; border-radius:8px; text-align:center;'>
                            <small style='color:#9CA3AF; font-size:11px;'>Avg Time</small><br>
                            <b style='color:#FFFFFF; font-size:16px;'>{content['avg_watch_time']}m</b>
                        </div>
                        <div style='flex:1; background:#1A1F2E; padding:12px; border-radius:8px; text-align:center;'>
                            <small style='color:#9CA3AF; font-size:11px;'>Top Region</small><br>
                            <b style='color:#FFFFFF; font-size:16px;'>{content['top_region'][:3]}</b>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info(f"No content data available for {studio_filter}")

    with col_right:
        # AI INSIGHTS PANEL
        st.markdown("### 🤖 AI Analytics Advisor")

        # Weekly AI Summary
        st.markdown("""
        <div style='background: linear-gradient(135deg, #1A1F2E 0%, #13161F 100%); 
                    border-left: 4px solid #E50914; 
                    border-radius: 8px; 
                    padding: 15px; 
                    margin-bottom: 20px;'>
            <div style='font-size: 12px; color: #9CA3AF; text-transform: uppercase; margin-bottom: 8px;'>
                📅 Weekly Summary
            </div>
        """, unsafe_allow_html=True)

        # Generate AI summary with FILTERED data
        summary_data = {
            'content_performance': content_perf,  # Use filtered content
            'total_content': len(content_perf),
            'top_content': [{'title': c['title']} for c in content_perf.values()],
            'health_score': 84 if is_netflix_exec else 80,
            'studio_content_count': len(content_perf),
            'studio_rank': 3 if current_studio == "Phoenix Studios" else 5,
            'total_studios': 12,
            'vs_platform': '+2%',
            'studio_name': studio_filter if is_netflix_exec else current_studio
        }

        if st.button("🔄 Generate AI Summary", key="gen_summary", use_container_width=True):
            with st.spinner("🤖 AI analyzing..."):
                summary = generate_analytics_summary(user_role, summary_data)
                st.session_state.ai_weekly_summary = summary

        if 'ai_weekly_summary' in st.session_state:
            st.markdown(f"""
            <div style='color: #D1D5DB; font-size: 13px; line-height: 1.6;'>
                {st.session_state.ai_weekly_summary}
            </div>
            """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

        # CHATBOT INTERFACE
        st.markdown("---")
        st.markdown("#### 💬 Ask Analytics AI")

        # Chat history display
        chat_container = st.container()
        with chat_container:
            for msg in st.session_state.analytics_chat_history[-6:]:
                if msg['role'] == 'user':
                    st.markdown(f"""
                    <div class='chat-message user-message'>
                        {msg['content']}
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class='chat-message ai-message'>
                        🤖 {msg['content']}
                    </div>
                    """, unsafe_allow_html=True)

        # Chat input
        with st.form("analytics_chat_form", clear_on_submit=True):
            user_question = st.text_input(
                "Ask about performance, trends, or insights...",
                placeholder="e.g., Which genre performs best?",
                label_visibility="collapsed"
            )
            submit_chat = st.form_submit_button("Send", use_container_width=True)

            if submit_chat and user_question:
                # Add user message
                st.session_state.analytics_chat_history.append({
                    'role': 'user',
                    'content': user_question
                })

                # Build correct data structure with FILTERED content
                chatbot_data = {
                    'content_performance': content_perf,  # Use filtered content
                    'total_content': len(content_perf),
                    'health_score': 84 if is_netflix_exec else 80,
                    'studio_name': studio_filter if is_netflix_exec else current_studio
                }

                # Get AI response
                with st.spinner("🤖 Thinking..."):
                    chatbot_data = {
                        'content_performance': content_perf,  # ✅ Now it has the actual content!
                        'total_content': len(content_perf),
                        'health_score': 84 if is_netflix_exec else 80,
                        'studio_name': current_studio if not is_netflix_exec else None
                    }
                    
                    ai_response = analytics_chatbot(
                        user_question,
                        st.session_state.analytics_chat_history,
                        user_role,
                        chatbot_data
                    )

                # Add AI response
                st.session_state.analytics_chat_history.append({
                    'role': 'assistant',
                    'content': ai_response
                })

                st.rerun()

        # Clear chat button
        if st.session_state.analytics_chat_history:
            if st.button("🗑️ Clear Chat", key="clear_chat"):
                st.session_state.analytics_chat_history = []
                st.rerun()

# ============================================================================
# MAIN APP FLOW
# ============================================================================
# ============================================================================
# MAIN APP FLOW
# ============================================================================
def main():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        # Login Page - Modern Netflix Style
        st.markdown("""
        <style>
        /* Hide default Streamlit header/footer */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        /* Full height container to vertically center */
        .stApp {
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            background-color: #1A1D29;
        }

        /* 
           FIX: Target the Streamlit Form directly to make it the "Login Box" 
           Instead of .login-box, we style [data-testid="stForm"]
        */
        [data-testid="stForm"] {
            background: linear-gradient(135deg, #242936 0%, #2a3544 100%);
            border-radius: 16px;
            padding: 40px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
            border: 1px solid rgba(255, 255, 255, 0.1);
            width: 100%;
            max-width: 450px;
            margin: auto;
        }

        /* Text Styling */
        .netflix-logo { text-align: center; margin-bottom: 10px; }
        .netflix-title { font-size: 48px; font-weight: 800; color: #E50914; letter-spacing: -1px; line-height: 1;}
        .studio-subtitle { text-align: center; color: #9CA3AF; font-size: 18px; margin-bottom: 40px; font-weight: 500; }
        .welcome-text { text-align: center; font-size: 28px; font-weight: 700; color: #FFFFFF; margin-bottom: 10px; }
        .signin-subtitle { text-align: center; color: #9CA3AF; font-size: 14px; margin-bottom: 35px; }

        /* Footer Styling */
        .login-footer { text-align: center; margin-top: 30px; padding-top: 25px; border-top: 1px solid rgba(255, 255, 255, 0.1); }
        .footer-text { color: #6B7280; font-size: 13px; }
        .contact-link { color: #E50914; text-decoration: none; font-weight: 600; }

        /* Input Styling */
        .stTextInput > div > div > input {
            background-color: #1A1D29 !important;
            border: 2px solid #3D4556 !important;
            border-radius: 8px !important;
            padding: 14px 16px !important;
            color: #FFFFFF !important;
            font-size: 15px !important;
        }
        .stTextInput > div > div > input:focus {
            border-color: #E50914 !important;
            background-color: #1F2330 !important;
            box-shadow: 0 0 0 3px rgba(229, 9, 20, 0.1) !important;
        }

        /* Button Styling */
        div[data-testid="stFormSubmitButton"] > button {
            background: linear-gradient(90deg, #E50914 0%, #B20710 100%) !important;
            color: #FFFFFF !important;
            font-weight: 700 !important;
            font-size: 16px !important;
            padding: 14px 20px !important;
            border-radius: 8px !important;
            border: none !important;
            width: 100% !important;
            margin-top: 10px !important;
            box-shadow: 0 4px 12px rgba(229, 9, 20, 0.3) !important;
            transition: all 0.3s ease !important;
        }
        div[data-testid="stFormSubmitButton"] > button:hover {
            background: linear-gradient(90deg, #F21120 0%, #C70813 100%) !important;
            box-shadow: 0 6px 16px rgba(229, 9, 20, 0.4) !important;
            transform: translateY(-1px) !important;
        }
        </style>
        """, unsafe_allow_html=True)

        # Create 3 columns to center the content, using the middle one
        c1, c2, c3 = st.columns([1, 2, 1])

        with c2:
            # FIX: Everything goes INSIDE the form
            with st.form("login_form", clear_on_submit=False):
                # 1. Header Content (Logo & Welcome)
                st.markdown("""
                <div class='netflix-logo'>
                    <div style='font-size: 50px; margin-bottom: 5px;'>▶️</div>
                    <div class='netflix-title'>NETFLIX</div>
                    <div class='studio-subtitle'>Studio Connect</div>
                </div>
                <div class='welcome-text'>Welcome back</div>
                <div class='signin-subtitle'>Sign in to access your studio portal</div>
                """, unsafe_allow_html=True)

                # 2. Input Fields
                email = st.text_input("Email address", key="login_email", placeholder="you@studio.com")
                password = st.text_input("Password", type="password", key="login_password", placeholder="Enter your password")

                # 3. Submit Button
                submitted = st.form_submit_button("Sign In", use_container_width=True)

                # 4. Footer Content
                st.markdown("""
                <div class='login-footer'>
                    <div class='footer-text'>
                        New partner? <a href='#' class='contact-link'>Contact Netflix</a>
                    </div>
                    <div class='footer-text' style='margin-top: 20px;'>
                        © 2024 Netflix Studio Connect. All rights reserved.
                    </div>
                </div>
                """, unsafe_allow_html=True)

                if submitted:
                    users = load_json('users.json')
                    # Basic check (in real app, use safer logic)
                    if email in users and users[email]['password'] == hash_txt(password):
                        st.session_state.logged_in = True
                        st.session_state.user = users[email]
                        st.session_state.current_user_role = users[email].get('role', 'studio')
                        st.rerun()
                    else:
                        st.error("❌ Invalid credentials. Please try again.")

    else:
        # ==========================================
        # LOGGED IN VIEW (Sidebar & Content)
        # ==========================================
        # ============================================================================
        # REPLACE YOUR SIDEBAR CODE IN main() FUNCTION
        # ============================================================================

# Find the sidebar section in your main() function (around line 950-990) and REPLACE with:

        # ==========================================
        # LOGGED IN VIEW (Sidebar & Content)
        # ==========================================
        with st.sidebar:
            # Logo/Header
            st.markdown("""
            <div style='text-align: center; padding: 20px 0 10px 0;'>
                <div style='font-size: 36px; margin-bottom: 8px;'>▶️</div>
                <h2 style='color:#E50914; margin: 0; font-size: 24px; font-weight: 800;'>NETFLIX</h2>
                <p style='color:#9CA3AF; font-size: 13px; margin: 5px 0 0 0; font-weight: 500;'>Studio Connect</p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("<div style='margin-bottom: 30px;'></div>", unsafe_allow_html=True)

            # Navigation Menu
            sel = option_menu(
                menu_title=None,
                options=["Dashboard", "Pitch Portal", "Production", "Analytics"],
                icons=["grid", "lightbulb", "camera-reels", "bar-chart"],
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
                        "background-color": "rgba(229, 9, 20, 0.1)",
                        "color": "#E50914",
                        "border-radius": "8px",
                        "font-weight": "600"
                    },
                }
            )

            # Spacer
            st.markdown("<div style='flex-grow: 1; min-height: 100px;'></div>", unsafe_allow_html=True)

            # User Profile Card
            user_name = st.session_state.user.get('name', 'User')
            user_studio = st.session_state.user.get('studio', 'Studio')
            user_role = st.session_state.user.get('role', 'studio')

            # Determine role display
            if user_role == 'netflix_exec':
                role_display = "Netflix Executive"
                role_color = "#9CA3AF"
            else:
                role_display = "Studio Executive"
                role_color = "#9CA3AF"

            st.markdown(f"""
            <div class='user-profile-card'>
                <div class='user-profile-label'>Logged in as</div>
                <div class='user-profile-name'>{user_name}</div>
                <div class='user-profile-studio'>{user_studio}</div>
                <div class='user-profile-role' style='color: {role_color};'>
                    {role_display}
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)

            # Logout Button
            if st.button("Logout", use_container_width=True, key="logout_btn"):
                st.session_state.logged_in = False
                if 'current_user_role' in st.session_state:
                    del st.session_state.current_user_role
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


# ============================================================================
# REPLACE YOUR ENTIRE init() FUNCTION WITH THIS
# ============================================================================

def init():
    """Initialize data files with multi-studio support"""

    # ========== USERS ==========
    if not os.path.exists('users.json'):
        save_json(
            'users.json', {
                "phoenix_exec": {
                    "password": hash_txt("phoenix123"),
                    "name": "Alex Rivera",
                    "studio": "Phoenix Studios",
                    "role": "studio"
                },
                "meridian_exec": {
                    "password": hash_txt("meridian123"),
                    "name": "Jordan Chen",
                    "studio": "Meridian Pictures",
                    "role": "studio"
                },
                "netflix_exec": {
                    "password": hash_txt("netflix123"),
                    "name": "Sarah Chen",
                    "studio": "Netflix Content Team",
                    "role": "netflix_exec"
                }
            })
    else:
        # Update existing users to ensure correct structure
        users = load_json('users.json')
        needs_update = False

        # Rename old "studio_exec" to "phoenix_exec"
        if 'studio_exec' in users and 'phoenix_exec' not in users:
            users['phoenix_exec'] = users.pop('studio_exec')
            users['phoenix_exec']['name'] = "Alex Rivera"
            needs_update = True

        # Add Meridian if not exists
        if 'meridian_exec' not in users:
            users['meridian_exec'] = {
                "password": hash_txt("meridian123"),
                "name": "Jordan Chen",
                "studio": "Meridian Pictures",
                "role": "studio"
            }
            needs_update = True

        # Ensure Netflix exec exists
        if 'netflix_exec' not in users:
            users['netflix_exec'] = {
                "password": hash_txt("netflix123"),
                "name": "Sarah Chen",
                "studio": "Netflix Content Team",
                "role": "netflix_exec"
            }
            needs_update = True

        # Fix roles
        if 'phoenix_exec' in users and users['phoenix_exec'].get('role') != 'studio':
            users['phoenix_exec']['role'] = 'studio'
            needs_update = True

        if 'meridian_exec' in users and users['meridian_exec'].get('role') != 'studio':
            users['meridian_exec']['role'] = 'studio'
            needs_update = True

        if 'netflix_exec' in users and users['netflix_exec'].get('role') != 'netflix_exec':
            users['netflix_exec']['role'] = 'netflix_exec'
            needs_update = True

        if needs_update:
            save_json('users.json', users)

    # ========== PROJECTS ==========
    if not os.path.exists('projects.json'):
        save_json(
            'projects.json', {
                # Phoenix Studios Projects
                "1": {
                    "name": "Midnight Chronicles",
                    "phase": "Post-Production",
                    "progress": 65,
                    "due": "Dec 15, 2024",
                    "studio": "Phoenix Studios"
                },
                # Meridian Pictures Projects
                "2": {
                    "name": "Neon Horizon",
                    "phase": "Production",
                    "progress": 45,
                    "due": "Jan 20, 2025",
                    "studio": "Meridian Pictures"
                }
            })

    # ========== PITCHES ==========
    if not os.path.exists('pitches.json'):
        save_json(
            'pitches.json', {
                # Phoenix Studios Pitches
                "1": {
                    "title": "Midnight Chronicles",
                    "genre": "Sci-Fi Thriller",
                    "logline": "In a future where dreams can be recorded and shared, a rogue dream detective uncovers a conspiracy.",
                    "description": "In a future where dreams can be recorded and shared, a rogue dream detective uncovers a conspiracy that threatens the fabric of reality itself. As she delves deeper into the mystery, she must confront her own buried memories and decide what's real and what's fabricated.",
                    "target": "Adults 18-49",
                    "studio": "Phoenix Studios",
                    "status": "Under Review",
                    "submitted": "Nov 1, 2024",
                    "days_ago": "2 days ago"
                },
                "2": {
                    "title": "The Last Horizon",
                    "genre": "Drama",
                    "logline": "An astronaut confronts her past during humanity's first mission to Mars.",
                    "description": "An astronaut confronts her past during humanity's first mission to Mars, discovering that the journey to another world requires confronting the demons she left behind on Earth.",
                    "target": "Adults 18-49",
                    "studio": "Phoenix Studios",
                    "status": "Approved",
                    "submitted": "Oct 25, 2024",
                    "days_ago": "5 days ago"
                },
                "3": {
                    "title": "Echo Chamber",
                    "genre": "Psychological Thriller",
                    "logline": "A true crime podcaster discovers that her listeners' anonymous confessions are connected to unsolved murders.",
                    "description": "A true crime podcaster discovers that her listeners' anonymous confessions are connected to a series of unsolved murders. As the line between storyteller and investigator blurs, she becomes the next target.",
                    "target": "Young Adults 18-34",
                    "studio": "Phoenix Studios",
                    "status": "Feedback Received",
                    "submitted": "Oct 22, 2024",
                    "days_ago": "1 week ago"
                },
                "4": {
                    "title": "Starlight Runners",
                    "genre": "Adventure",
                    "logline": "In a colonized solar system, a crew of charismatic smugglers navigate dangerous trade routes.",
                    "description": "In a colonized solar system, a crew of charismatic smugglers navigate dangerous trade routes while evading corporate authorities and space pirates, all while uncovering a conspiracy that could change humanity's future among the stars.",
                    "target": "Adults 18-49",
                    "studio": "Phoenix Studios",
                    "status": "Under Review",
                    "submitted": "Oct 28, 2024",
                    "days_ago": "3 days ago"
                },

                # Meridian Pictures Pitches
                "5": {
                    "title": "Silent Symphony",
                    "genre": "Drama",
                    "logline": "A deaf composer discovers she can hear music through touch, revolutionizing the classical music world.",
                    "description": "Born deaf but with an extraordinary gift, Maya can perceive music through vibrations and touch. When she composes a groundbreaking symphony using unconventional methods, the classical music establishment must confront its prejudices. A story about breaking barriers and redefining what it means to truly hear music.",
                    "target": "Adults 18-49",
                    "studio": "Meridian Pictures",
                    "status": "Under Review",
                    "submitted": "Nov 5, 2024",
                    "days_ago": "1 day ago"
                },
                "6": {
                    "title": "Quantum Leap",
                    "genre": "Sci-Fi Thriller",
                    "logline": "A physicist accidentally creates a device that lets her communicate with parallel versions of herself.",
                    "description": "Dr. Elena Park's quantum communication experiment goes awry, opening channels to parallel universes where different versions of herself made different choices. As she navigates infinite possibilities, she must decide which version of her life is worth fighting for—before the multiverse collapses.",
                    "target": "Young Adults 18-34",
                    "studio": "Meridian Pictures",
                    "status": "Approved",
                    "submitted": "Oct 18, 2024",
                    "days_ago": "2 weeks ago"
                },
                "7": {
                    "title": "Underneath",
                    "genre": "Horror",
                    "logline": "Urban explorers discover an ancient civilization living beneath modern New York City.",
                    "description": "What begins as an urban exploration documentary turns into a nightmare when a film crew discovers an entrance to a vast underground society that has existed beneath Manhattan for millennia. They worship something ancient and hungry, and the explorers' arrival has awakened it.",
                    "target": "Young Adults 18-34",
                    "studio": "Meridian Pictures",
                    "status": "Under Review",
                    "submitted": "Oct 30, 2024",
                    "days_ago": "4 days ago"
                }
            })

    # ========== ANALYTICS DATA ==========
    if not os.path.exists('analytics_data.json'):
        analytics_data = {
            "content_performance": {
                # Phoenix Studios Content
                "1": {
                    "title": "Midnight Chronicles",
                    "genre": "Sci-Fi Thriller",
                    "studio": "Phoenix Studios",
                    "viewership_hours": 8200000,
                    "completion_rate": 87,
                    "avg_watch_time": 42,
                    "top_region": "United States",
                    "top_age_group": "25-34",
                    "trending": "up",
                    "performance_badge": "excellent"
                },
                "2": {
                    "title": "The Last Horizon",
                    "genre": "Drama",
                    "studio": "Phoenix Studios",
                    "viewership_hours": 12500000,
                    "completion_rate": 91,
                    "avg_watch_time": 48,
                    "top_region": "United Kingdom",
                    "top_age_group": "35-44",
                    "trending": "up",
                    "performance_badge": "excellent"
                },
                "3": {
                    "title": "Echo Chamber",
                    "genre": "Psychological Thriller",
                    "studio": "Phoenix Studios",
                    "viewership_hours": 6800000,
                    "completion_rate": 78,
                    "avg_watch_time": 38,
                    "top_region": "Canada",
                    "top_age_group": "18-24",
                    "trending": "stable",
                    "performance_badge": "good"
                },
                "4": {
                    "title": "Starlight Runners",
                    "genre": "Adventure",
                    "studio": "Phoenix Studios",
                    "viewership_hours": 5200000,
                    "completion_rate": 65,
                    "avg_watch_time": 35,
                    "top_region": "Australia",
                    "top_age_group": "18-24",
                    "trending": "down",
                    "performance_badge": "warning"
                },

                # Meridian Pictures Content
                "5": {
                    "title": "Silent Symphony",
                    "genre": "Drama",
                    "studio": "Meridian Pictures",
                    "viewership_hours": 9500000,
                    "completion_rate": 89,
                    "avg_watch_time": 45,
                    "top_region": "United States",
                    "top_age_group": "35-44",
                    "trending": "up",
                    "performance_badge": "excellent"
                },
                "6": {
                    "title": "Quantum Leap",
                    "genre": "Sci-Fi Thriller",
                    "studio": "Meridian Pictures",
                    "viewership_hours": 11200000,
                    "completion_rate": 84,
                    "avg_watch_time": 40,
                    "top_region": "United Kingdom",
                    "top_age_group": "18-24",
                    "trending": "up",
                    "performance_badge": "excellent"
                },
                "7": {
                    "title": "Underneath",
                    "genre": "Horror",
                    "studio": "Meridian Pictures",
                    "viewership_hours": 7800000,
                    "completion_rate": 72,
                    "avg_watch_time": 36,
                    "top_region": "Canada",
                    "top_age_group": "18-24",
                    "trending": "stable",
                    "performance_badge": "good"
                }
            }
        }
        save_json('analytics_data.json', analytics_data)


if __name__ == "__main__":
    init()
    main()