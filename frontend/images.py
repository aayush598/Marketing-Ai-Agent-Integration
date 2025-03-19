import streamlit as st
from agents.MarketingAgent import MarketingAgent

def display_images_section():
    """Displays the UI for generating and scraping images."""
    st.title("🖼️ Generate & Scrape Images")

    if "formatted_prompt" not in st.session_state:
        st.warning("⚠️ Please enter product details in the **Input Form** first.")
        return

    formatted_prompt = st.session_state["formatted_prompt"]
    marketing_agent = MarketingAgent(groq_api_key="your_api_key", serpapi_key="your_serp_api_key")

    # ✅ Image Generation
    if st.button("Generate AI Images"):
        response = marketing_agent.run_campaign(formatted_prompt, actions=["generated_images"])
        st.session_state["generated_images"] = response.get("generated_images", [])

    if "generated_images" in st.session_state and st.session_state["generated_images"]:
        st.subheader("🎨 AI-Generated Images")
        for img_path in st.session_state["generated_images"]:
            st.image(img_path, caption="Generated Image", use_column_width=True)
        
        # ✅ Button to Download Images
        for img_path in st.session_state["generated_images"]:
            with open(img_path, "rb") as img_file:
                st.download_button(label="📥 Download Image", data=img_file, file_name=img_path.split("/")[-1], mime="image/png")
