import streamlit as st

def display_ad_copy_section(marketing_agent, formatted_prompt):
    """Handles ad copy generation and modification."""
    if st.session_state.get("ad_copy_info"):
        st.subheader("📝 Suggested Ad Copy")
        st.text_area("Ad Copy Details", st.session_state.ad_copy_info, height=200)

        st.session_state.ad_copy_modifications = st.text_area(
            "Modify Ad Copy (Before Generation):", st.session_state.ad_copy_modifications
        )

        if st.button("Modify Ad Copy"):
            response = marketing_agent.run_campaign(
                formatted_prompt,
                actions=["ad_copy"],
                modifications={"ad_copy_structure": st.session_state.ad_copy_info, "ad_copy_modifications": st.session_state.ad_copy_modifications}
            )
            st.session_state.ad_copy_info = response["ad_copy_structure"]
            st.rerun()

        if st.button("Confirm & Generate Ad Copy"):
            response = marketing_agent.run_campaign(
                formatted_prompt,
                actions=["ad_copy"],
                modifications={"ad_copy_structure": st.session_state.ad_copy_info},
                confirm_final=True
            )
            st.session_state.ad_copy_text = response["ad_copy"]
            st.rerun()

    if st.session_state.get("ad_copy_text"):
        st.subheader("Generated Ad Copy")
        st.markdown(st.session_state.ad_copy_text, unsafe_allow_html=True)
