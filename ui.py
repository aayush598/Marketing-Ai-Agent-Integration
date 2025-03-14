import streamlit as st
from campaign import generate_campaign
from audience import get_target_audience

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
if "blog_structure" not in st.session_state:
    st.session_state.blog_structure = None
if "modifications" not in st.session_state:
    st.session_state.modifications = ""
if "final_blog" not in st.session_state:
    st.session_state.final_blog = None

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
            response = generate_campaign(formatted_prompt, ["blog_post"])
            st.session_state.blog_structure = response.get("blog_structure", "No structure generated.")
    else:
        st.warning("Please fill in all fields and select at least one action.")

# Show blog structure if generated
if st.session_state.blog_structure:
    st.subheader("Generated Blog Structure")
    st.text_area("Blog Structure", st.session_state.blog_structure, height=200, key="structure_display")

    # Allow user to modify the structure
    st.session_state.modifications = st.text_area("Modify Structure (Optional):", key="modification_input")

    # Button to modify structure
    # Button to modify structure
    if st.button("Modify Structure"):
        if formatted_prompt and st.session_state.modifications:
            if not st.session_state.blog_structure:
                st.warning("No blog structure available. Please generate the structure first.")
            else:
                modified_response = generate_campaign(
                    formatted_prompt, 
                    ["blog_post"], 
                    blog_modifications=st.session_state.modifications
                )
                
                # ✅ Ensure the modified structure is saved in session state
                if "blog_structure" in modified_response:
                    st.session_state.blog_structure = modified_response["blog_structure"]
                    st.rerun()  # 🔄 Force Streamlit to refresh the UI
                else:
                    st.warning("Modification failed. Try again.")
        else:
            st.warning("Enter modifications before clicking 'Modify Structure'.")

    # Confirm button to generate the final blog
    # Button to confirm structure and generate final blog
    if st.button("Confirm & Generate Blog"):
        if formatted_prompt and st.session_state.blog_structure:
            final_response = generate_campaign(
                formatted_prompt, 
                ["blog_post"], 
                blog_modifications=st.session_state.blog_structure, 
                confirm_blog=True
            )

            # ✅ Store final blog in session state
            st.session_state.final_blog = final_response.get("blog_post", "No blog generated.")
            st.rerun()  # 🔄 Force UI refresh to display the final blog
        else:
            st.warning("No final structure available. Please generate or modify the structure first.")

# Show the final blog after confirmation
if st.session_state.final_blog:
    st.subheader("Generated Blog")
    st.text_area("Final Blog Content", st.session_state.final_blog, height=400)
