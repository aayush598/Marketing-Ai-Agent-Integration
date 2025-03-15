import streamlit as st
from audience import get_target_audience
from agents.MarketingAgent import MarketingAgent
import google.generativeai as genai

# Initialize MarketingAgent
marketing_agent = MarketingAgent(groq_api_key="YOUR_GROQ_API_KEY", serpapi_key="YOUR_SERPAPI_KEY")

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
audience = get_target_audience()
platform = st.selectbox("Select Platform:", ["Twitter", "LinkedIn", "Instagram", "Facebook", "YouTube", "Other"])

# Multi-select for actions
selected_actions = st.multiselect("Select Actions:", ACTIONS)

# Define session states
session_keys = [
    "blog_info", "blog_post_text", "blog_modifications","blog_post_modifications",
    "video_script_info", "video_script_text", "video_script_modifications",
    "social_media_info", "social_media_post_text", "social_media_modifications"
]

for key in session_keys:
    if key not in st.session_state:
        st.session_state[key] = None if "info" in key else ""

# Prepare formatted prompt
if product_name and product_features and description and audience and platform and selected_actions:
    product_features = [feature.strip() for feature in product_features.split(',')]
    formatted_prompt = [product_name, product_features, description, audience, platform]
else:
    formatted_prompt = None  # Ensures it's not used before input validation

# Button to start the campaign
if st.button("Generate Campaign"):
    if formatted_prompt:
        response = marketing_agent.run_campaign(formatted_prompt, actions=selected_actions)
        
        if "blog_structure" in response:
            st.session_state.blog_info = response["blog_structure"]
        if "video_script" in response:
            st.session_state.video_script_info = response["video_script"]
        if "social_media_info" in response:
            st.session_state.social_media_info = response["social_media_info"]
        
        st.rerun()
    else:
        st.warning("Please fill in all fields and select at least one action.")

### **🔹 Blog Post Generation**
if st.session_state.blog_info:
    st.subheader("Suggested Blog Info")
    st.text_area("Blog Details", st.session_state.blog_info, height=300)

    st.session_state.blog_modifications = st.text_area(
        "Modify Blog Info (Before Generation):", st.session_state.blog_modifications
    )

    if st.button("Modify Blog Info"):
        if st.session_state.blog_modifications:
            response = marketing_agent.run_campaign(
                formatted_prompt, 
                actions=["blog_post"], 
                modifications={"blog_structure": st.session_state.blog_info, "blog_modifications": st.session_state.blog_modifications}
            )
            st.session_state.blog_info = response["blog_structure"]
            st.rerun()

    if st.button("Confirm & Generate Blog"):
        response = marketing_agent.run_campaign(
            formatted_prompt, 
            actions=["blog_post"], 
            modifications={"blog_structure": st.session_state.blog_info}, 
            confirm_final=True
        )
        st.session_state.blog_post_text = response["blog_post"]
        st.rerun()

if st.session_state.blog_post_text:
    st.subheader("Generated Blog Post")
    st.text_area("Blog Content", st.session_state.blog_post_text, height=400)

    # ✅ Adding an input field for modifying the generated blog
    st.session_state.blog_post_modifications = st.text_area(
        "Modify Blog (Optional):", 
        st.session_state.blog_post_modifications
    )

    if st.button("Modify Blog"):
        response = marketing_agent.run_campaign(
            formatted_prompt, 
            actions=["blog_post"], 
            modifications={
                "blog_post": st.session_state.blog_post_text, 
                "blog_post_modifications": st.session_state.blog_post_modifications
            }
        )
        st.session_state.blog_post_text = response["blog_post"]
        st.rerun()


### **🔹 Video Script Generation**
if st.session_state.video_script_info:
    st.subheader("Suggested Video Script Info")
    st.text_area("Script Info", st.session_state.video_script_info, height=300)

    st.session_state.video_script_modifications = st.text_area(
        "Modify Script Info (Before Generation):", st.session_state.video_script_modifications
    )

    if st.button("Modify Video Script Info"):
        if st.session_state.video_script_modifications:
            response = marketing_agent.run_campaign(
                formatted_prompt, 
                actions=["video_script"], 
                modifications={"video_script": st.session_state.video_script_info, "video_script_modifications": st.session_state.video_script_modifications}
            )
            st.session_state.video_script_info = response["video_script"]
            st.rerun()

    if st.button("Confirm & Generate Video Script"):
        response = marketing_agent.run_campaign(
            formatted_prompt, 
            actions=["video_script"], 
            modifications={"video_script": st.session_state.video_script_info}, 
            confirm_final=True
        )
        st.session_state.video_script_text = response["video_script"]
        st.rerun()

if st.session_state.video_script_text:
    st.subheader("Generated Video Script")
    st.text_area("Video Script", st.session_state.video_script_text, height=300)

    st.session_state.video_script_modifications = st.text_area(
        "Modify Script (Optional):", st.session_state.video_script_modifications
    )

    if st.button("Modify Video Script"):
        response = marketing_agent.run_campaign(
            formatted_prompt, 
            actions=["video_script"], 
            modifications={"video_script": st.session_state.video_script_text, "video_script_modifications": st.session_state.video_script_modifications}
        )
        st.session_state.video_script_text = response["video_script"]
        st.rerun()

### **🔹 Social Media Post Generation**
if st.session_state.social_media_info:
    st.subheader("Suggested Social Media Post Info")
    st.text_area("Post Info", st.session_state.social_media_info, height=300)

    st.session_state.social_media_modifications = st.text_area(
        "Modify Post Info (Before Generation):", st.session_state.social_media_modifications
    )

    if st.button("Modify Social Media Info"):
        if st.session_state.social_media_modifications:
            response = marketing_agent.run_campaign(
                formatted_prompt, 
                actions=["social_media_post"], 
                modifications={"social_media_info": st.session_state.social_media_info, "social_media_modifications": st.session_state.social_media_modifications}
            )
            st.session_state.social_media_info = response["social_media_info"]
            st.rerun()

    if st.button("Confirm & Generate Social Media Post"):
        response = marketing_agent.run_campaign(
            formatted_prompt, 
            actions=["social_media_post"], 
            modifications={"social_media_info": st.session_state.social_media_info}, 
            confirm_final=True
        )
        st.session_state.social_media_post_text = response["social_media_post"]
        st.rerun()

if st.session_state.social_media_post_text:
    st.subheader("Generated Social Media Post")
    st.text_area("Social Media Post", st.session_state.social_media_post_text, height=300)

    st.session_state.social_media_modifications = st.text_area(
        "Modify Post (Optional):", st.session_state.social_media_modifications
    )

    if st.button("Modify Social Media Post"):
        response = marketing_agent.run_campaign(
            formatted_prompt, 
            actions=["social_media_post"], 
            modifications={"social_media_post": st.session_state.social_media_post_text, "social_media_modifications": st.session_state.social_media_modifications}
        )
        st.session_state.social_media_post_text = response["social_media_post"]
        st.rerun()
