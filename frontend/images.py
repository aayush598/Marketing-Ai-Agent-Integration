import streamlit as st

def display_images_section():
    """Displays scraped or generated images in the UI."""
    if st.session_state.get("scraped_images"):
        st.subheader("📸 Scraped Images")
        for img_path in st.session_state.scraped_images:
            st.image(img_path, caption=img_path, use_column_width=True)

    if st.session_state.get("generated_images"):
        st.subheader("🖼️ AI-Generated Images")
        for img_path in st.session_state.generated_images:
            st.image(img_path, caption=img_path, use_column_width=True)
