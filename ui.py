import streamlit as st
from audience import get_target_audience
from agents.MarketingAgent import MarketingAgent
import google.generativeai as genai
from config.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

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
    "video_script_info", "video_script_text", "video_script_modifications","generated_video_script_modifications",
    "social_media_info", "social_media_post_text", "social_media_modifications","generated_social_media_post_modifications"
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
        if "video_script_structure" in response:
            st.session_state.video_script_info = response["video_script_structure"]
        if "social_media_structure" in response:
            st.session_state.social_media_info = response["social_media_structure"]

        
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
    st.subheader("Suggested Video Script Format")
    st.text_area("Video Script Details", st.session_state.video_script_info, height=300)

    # Input for modifying the video script format before generation
    st.session_state.video_script_modifications = st.text_area(
        "Modify Video Script Format (Before Generation):", st.session_state.video_script_modifications
    )

    if st.button("Modify Video Script Format"):
        if st.session_state.video_script_modifications:
            response = marketing_agent.run_campaign(
                formatted_prompt, 
                actions=["video_script"], 
                modifications={"video_script_structure": st.session_state.video_script_info, "video_script_modifications": st.session_state.video_script_modifications}
            )
            st.session_state.video_script_info = response["video_script_structure"]
            st.rerun()

    if st.button("Confirm & Generate Video Script"):
        response = marketing_agent.run_campaign(
            formatted_prompt, 
            actions=["video_script"], 
            modifications={"video_script_structure": st.session_state.video_script_info}, 
            confirm_final=True
        )
        st.session_state.video_script_text = response["video_script"]
        st.rerun()

if st.session_state.video_script_text:
    st.subheader("Generated Video Script")
    st.text_area("Final Video Script", st.session_state.video_script_text, height=400)

    # ✅ Adding an input field for modifying the generated video script
    st.session_state.generated_video_script_modifications = st.text_area(
        "Modify Video Script (Optional):", 
        st.session_state.generated_video_script_modifications
    )

    if st.button("Modify Video Script"):
        response = marketing_agent.run_campaign(
            formatted_prompt, 
            actions=["video_script"], 
            modifications={
                "video_script": st.session_state.video_script_text, 
                "generated_video_script_modifications": st.session_state.generated_video_script_modifications
            }
        )
        st.session_state.video_script_text = response["video_script"]
        st.rerun()

### **🔹 Social Media Post Generation**
if st.session_state.social_media_info:
    st.subheader("Suggested Social Media Post Format")
    st.text_area("Social Media Post Details", st.session_state.social_media_info, height=300)

    # Input for modifying the structured social media post format before full generation
    st.session_state.social_media_modifications = st.text_area(
        "Modify Social Media Post Format (Before Generation):", st.session_state.social_media_modifications
    )

    if st.button("Modify Social Media Post Format"):
        if st.session_state.social_media_modifications:
            response = marketing_agent.run_campaign(
                formatted_prompt, 
                actions=["social_media_post"], 
                modifications={"social_media_structure": st.session_state.social_media_info, "social_media_modifications": st.session_state.social_media_modifications}
            )
            st.session_state.social_media_info = response["social_media_structure"]
            st.rerun()

    if st.button("Confirm & Generate Social Media Post"):
        response = marketing_agent.run_campaign(
            formatted_prompt, 
            actions=["social_media_post"], 
            modifications={"social_media_structure": st.session_state.social_media_info}, 
            confirm_final=True
        )
        st.session_state.social_media_post_text = response["social_media_post"]
        st.rerun()

if st.session_state.social_media_post_text:
    st.subheader("Generated Social Media Post")
    st.text_area("Final Social Media Post", st.session_state.social_media_post_text, height=400)

    # ✅ Adding an input field for modifying the generated social media post
    st.session_state.generated_social_media_post_modifications = st.text_area(
        "Modify Social Media Post (Optional):", 
        st.session_state.generated_social_media_post_modifications
    )

    if st.button("Modify Social Media Post"):
        response = marketing_agent.run_campaign(
            formatted_prompt, 
            actions=["social_media_post"], 
            modifications={
                "social_media_post": st.session_state.social_media_post_text, 
                "generated_social_media_post_modifications": st.session_state.generated_social_media_post_modifications
            }
        )
        st.session_state.social_media_post_text = response["social_media_post"]
        st.rerun()

    # ✅ **Dropdown for Social Media Platform Selection**
    social_media_platform = st.selectbox("Select Platform to Post:", ["Twitter", "YouTube", "Email"])

    if st.button("Post to Social Media"):
        print(f"social_media_post : {st.session_state.social_media_post_text} | social_media_platform : {social_media_platform}")
        response = marketing_agent.run_campaign(
            formatted_prompt, 
            actions=["social_media_post"], 
            modifications={"social_media_post": st.session_state.social_media_post_text, "social_media_platform": social_media_platform}
        )
        print(f"RESPONSE : {response}")
        if "social_media_post_result" in response and response["social_media_post_result"]:
            st.success(f"✅ Successfully posted to {social_media_platform}!")
        else:
            st.error(f"❌ Failed to post to {social_media_platform}.")