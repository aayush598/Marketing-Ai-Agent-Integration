import streamlit as st
from frontend.blog import display_blog_section
from frontend.social_media import display_social_media_section
from frontend.ad_copy import display_ad_copy_section
from frontend.images import display_images_section
from frontend.monitoring import display_monitoring_section
from frontend.strategy import display_strategy_section
from frontend.planning import display_planning_section
from agents.MarketingAgent import MarketingAgent
from audience import get_target_audience

# ✅ Initialize Marketing Agent
marketing_agent = MarketingAgent(groq_api_key="your_api_key", serpapi_key="your_serp_api_key")

# ✅ Page Title
st.set_page_config(page_title="Marketing AI Tool", layout="wide")
st.title("📢 AI-Powered Marketing Campaign Generator")


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


# ✅ Input Fields for Campaign Details
with st.form("campaign_form"):
    st.subheader("📌 Enter Campaign Details")
    product_name = st.text_input("Product Name:")
    product_features = st.text_area("Product Features (comma separated):")
    description = st.text_area("Product Description:")
    audience = get_target_audience(product_name, product_features, description)
    platform = st.selectbox("Platform:", ["Twitter", "LinkedIn", "Instagram", "Facebook", "YouTube", "Email", "Blog"])
    
    # ✅ Select Actions to Perform
    actions = st.multiselect("Select Actions:", [
        "blog_post", "social_media_post", "ad_copy", "scraped_images", 
        "generated_images", "monitor", "strategy", "planning"
    ])
    
    submit_button = st.form_submit_button("🚀 Generate Content")

# ✅ Run campaign logic when Submit button is clicked
if submit_button and actions:
    print(f"Actions :{actions}")
    formatted_prompt = (product_name, product_features.split(","), description, audience, platform)
    st.session_state.formatted_prompt = formatted_prompt
    response = marketing_agent.run_campaign(formatted_prompt, actions=actions)
    print(f"Response :{response}")
    # ✅ Store responses in Streamlit session state dynamically
    if "blog_structure" in response:
        print(f"Blog post received")
        st.session_state.blog_info = response["blog_structure"]
    if "social_media_structure" in response:
        st.session_state.social_media_info = response["social_media_structure"]
    if "ad_copy" in response:
        st.session_state.ad_copy_info = response["ad_copy"]
    if "scraped_images" in response:
        st.session_state.scraped_images = response["scraped_images"]
    if "generated_images" in response:
        st.session_state.generated_images = response["generated_images"]
    if "monitor" in response:
        st.session_state.monitor_info = response["monitor"]
    if "strategy" in response:
        st.session_state.strategy_info = response["strategy"]
    if "planning" in response:
        st.session_state.planning_info = response["planning"]

# ✅ Retrieve formatted prompt from session (Avoid NameError)
formatted_prompt = st.session_state.get("formatted_prompt", None)

# ✅ Dynamically Render Sections Based on User Selection
if "blog_info" in st.session_state and "blog_post" in actions:
    display_blog_section(marketing_agent, formatted_prompt)
if "social_media_info" in st.session_state and "social_media_post" in actions:
    display_social_media_section(marketing_agent, formatted_prompt)
if "ad_copy_info" in st.session_state and "ad_copy" in actions:
    display_ad_copy_section(marketing_agent, formatted_prompt)
if "scraped_images" in st.session_state and "scraped_images" in actions:
    display_images_section()
if "generated_images" in st.session_state and "generated_images" in actions:
    display_images_section()
if "monitor_info" in st.session_state and "monitor" in actions:
    display_monitoring_section()
if "strategy_info" in st.session_state and "strategy" in actions:
    display_strategy_section(marketing_agent, formatted_prompt)
if "planning_info" in st.session_state and "planning" in actions:
    display_planning_section(marketing_agent, formatted_prompt)
