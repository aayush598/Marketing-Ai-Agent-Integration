import streamlit as st
from audience import get_target_audience

ACTIONS = [
    "planning", "strategy", "campaign_idea", "ad_copy",
    "blog_post", "video_script", "social_media_post",
    "hashtags", "scraped_images", "generated_images", "monitor"
]

def collect_inputs():
    """Collect user inputs for the marketing campaign."""
    product_name = st.text_input("Product Name:")
    product_features = st.text_area("Product Features (comma-separated):")
    description = st.text_area("Campaign Description:")
    audience = get_target_audience(product_name, product_features, description)
    platform = st.selectbox("Select Platform:", ["Twitter", "LinkedIn", "Instagram", "Facebook", "YouTube", "Gmail", "Other"])
    selected_actions = st.multiselect("Select Actions:", ACTIONS)

    if product_name and product_features and description and audience and platform and selected_actions:
        product_features_list = [feature.strip() for feature in product_features.split(',')]
        formatted_prompt = [product_name, product_features_list, description, audience, platform]
    else:
        formatted_prompt = None

    return formatted_prompt, selected_actions
