import streamlit as st
from campaign import generate_campaign
from audience import get_target_audience
import google.generativeai as genai

gemini_text_model = genai.GenerativeModel('gemini-1.5-pro')

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
if "blog_info" not in st.session_state:
    st.session_state.blog_info = None
if "blog_post_text" not in st.session_state:
    st.session_state.blog_post_text = ""
if "blog_modifications" not in st.session_state:
    st.session_state.blog_modifications = ""

if "video_script_info" not in st.session_state:
    st.session_state.video_script_info = None
if "video_script_text" not in st.session_state:
    st.session_state.video_script_text = ""
if "video_script_modifications" not in st.session_state:
    st.session_state.video_script_modifications = ""

# Define session states
if "social_media_info" not in st.session_state:
    st.session_state.social_media_info = None
if "social_media_post_text" not in st.session_state:
    st.session_state.social_media_post_text = ""
if "social_media_modifications" not in st.session_state:
    st.session_state.social_media_modifications = ""


# Prepare formatted_prompt (Moved outside button scope)
if product_name and product_features and description and audience and platform and selected_actions:
    product_features = [feature.strip() for feature in product_features.split(',')]
    formatted_prompt = [product_name, product_features, description, audience, platform]
else:
    formatted_prompt = None  # Ensures it's not used before input validation

# Button to start the campaign
if st.button("Generate Campaign"):
    if formatted_prompt:
        # Generate initial blog structure if "blog_post" is selected
        if "blog_post" in selected_actions:
            response = gemini_text_model.generate_content(
                f"""
                Provide only the following structured details for a blog post:
                - Suitable Tone
                - SEO Optimization Techniques
                - Recommended Content Length
                - Content Headings only (Introduction, Problem, Solution, Features, Benefits, Conclusion, CTA)
                - Do not include any further details in content heading section except the headings
                - Headings must not be greater than 3-4 words
                
                Product: {product_name}
                Features: {product_features}
                Target Audience: {audience}
                Platform: {platform}
                """
            )
            st.session_state.blog_info = response.text
            st.rerun()
        elif "video_script" in selected_actions:
            response = gemini_text_model.generate_content(
                f"""
                Provide only the following structured details for a video script:
                - Suitable Tone
                - Best Platform for Posting
                - Recommended Video Length
                - Content Headings only (Hook, Problem, Solution, Features, Social Proof, CTA)
                - Do not include any further details in content heading secting except the headings
                - Headings must not be greated than 3-4 words
                
                Product: {product_name}
                Features: {product_features}
                Target Audience: {audience}
                Platform: {platform}
                """
            )
            st.session_state.video_script_info = response.text
            st.rerun()
        elif "social_media_post" in selected_actions:
            response = gemini_text_model.generate_content(
                f"""
                For a social media post about:
                - Product: {product_name}
                - Features: {product_features}
                - Target Audience: {audience}
                
                Provide ONLY the following details:
                1️⃣ **Engagement Strategies**: (e.g., storytelling, CTA, question-based)  
                2️⃣ **Use of Emojis & Readability**: (How to make the post visually appealing, scannable)  
                3️⃣ **Best Tone**: (Casual, professional, humorous, inspiring, persuasive, etc.)  

                🚨 *DO NOT* include the full post or any other details. Focus only on these aspects. 
                """
            )

            st.session_state.social_media_info = response.text
            st.rerun()
    else:
        st.warning("Please fill in all fields and select at least one action.")

if st.session_state.blog_info:
    st.subheader("Suggested Blog Info")
    st.text_area("Blog Details", st.session_state.blog_info, height=300)
    
    st.session_state.blog_modifications = st.text_area(
        "Modify Blog Info (Before Generation):",
        st.session_state.blog_modifications
    )
    
    if st.button("Modify Info"):
        if st.session_state.blog_modifications:
            modified_response = gemini_text_model.generate_content(
                f"""
                Modify the following blog post details based on user input:
                {st.session_state.blog_info}
                
                Modifications: {st.session_state.blog_modifications}
                
                Instructions:
                - Suitable Tone
                - SEO Optimization Techniques
                - Recommended Content Length
                - Content Headings only (Introduction, Problem, Solution, Features, Benefits, Conclusion, CTA)
                - Do not include any further details in content heading section except the headings
                - Headings must not be greater than 3-4 words
                """
            )
            st.session_state.blog_info = modified_response.text
            st.rerun()
    
    if st.button("Confirm & Generate Blog"):
        response = gemini_text_model.generate_content(
            f"""
            Generate a blog post based on the following details:
            {st.session_state.blog_info}
            """
        )
        st.session_state.blog_post_text = response.text
        st.rerun()

