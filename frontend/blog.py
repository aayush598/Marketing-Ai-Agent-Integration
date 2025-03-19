import streamlit as st
from agents.MarketingAgent import MarketingAgent

def display_blog_section():
    """Displays the blog post generation UI."""
    st.title("📝 Generate Blog Post")
    
    if "formatted_prompt" not in st.session_state:
        st.warning("⚠️ Please enter product details in the **Input Form** first.")
        return

    formatted_prompt = st.session_state["formatted_prompt"]
    marketing_agent = MarketingAgent(groq_api_key="your_api_key", serpapi_key="your_serp_api_key")

    if st.button("Generate Blog Structure"):
        response = marketing_agent.run_campaign(formatted_prompt, actions=["blog_post"])
        st.session_state["blog_info"] = response.get("blog_structure", "")
    
    if "blog_info" in st.session_state and st.session_state["blog_info"]:
        st.subheader("📑 Suggested Blog Structure")
        st.write(st.session_state["blog_info"])

        st.text_area("Modify Blog Structure (Optional):", key="blog_modifications")

        if st.button("Modify Blog"):
            response = marketing_agent.run_campaign(
                formatted_prompt,
                actions=["blog_post"],
                modifications={"blog_structure": st.session_state["blog_info"], "blog_modifications": st.session_state["blog_modifications"]}
            )
            st.session_state["blog_info"] = response["blog_structure"]
            st.rerun()

        if st.button("Confirm & Generate Blog"):
            response = marketing_agent.run_campaign(
                formatted_prompt,
                actions=["blog_post"],
                modifications={"blog_structure": st.session_state["blog_info"]},
                confirm_final=True
            )
            st.session_state["blog_post_text"] = response["blog_post"]
            st.rerun()

        if "blog_post_text" in st.session_state and st.session_state["blog_post_text"]:
            st.subheader("📖 Generated Blog Post")
            st.components.v1.html(st.session_state.blog_post_text, height=800, scrolling=True)

            # ✅ Provide Download Option for HTML File
            blog_html = st.session_state["blog_post_text"]
            blog_file_name = "generated_blog.html"
            
            st.download_button(
                label="📥 Download Blog as HTML",
                data=blog_html,
                file_name=blog_file_name,
                mime="text/html"
            )
