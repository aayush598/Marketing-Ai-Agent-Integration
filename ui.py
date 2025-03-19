import streamlit as st
from frontend.layout import render_navbar

# ✅ Set Page Configuration
st.set_page_config(page_title="Marketing AI Tool", layout="wide")

# ✅ Render Navbar
page = render_navbar()

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