if st.session_state.blog_post_text:
    st.subheader("Generated Blog Post")
    st.text_area("Blog Content", st.session_state.blog_post_text, height=400)


if st.session_state.video_script_info:
    st.subheader("Suggested Video Script Info")
    st.text_area("Script Info", st.session_state.video_script_info, height=300)

    st.session_state.video_script_modifications = st.text_area(
        "Modify Script Info (Before Generation):",
        st.session_state.video_script_modifications
    )

    if st.button("Modify Info"):
        if st.session_state.video_script_modifications:
            modified_response = gemini_text_model.generate_content(
                f"""
                Modify the following video script details based on user input:
                {st.session_state.video_script_info}

                Modifications: {st.session_state.video_script_modifications}

                Instructions : 
                 Provide only the following structured details for a video script:
                - Suitable Tone
                - Best Platform for Posting
                - Recommended Video Length
                - Content Headings only (Hook, Problem, Solution, Features, Social Proof, CTA)
                - Do not include any further details in content heading secting except the headings
                - Headings must not be greated than 3-4 words
                """
            )
            st.session_state.video_script_info = modified_response.text
            st.rerun()

    if st.button("Confirm & Generate Video Script"):
        response = gemini_text_model.generate_content(
            f"""
            Generate a video script based on the following details:
            {st.session_state.video_script_info}
            """
        )
        st.session_state.video_script_text = response.text
        st.rerun()

if st.session_state.video_script_text:
    st.subheader("Generated Video Script")
    st.text_area("Video Script", st.session_state.video_script_text, height=300)

    # ✅ Providing a single input field for modification at the end
    st.session_state.video_script_modifications = st.text_area(
        "Modify Script (Optional):", 
        st.session_state.video_script_modifications
    )

    if st.button("Modify Script") and st.session_state.video_script_modifications:
        response = gemini_text_model.generate_content(
            f"""
            Modify the following video script based on user input:
            {st.session_state.video_script_text}
            
            Modifications: {st.session_state.video_script_modifications}
            """
        )
        st.session_state.video_script_text = response.text
        st.rerun()

if st.session_state.social_media_info:
    st.subheader("Suggested Social Media Post Info")
    st.text_area("Post Info", st.session_state.social_media_info, height=300)

    st.session_state.social_media_modifications = st.text_area(
        "Modify Post Info (Before Generation):",
        st.session_state.social_media_modifications
    )

    if st.button("Modify Info"):
        if st.session_state.social_media_modifications:
            modified_response = gemini_text_model.generate_content(
                f"""
                Modify the following social media post details based on user input:
                {st.session_state.social_media_info}

                Modifications: {st.session_state.social_media_modifications}

                Provide ONLY the following details:
                1️⃣ **Engagement Strategies**: (e.g., storytelling, CTA, question-based)  
                2️⃣ **Use of Emojis & Readability**: (How to make the post visually appealing, scannable)  
                3️⃣ **Best Tone**: (Casual, professional, humorous, inspiring, persuasive, etc.)  

                🚨 *DO NOT* include the full post or any other details. Focus only on these aspects. 
                
                """
            )
            st.session_state.social_media_info = modified_response.text
            st.rerun()

    if st.button("Confirm & Generate Social Media Post"):
        response = gemini_text_model.generate_content(
            f"""
            Generate a detailed social media post based on the following structured details:
            {st.session_state.social_media_info}
            """
        )
        st.session_state.social_media_post_text = response.text
        st.rerun()

if st.session_state.social_media_post_text:
    st.subheader("Generated Social Media Post")
    st.text_area("Social Media Post", st.session_state.social_media_post_text, height=300)

    st.session_state.social_media_modifications = st.text_area(
        "Modify Post (Optional):", 
        st.session_state.social_media_modifications
    )

    if st.button("Modify Post") and st.session_state.social_media_modifications:
        response = gemini_text_model.generate_content(
            f"""
            Modify the following social media post based on user input:
            {st.session_state.social_media_post_text}
            
            Modifications: {st.session_state.social_media_modifications}
            """
        )
        st.session_state.social_media_post_text = response.text
        st.rerun()