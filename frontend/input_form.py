import streamlit as st
from audience import get_target_audience

def display_input_form():
    """Displays the input form and stores data in session state."""
    st.title("📌 Enter Campaign Details")

    with st.form("campaign_form"):
        product_name = st.text_input("Product Name:")
        product_features = st.text_area("Product Features (comma separated):")
        description = st.text_area("Product Description:")
        audience = get_target_audience(product_name, product_features, description)
        platform = st.selectbox("Platform:", ["Twitter", "LinkedIn", "Instagram", "Facebook", "YouTube", "Email", "Blog"])

        submit_button = st.form_submit_button("🚀 Save Inputs")

    if submit_button:
        st.session_state["formatted_prompt"] = (product_name, product_features.split(","), description, audience, platform)
        st.success("✅ Product details saved! Navigate to other sections to generate content.")
