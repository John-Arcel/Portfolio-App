import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import base64

# ---------------------------------------------------------
# Page Configuration (Sidebar hidden/collapsed)
# ---------------------------------------------------------
st.set_page_config(
    page_title="John Arcel Sabagkit | Developer Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------------
# Session State Initialization
# ---------------------------------------------------------
if "feedback_entries" not in st.session_state:
    st.session_state["feedback_entries"] = []

if "selected_project" not in st.session_state:
    st.session_state["selected_project"] = None

# ---------------------------------------------------------
# Base64 Local Image Loader Helper
# ---------------------------------------------------------
def load_image_as_base64(image_path: str) -> str:
    """Loads a local image file and converts it to a base64 string for HTML rendering."""
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    return f"data:image/jpeg;base64,{encoded}"

# ---------------------------------------------------------
# Professional Dark Mode Styling & Rounded Avatar CSS
# ---------------------------------------------------------
st.markdown("""
<style>
    /* Dark Theme Background */
    .stApp {
        background-color: #0B0F19;
        color: #F3F4F6;
    }
    
    /* Hide the default sidebar navigation button entirely */
    [data-testid="collapsedControl"] {
        display: none;
    }
    
    /* Rounded Profile Avatar */
    .rounded-avatar {
        width: 105px;
        height: 105px;
        border-radius: 50%;
        object-fit: cover;
        border: 3px solid #6366F1;
        box-shadow: 0 0 16px rgba(99, 102, 241, 0.35);
        display: block;
        margin: auto;
    }
    
    /* Header Typography */
    .portfolio-header {
        font-size: 2.2rem;
        font-weight: 800;
        letter-spacing: -0.02em;
        background: linear-gradient(90deg, #FFFFFF, #94A3B8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2px;
    }
    .portfolio-sub {
        color: #94A3B8;
        font-size: 1.0rem;
        margin-bottom: 12px;
    }
    
    /* Card Container */
    .dark-card {
        background-color: #111827;
        border: 1px solid #1F2937;
        border-radius: 10px;
        padding: 18px;
        margin-bottom: 16px;
    }
    
    /* Tech Badges */
    .badge {
        display: inline-block;
        padding: 3px 8px;
        background-color: #1E293B;
        color: #38BDF8;
        border: 1px solid #334155;
        border-radius: 6px;
        font-size: 0.75rem;
        font-weight: 500;
        margin-right: 5px;
        margin-top: 5px;
    }
    
    /* Divider line */
    .dark-divider {
        border-top: 1px solid #1F2937;
        margin: 20px 0;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Top Navigation with Rounded Avatar & Status
# ---------------------------------------------------------
col_avatar, col_main, col_action = st.columns([0.8, 3.2, 1.4], vertical_alignment="center")

with col_avatar:
    # Set your local photo path here, e.g., "assets/my_face.jpg" or "my_face.png"
    LOCAL_AVATAR_PATH = "assets/1737042940292.jpg"
    FALLBACK_AVATAR_URL = "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=300&q=80"
    
    try:
        avatar_src = load_image_as_base64(LOCAL_AVATAR_PATH)
    except Exception:
        avatar_src = FALLBACK_AVATAR_URL
        
    st.markdown(f'<img src="{avatar_src}" class="rounded-avatar" alt="John Arcel R. Sabagkit" />', unsafe_allow_html=True)

with col_main:
    st.markdown('<div class="portfolio-header">John Arcel R. Sabagkit</div>', unsafe_allow_html=True)
    st.markdown('<div class="portfolio-sub">BS Computer Science  |  Cebu Institute of Technology – University ', unsafe_allow_html=True)

st.write("")
 
# Real-time High-Level Metrics
m1, m2, m3, m4 = st.columns(4)
m1.metric(label="Academic Standing", value="3rd Year", delta="CIT - University")
m2.metric(label="Featured Projects", value="5 Major", delta="2 Game Titles")
m3.metric(label="Primary Toolkits", value="8+", delta="Godot, .NET, Python")
m4.metric(label="Focus Area", value="Game Dev", delta="System Design")

st.markdown('<div class="dark-divider"></div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# Tabbed Workspace
# ---------------------------------------------------------
tab_autobio, tab_projects, tab_skills, tab_contact = st.tabs([
    "Autobiography & Roots",
    "Projects & Game Portfolio",
    "Technical Metrics & Data",
    "Inquiries & Peer Review"
])

# =========================================================
# TAB 1: AUTOBIOGRAPHY
# =========================================================
with tab_autobio:
    st.subheader("My Journey: From Gamer to Software Engineer")
    
    col_bio_left, col_bio_right = st.columns([2, 1])
    
    with col_bio_left:
        st.write("""
        My entrance into computer science was sparked by a lifelong fascination with computer games. 
        What began as playing immersive worlds evolved into a drive to understand the systems powering them: 
        *How do game engines simulate aerodynamic lift at high frame rates? How can custom shaders manipulate light on 
        low-poly meshes? How do distributed architectures handle state synchronization?*
        """)
        st.write("""
        Hailing from **Biliran Province** and graduating from **Biliran Province State University - Laboratory High School**, 
        I moved to Cebu City to pursue my Bachelor of Science in Computer Science at **Cebu Institute of Technology – University (CIT-U)**. 
        My design philosophy is grounded in hands-on implementation: mastering concepts by writing compiler-clean, 
        architecturally sound software. 
        """)
        st.write("""
        Whether designing flight dynamics in **Godot**, tuning computer vision filters for coin recognition in **C#**, 
        or architecting mobile utilities in **Kotlin**, I treat software as an engineering discipline guided by mathematical logic.
        """)


    st.markdown("### Key Milestones")
    
    # Component: Expander
    with st.expander("📍 Early Milestone: Biliran Province State University - LHS"):
        st.write("""
        - Developed strong analytical foundations in mathematics, logic, and self-directed programming.
        """)
        
    with st.expander("📍 Intermediate Milestone: Core Systems & Mobile Architecture at CIT-U"):
        st.write("""
        - Developed the **Equipment Borrowing System (EBS)** in JavaFX with relational MySQL integration and SOLID architecture.
        - Engineered **Picsweep** in Android (Kotlin) utilizing the Model-View-Presenter (MVP) pattern and MediaStore APIs.
        - Deepened proficiency in C++, Java, and C# memory structures and algorithms.
        """)

    with st.expander("📍 Current Milestone: Game Development & Applied AI"):
        st.write("""
        - Released prototypes for **AeroSpire** (3D flight mechanics) and **Ame** (custom GLSL shaders & 2D/3D systems).
        - Spearheaded **ReqClub**, integrating Blazor frontends with Django REST backends.
        """)


# =========================================================
# TAB 2: PROJECTS & GAMEDEV
# =========================================================
with tab_projects:
    st.subheader("Featured Engineering & Game Dev Showcase")
    st.write(
        "Browse project implementations. "
        "Explore the projects through their GitHub repositories or showcase posts."
    )

    # ---------------------------------------------------------
    # IN-TAB FILTERS
    # ---------------------------------------------------------
    col_filter_p1, col_filter_p2 = st.columns([1, 2])

    with col_filter_p1:
        # Component: Radio
        view_perspective = st.radio(
            "Filter Category",
            options=[
                "All Domains",
                "Game Dev & Graphics",
                "Web Development"
            ],
            horizontal=True
        )

    with col_filter_p2:
        # Component: Multiselect
        tech_tags = st.multiselect(
            "Filter Tech Stacks",
            options=[
                "Godot",
                "GDScript",
                "C#",
                "Python",
                "Kotlin",
                "Django",
                "Blazor",
                "DIP / Vision"
            ],
            default=["Godot", "Python", "C#"]
        )

    # ---------------------------------------------------------
    # PROJECT CATALOG
    # ---------------------------------------------------------
    project_catalog = [
        {
            "title": "AeroSpire",
            "tagline": "A Strategy/City-building Game",
            "role": "Systems Programmer",
            "tools": [
                "Godot",
                "GDScript",
                "3D Physics",
                "Spatial Nodes"
            ],
            "category": "Game Dev",
            "image": "assets/Game poster.png",

            "description": (
                "AeroSpire is a two-player strategy and city-building game "
                "focused on resource management, sustainability, and resilience. "
                "Players must manage their city's population, food, water, "
                "electricity, and economy while competing for limited resources. "
                "Overconsumption increases the risk of disasters, while "
                "technological upgrades boost GDP but require more electricity. "
                "The goal is to outlast the opponent by maintaining a balanced, "
                "sustainable, and disaster-resistant city."
            ),

            "outcome": (
                "Developed gameplay systems centered on resource management, "
                "sustainable consumption, city development, and disaster resilience."
            ),

            "tech_keys": ["Godot", "GDScript"],

            # Replace with your actual GitHub repository or project post
            "project_url": "https://web.facebook.com/story.php?story_fbid=122129572605282108&id=61588463261309&rdid=baDKzb3VIJ5208of#"
        },

        {
            "title": "Ame",
            "tagline": "Stylized 2D/3D Narrative Exploration & Shader Lab",
            "role": "Programmer & Technical Artist",
            "tools": [
                "Godot",
                "GDScript",
                "Custom Shaders",
                "Lighting"
            ],
            "category": "Game Dev",
            "image": "assets/vCyf5J.png",

            "description": (
                "An atmospheric game project exploring custom visual GLSL "
                "shaders, interactive canvas items, weather and particle nodes, "
                "and responsive character controllers in Godot. Ame is a "
                "story-based horror game set in the Philippines in the early "
                "2000s. It explores rural beliefs, religious imagery, and the "
                "blurred lines between myths and truths, offering players a "
                "nostalgic yet unsettling glimpse into rural life in Cebu."
            ),

            "outcome": (
                "Worked on gameplay programming and technical art, including "
                "custom shaders, character interactions, lighting, and "
                "atmospheric effects."
            ),

            "tech_keys": ["Godot", "GDScript"],

            # Replace with your actual GitHub repository or project post
            "project_url": "https://team9lives.itch.io/ame"
        },

        {
            "title": "ReqClub — Community Runner Platform",
            "tagline": "Full-Stack Training Session & Pace-Matching Utility",
            "role": "Full-Stack Architect",
            "tools": [
                "Blazor",
                "Django",
                "Python",
                "SQL"
            ],
            "category": "Web Systems",
            "image": "assets/Your paragraph text.jpg",

            "description": (
                "A web application designed to connect university and regional "
                "runners. It enables users to schedule group pacing workouts, "
                "coordinate running routes, and track training sessions."
            ),

            "outcome": (
                "Designed a multi-tier application combining Blazor interfaces "
                "with Django-based backend services and member management."
            ),

            "tech_keys": ["Django", "Blazor", "Python"],

            # Replace with your actual GitHub repository or project post
            "project_url": "https://github.com/John-Arcel/SabagkitSprintActivity"
        }
    ]

    # ---------------------------------------------------------
    # FILTER PROJECTS BY CATEGORY
    # ---------------------------------------------------------
    filtered_projects = project_catalog

    if view_perspective == "Game Dev & Graphics":
        filtered_projects = [
            project for project in filtered_projects
            if project["category"] == "Game Dev"
        ]

    elif view_perspective == "Web Development":
        filtered_projects = [
            project for project in filtered_projects
            if project["category"] in [
                "Applied AI",
                "Web Systems",
                "Mobile"
            ]
        ]

    # ---------------------------------------------------------
    # FILTER PROJECTS BY TECHNOLOGY
    # ---------------------------------------------------------
    if tech_tags:
        filtered_projects = [
            project for project in filtered_projects
            if any(
                tag in project["tech_keys"]
                for tag in tech_tags
            )
        ]

    # ---------------------------------------------------------
    # DISPLAY PROJECT CARDS
    # ---------------------------------------------------------
    st.markdown(
        '<div class="dark-divider"></div>',
        unsafe_allow_html=True
    )

    if not filtered_projects:
        st.warning(
            "No projects match the active filters. "
            "Adjust your tag selections above."
        )

    else:
        for proj in filtered_projects:

            with st.container():

                col_card_img, col_card_info, col_card_actions = st.columns(
                    [1.2, 2.0, 0.8],
                    vertical_alignment="top"
                )

                # -------------------------------------------------
                # PROJECT IMAGE
                # -------------------------------------------------
                with col_card_img:
                    st.image(
                        proj["image"],
                        caption=f"Project Asset: {proj['title']}",
                        use_container_width=True
                    )

                # -------------------------------------------------
                # PROJECT INFORMATION
                # -------------------------------------------------
                with col_card_info:
                    st.markdown(f"### {proj['title']}")

                    st.caption(
                        f"**{proj['tagline']}** • "
                        f"Role: `{proj['role']}`"
                    )

                    st.write(proj["description"])

                    st.markdown(
                        f"**Outcome:** {proj['outcome']}"
                    )

                    # Technology badges
                    badge_markup = "".join(
                        [
                            f'<span class="badge">{tool}</span>'
                            for tool in proj["tools"]
                        ]
                    )

                    st.markdown(
                        badge_markup,
                        unsafe_allow_html=True
                    )

                # -------------------------------------------------
                # PROJECT ACTIONS
                # -------------------------------------------------
                with col_card_actions:
                    st.markdown("#### Actions")

                    # Each project has its own Inspect button
                    if st.button(
                        "Inspect",
                        key=f"btn_inspect_{proj['title']}",
                        use_container_width=True
                    ):
                        st.session_state["selected_project"] = (
                            proj["title"]
                        )

                    # Display the project link when selected
                    if (
                        st.session_state.get("selected_project")
                        == proj["title"]
                    ):
                        project_url = proj.get("project_url", "")

                        if project_url:
                            st.link_button(
                                "View Project ↗",
                                project_url,
                                use_container_width=True
                            )

                        else:
                            st.warning(
                                "No project link available yet."
                            )

                    st.caption(
                        f"Domain: {proj['category']}"
                    )

                # Divider between project cards
                st.markdown(
                    '<div class="dark-divider"></div>',
                    unsafe_allow_html=True
                )

# =========================================================
# TAB 3: SKILLS & CHARTS
# =========================================================
with tab_skills:
    st.subheader("Quantitative Skill Matrix & Applied AI Metrics")
    st.write("Quantitative self-assessment based on engineering hours, shipped projects, and coursework.")
    
    # In-tab Slider & Checkbox (Preserving required rubric controls)
    col_ctrl1, col_ctrl2 = st.columns([2, 1])
    with col_ctrl1:
        # Component: Slider
        min_proficiency = st.slider(
            "Filter Skills by Minimum Competency (%)",
            min_value=50,
            max_value=100,
            value=75,
            step=5
        )
    with col_ctrl2:
        # Component: Checkbox
        display_matrix = st.checkbox("Show Raw Data Table", value=False)
    
    skills_dataset = {
        "Technology": [
            "Godot & GDScript", 
            "Python (AI / Backend)", 
            "C# (.NET / WinForms)", 
            "C++ (Memory & Logic)", 
            "Kotlin (Android SDK)", 
            "Digital Image Processing (DIP)",
            "Web (Django & Blazor)", 
            "Custom Shaders (GLSL)", 
            "SQL & Relational DB"
        ],
        "Domain": [
            "Game Development", 
            "Applied AI", 
            "Systems & Vision", 
            "Core Programming", 
            "Mobile Systems", 
            "Applied AI", 
            "Web Architecture", 
            "Game Graphics", 
            "Data Management"
        ],
        "Proficiency": [88, 86, 85, 83, 80, 82, 81, 78, 79],
        "Hours_Logged": [320, 290, 240, 310, 180, 140, 210, 120, 190]
    }
    
    df_skills = pd.DataFrame(skills_dataset)
    df_filtered = df_skills[df_skills["Proficiency"] >= min_proficiency].sort_values(by="Proficiency", ascending=False)
    
    col_chart, col_meta = st.columns([3, 2])
    
    with col_chart:
        st.markdown("#### Proficiency Distribution (%)")
        # Component: Chart (st.bar_chart)
        st.bar_chart(
            df_filtered.set_index("Technology")[["Proficiency"]],
            color="#6366F1"
        )
        
    with col_meta:
        st.markdown("#### Technical Breakdown")
        st.markdown("""
        - **Game Architecture (Ame & AeroSpire):** Extensive use of node structures, custom spatial mechanics, and GLSL visual shaders.
        - **Applied AI & Vision:** Implementing contour tracking, thresholding filters, and automated coin valuation.
        - **System Reliability:** Writing clean, decoupled code using MVP and SOLID architectural patterns.
        """)
        
    # Component: Table (st.dataframe)
    if display_matrix:
        st.markdown("#### Complete Competencies Matrix")
        st.dataframe(df_filtered, use_container_width=True)

# =========================================================
# TAB 4: CONTACT & FEEDBACK FORM
# =========================================================
with tab_contact:
    st.subheader("Peer Review & Inquiries")
    st.write("Submit evaluations, course feedback, or developer collaboration queries.")
    
    col_entry, col_stream = st.columns([3, 2])
    
    with col_entry:
        # Component: Form
        with st.form("portfolio_contact_form", clear_on_submit=True):
            # Component: Text input
            reviewer_name = st.text_input("Reviewer Name", placeholder="e.g., Prof. / Peer Reviewer")
            reviewer_email = st.text_input("Contact Email", placeholder="e.g., reviewer@cit.edu")
            review_category = st.selectbox(
                "Feedback Topic", 
                ["CSIT 349 Activity Evaluation", "AeroSpire / Ame Game Feedback", "Code Architecture Inquiry", "General Remarks"]
            )
            # Component: Text area
            review_notes = st.text_area("Observations / Comments", placeholder="Enter your detailed remarks...")
            
            # Form submit button
            submit_action = st.form_submit_button("Record Feedback")
            
            if submit_action:
                if not reviewer_name.strip() or not review_notes.strip():
                    st.error("Please complete both the Name and Feedback fields before submitting.")
                else:
                    new_record = {
                        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "name": reviewer_name,
                        "email": reviewer_email if reviewer_email else "Confidential",
                        "category": review_category,
                        "notes": review_notes
                    }
                    st.session_state["feedback_entries"].append(new_record)
                    st.success("Evaluation submitted successfully. Thank you!")
                    st.balloons()
                    
    with col_stream:
        st.markdown("#### Recorded Feedback Stream")
        if not st.session_state["feedback_entries"]:
            st.info("No reviews submitted in this browser session. Test the form to verify reactive state!")
        else:
            for item in reversed(st.session_state["feedback_entries"]):
                st.markdown(f"""
                <div class="dark-card">
                    <strong style="color:#38BDF8;">{item['name']}</strong> — <span style="font-size:0.8rem; color:#94A3B8;">{item['category']}</span><br>
                    <span style="font-size:0.75rem; color:#64748B;">{item['timestamp']}</span>
                    <p style="margin-top:8px; margin-bottom:0; font-size:0.9rem;">{item['notes']}</p>
                </div>
                """, unsafe_allow_html=True)

# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------
st.markdown('<div class="dark-divider"></div>', unsafe_allow_html=True)
col_foot1, col_foot2 = st.columns(2)
with col_foot1:
    st.caption("Coursework: **CSIT 349 · Applied AI** — Autobiography & Portfolio App")
with col_foot2:
    st.markdown('<p style="text-align:right; font-size:0.8rem; color:#64748B;">© 2026 John Arcel R. Sabagkit | CIT - University</p>', unsafe_allow_html=True)