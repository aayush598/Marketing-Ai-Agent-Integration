import streamlit as st
from audience import get_target_audience
from agents.MarketingAgent import MarketingAgent
import google.generativeai as genai
from config.config import GEMINI_API_KEY, SERPAPI_KEY, GROQ_API_KEY


genai.configure(api_key=GEMINI_API_KEY)

# Initialize MarketingAgent
marketing_agent = MarketingAgent(groq_api_key=GROQ_API_KEY, serpapi_key=SERPAPI_KEY)

# Define available actions
ACTIONS = [
    "strategy", 
    "campaign_idea",
    "ad_copy",
    "blog_post",
    "video_script",
    "social_media_post",
    "hashtags",
    "scraped_images",
    "generated_images",
    "monitor",
]

st.title("Marketing Campaign Generator")

# Collect input from the user
product_name = st.text_input("Product Name:")
product_features = st.text_area("Product Features (comma-separated):")
description = st.text_area("Campaign Description:")
audience = get_target_audience(product_name, product_features, description)
platform = st.selectbox("Select Platform:", ["Twitter", "LinkedIn", "Instagram", "Facebook", "YouTube", "Gmail", "Other"])

# Multi-select for actions
selected_actions = st.multiselect("Select Actions:", ACTIONS)

# Define session states
session_keys = [
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
        print(f"Response : {response}")
        if "ad_copy_structure" in response:
            st.session_state.ad_copy_structure = response["ad_copy_structure"]
        if "blog_structure" in response:
            st.session_state.blog_info = response["blog_structure"]
        if "video_script_structure" in response:
            st.session_state.video_script_info = response["video_script_structure"]
        if "social_media_structure" in response:
            st.session_state.social_media_info = response["social_media_structure"]
        if "scraped_images" in response:
            st.session_state.scraped_images = response["scraped_images"]
        if "generated_images" in response:
            st.session_state.generated_images = response["generated_images"]
        if "monitor_data" in response:
            st.session_state.monitor_data = response["monitor_data"]
        if "strategy" in response:
            st.session_state.strategy_data = response["strategy"]

        
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

### **🔹 Ad Copy Generation**
if st.session_state.ad_copy_structure:
    st.subheader("Suggested Ad Copy Format")
    st.text_area("Ad Copy Details", st.session_state.ad_copy_structure, height=300)

    # Modify ad copy format before full generation
    st.session_state.ad_copy_modifications = st.text_area(
        "Modify Ad Copy Format (Before Generation):", st.session_state.ad_copy_modifications
    )

    if st.button("Modify Ad Copy Format"):
        if st.session_state.ad_copy_modifications:
            response = marketing_agent.run_campaign(
                formatted_prompt,
                actions=["ad_copy"],
                modifications={"ad_copy_structure": st.session_state.ad_copy_structure, "ad_copy_modifications": st.session_state.ad_copy_modifications}
            )
            st.session_state.ad_copy_structure = response["ad_copy_structure"]
            st.rerun()

    if st.button("Confirm & Generate Ad Copy"):
        response = marketing_agent.run_campaign(
            formatted_prompt,
            actions=["ad_copy"],
            modifications={"ad_copy_structure": st.session_state.ad_copy_structure},
            confirm_final=True
        )
        st.session_state.ad_copy_text = response["ad_copy"]
        st.rerun()

if st.session_state.ad_copy_text:
    st.subheader("Generated Ad Copy")
    st.text_area("Final Ad Copy", st.session_state.ad_copy_text, height=400)

    # ✅ Adding an input field for modifying the generated ad copy
    st.session_state.ad_copy_modifications = st.text_area(
        "Modify Ad Copy (Optional):", st.session_state.ad_copy_modifications
    )

    if st.button("Modify Ad Copy"):
        response = marketing_agent.run_campaign(
            formatted_prompt,
            actions=["ad_copy"],
            modifications={
                "ad_copy": st.session_state.ad_copy_text,
                "generated_ad_copy_modifications": st.session_state.ad_copy_modifications
            }
        )
        st.session_state.ad_copy_text = response["ad_copy"]
        st.rerun()

    # ✅ **Dropdown for Social Media Platform Selection**
    social_media_platform = st.selectbox("Select Platform to Post:", ["Twitter", "YouTube", "Email"])

    if st.button("Post Ad Copy to Social Media"):
        print(f"Ad Copy: {st.session_state.ad_copy_text} | Platform: {social_media_platform}")
        response = marketing_agent.run_campaign(
            formatted_prompt,
            actions=["ad_copy"],
            modifications={"ad_copy": st.session_state.ad_copy_text, "social_media_platform": social_media_platform}
        )
        print(f"Response: {response}")
        if "ad_copy_result" in response and response["ad_copy_result"]:
            st.success(f"✅ Successfully posted to {social_media_platform}!")
        else:
            st.error(f"❌ Failed to post to {social_media_platform}.")

# ✅ Display Scraped Images
if "scraped_images" in selected_actions:
    st.subheader(f"📸 Scraped Images for {product_name}")

    print(f"Scraped Images: {st.session_state}")
    if "scraped_images" in st.session_state and st.session_state.scraped_images:
        for idx, img_url in enumerate(st.session_state.scraped_images):
            st.image(img_url, caption=f"Scraped Image {idx+1}", use_column_width=True)
            st.text(f"📂 Saved Path: {img_url}")
    else:
        st.warning("No images scraped yet. Try generating again.")

# ✅ **Display Generated Images**
if st.session_state.generated_images:
    st.subheader("Generated Images")
    for img_path in st.session_state.generated_images:
        try:
            st.image(img_path, caption=f"Generated Image: {img_path}", use_column_width=True)
        except Exception as e:
            st.error(f"Error displaying image {img_path}: {e}")

### **🔹 Monitoring Dashboard**
if "monitor_data" in st.session_state:
    st.subheader("📊 Campaign Monitoring Report")

    monitor_data = st.session_state.monitor_data
    st.metric(label="📈 Sales Performance", value=monitor_data["sales_performance"])
    st.metric(label="🔄 Lead Conversion Rate", value=monitor_data["lead_conversion_rate"])
    st.metric(label="🗣 Customer Feedback", value=monitor_data["customer_feedback"])
    st.metric(label="⭐ Satisfaction Score", value=monitor_data["satisfaction_score"])
    st.metric(label="🏆 Competitor Activity", value=", ".join(monitor_data["competitor_activity"]))
    st.metric(label="💰 Budget Utilization", value=monitor_data["budget_utilization"])
    st.metric(label="⚙ Operational Efficiency", value=monitor_data["operational_efficiency"])

    st.success("✅ Monitoring data updated successfully!")

### **🔹 Strategy View**
if "strategy_data" in st.session_state:
    st.subheader("🎯 Marketing Strategy")

    strategy_data = st.session_state.strategy_data
    st.text_area("📌 Strategy Details", strategy_data, height=400)

    st.success("✅ Strategy generated successfully!")