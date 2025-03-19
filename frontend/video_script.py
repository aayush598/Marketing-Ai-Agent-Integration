import streamlit as st

def display_video_script_section(marketing_agent, formatted_prompt):
    """Handles video script generation."""
    if st.session_state.get("video_script_info"):
        st.subheader("🎬 Suggested Video Script Format")
        st.text_area("Video Script Details", st.session_state.video_script_info, height=300)

        st.session_state.video_script_modifications = st.text_area(
            "Modify Video Script (Before Generation):", st.session_state.video_script_modifications
        )

        if st.button("Modify Video Script"):
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

    if st.session_state.get("video_script_text"):
        st.subheader("Generated Video Script")
        st.markdown(st.session_state.video_script_text, unsafe_allow_html=True)
