import streamlit as st

def display_planning_section(marketing_agent, formatted_prompt):
    """Handles planning phase of marketing strategy."""
    if st.session_state.get("planning_info"):
        st.subheader("📅 Suggested Marketing Planning")
        st.text_area("Planning Details", st.session_state.planning_info, height=250)

        st.session_state.planning_modifications = st.text_area(
            "Modify Planning Details (Before Generation):", st.session_state.planning_modifications
        )

        if st.button("Modify Planning"):
            response = marketing_agent.run_campaign(
                formatted_prompt,
                actions=["planning"],
                modifications={"planning_structure": st.session_state.planning_info, "planning_modifications": st.session_state.planning_modifications}
            )
            st.session_state.planning_info = response["planning_structure"]
            st.rerun()

        if st.button("Confirm & Generate Planning"):
            response = marketing_agent.run_campaign(
                formatted_prompt,
                actions=["planning"],
                modifications={"planning_structure": st.session_state.planning_info},
                confirm_final=True
            )
            st.session_state.planning_text = response["planning"]
            st.rerun()

    if st.session_state.get("planning_text"):
        st.subheader("Generated Marketing Plan")
        st.markdown(st.session_state.planning_text, unsafe_allow_html=True)
