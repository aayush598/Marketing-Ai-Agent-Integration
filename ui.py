import streamlit as st
from frontend.layout import render_navbar

# ✅ Set Page Configuration
st.set_page_config(page_title="Marketing AI Tool", layout="wide")

# ✅ Render Navbar
page = render_navbar()


# Define session states
session_keys = [
    "formatted_prompt",
    "planning_results","planning_modifications",
    "strategy_data", "strategy_modifications",
    "generated_images",
    "scraped_images",
    "ad_copy_structure", "ad_copy_text", "ad_copy_modifications",
    "blog_info", "blog_post_text", "blog_modifications","blog_post_modifications",
    "video_script_info", "video_script_text", "video_script_modifications","generated_video_script_modifications",
    "social_media_info", "social_media_post_text", "social_media_modifications","generated_social_media_post_modifications"
]

for key in session_keys:
    if key not in st.session_state:
        st.session_state[key] = None if "info" in key else ""
        
# ✅ Routing Based on Page Selection
if page == "Home":
    from frontend.home import display_home
    display_home()
elif page == "Input Form":
    from frontend.input_form import display_input_form
    display_input_form()
elif page == "Blog Post":
    from frontend.blog import display_blog_section
    display_blog_section()
elif page == "Social Media Post":
    from frontend.social_media import display_social_media_section
    display_social_media_section()
elif page == "Ad Copy":
    from frontend.ad_copy import display_ad_copy_section
    display_ad_copy_section()
elif page == "Images":
    from frontend.images import display_images_section
    display_images_section()
elif page == "Monitoring":
    from frontend.monitoring import display_monitoring_section
    display_monitoring_section()
elif page == "Strategy":
    from frontend.strategy import display_strategy_section
    display_strategy_section()
elif page == "Planning":
    from frontend.planning import display_planning_section
    display_planning_section()
