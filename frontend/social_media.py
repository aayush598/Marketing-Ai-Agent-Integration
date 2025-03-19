import streamlit as st

def display_social_media_section(marketing_agent, formatted_prompt):
    """Handles social media post generation."""
    if st.session_state.get("social_media_info"):
        st.subheader("📢 Suggested Social Media Post")
        st.text_area("Social Media Post Details", st.session_state.social_media_info, height=200)

        st.session_state.social_media_modifications = st.text_area(
            "Modify Social Media Post (Before Generation):", st.session_state.social_media_modifications
        )

        if st.button("Modify Social Media Post"):
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

    if st.session_state.get("social_media_post_text"):
        st.subheader("Generated Social Media Post")
        st.markdown(st.session_state.social_media_post_text, unsafe_allow_html=True)
