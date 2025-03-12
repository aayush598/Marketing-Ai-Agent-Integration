import streamlit as st
from campaign import generate_campaign

# Define available actions
ACTIONS = [
    "campaign_idea",
    "ad_copy",
    "blog_post",
    "video_script",
    "social_media_post",
    "hashtags",
    "scraped_images",
    "generated_images",
]

st.title("Marketing Campaign Generator")

# Collect input from the user
product_name = st.text_input("Product Name:")
product_features = st.text_area("Product Features (comma-separated):")
description = st.text_area("Campaign Description:")
audience = st.text_input("Target Audience:")
platform = st.selectbox("Select Platform:", ["Twitter", "LinkedIn", "Instagram", "Facebook", "YouTube", "Other"])

# Multi-select for actions
selected_actions = st.multiselect("Select Actions:", ACTIONS)

if st.button("Generate Campaign"):
    if product_name and product_features and description and audience and platform and selected_actions:
        product_features = [feature.strip() for feature in product_features.split(',')]
        formatted_prompt = [product_name, product_features, description, audience, platform]

        result = generate_campaign(formatted_prompt, selected_actions)
        st.subheader("Generated Results")
        st.json(result)
    else:
        st.warning("Please fill in all fields and select at least one action.")
