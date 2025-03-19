import streamlit as st
from agents.MarketingAgent import MarketingAgent

def display_strategy_section():
    """Displays the UI for marketing strategy generation."""
    st.title("📌 Marketing Strategy")

    if "formatted_prompt" not in st.session_state:
        st.warning("⚠️ Please enter product details in the **Input Form** first.")
        return

    formatted_prompt = st.session_state["formatted_prompt"]
    marketing_agent = MarketingAgent(groq_api_key="your_api_key", serpapi_key="your_serp_api_key")

    # ✅ Generate Strategy Data
    if st.button("Generate Strategy"):
        response = marketing_agent.run_campaign(formatted_prompt, actions=["strategy"])
        st.session_state["strategy_info"] = response.get("strategy", "")

    if "strategy_info" in st.session_state and st.session_state["strategy_info"]:
        st.subheader("📌 Generated Marketing Strategy")
        st.write(st.session_state["strategy_info"])

        # ✅ Modify Strategy Section
        st.text_area("Modify Strategy (Optional):", key="strategy_modifications")

        if st.button("Modify Strategy"):
            response = marketing_agent.run_campaign(
                formatted_prompt,
                actions=["strategy"],
                modifications={"strategy": st.session_state["strategy_info"], "strategy_modifications": st.session_state["strategy_modifications"]}
            )
            st.session_state["strategy_info"] = response["strategy"]
            st.rerun()

        # ✅ Download Strategy Report
        st.download_button(
            label="📥 Download Strategy Report",
            data=st.session_state["strategy_info"],
            file_name="marketing_strategy.txt",
            mime="text/plain"
        )
