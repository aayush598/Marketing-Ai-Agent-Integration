import streamlit as st

def display_blog_section(marketing_agent, formatted_prompt):
    """Handles blog structure and modification."""
    if st.session_state.get("blog_info"):
        st.subheader("📑 Suggested Blog Outline")
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

        st.download_button(
            label="📥 Download Blog Outline",
            data=st.session_state.blog_info,
            file_name="blog_outline.txt",
            mime="text/plain"
        )

    if st.session_state.get("blog_post_text"):
        st.subheader("Generated Blog Post")
        # ✅ Render the blog HTML properly in Streamlit
        st.components.v1.html(st.session_state.blog_post_text, height=800, scrolling=True)
        # st.markdown(st.session_state.blog_post_text, unsafe_allow_html=True)
        st.download_button(
            label="📥 Download Blog as HTML",
            data=st.session_state.blog_post_text,
            file_name="generated_blog.html",
            mime="text/html"
        )
