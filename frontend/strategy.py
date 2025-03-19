import streamlit as st

def display_strategy_section(marketing_agent, formatted_prompt):
    """Handles strategy development for marketing campaigns."""
    if st.session_state.get("strategy_info"):
        st.subheader("📌 Suggested Strategy Plan")
        st.text_area("Strategy Details", st.session_state.strategy_info, height=250)

        st.session_state.strategy_modifications = st.text_area(
            "Modify Strategy (Before Generation):", st.session_state.strategy_modifications
        )

        if st.button("Modify Strategy"):
            response = marketing_agent.run_campaign(
                formatted_prompt,
                actions=["strategy"],
                modifications={"strategy_structure": st.session_state.strategy_info, "strategy_modifications": st.session_state.strategy_modifications}
            )
            st.session_state.strategy_info = response["strategy_structure"]
            st.rerun()

        if st.button("Confirm & Generate Strategy"):
            response = marketing_agent.run_campaign(
                formatted_prompt,
                actions=["strategy"],
                modifications={"strategy_structure": st.session_state.strategy_info},
                confirm_final=True
            )
            st.session_state.strategy_text = response["strategy"]
            st.rerun()

    if st.session_state.get("strategy_text"):
        st.subheader("Generated Strategy Plan")
        st.markdown(st.session_state.strategy_text, unsafe_allow_html=True)
