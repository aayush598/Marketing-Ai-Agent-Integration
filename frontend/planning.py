import streamlit as st
import json
from agents.MarketingAgent import MarketingAgent

def display_planning_section():
    """Displays the UI for the marketing planning phase."""
    st.title("📅 Marketing Planning")

    if "formatted_prompt" not in st.session_state:
        st.warning("⚠️ Please enter product details in the **Input Form** first.")
        return

    formatted_prompt = st.session_state["formatted_prompt"]
    marketing_agent = MarketingAgent(groq_api_key="your_api_key", serpapi_key="your_serp_api_key")

    # ✅ Generate Planning Data
    if st.button("📝 Generate Planning Details"):
        response = marketing_agent.run_campaign(formatted_prompt, actions=["planning"])
        st.session_state["planning_info"] = response.get("planning_results", "")

    # ✅ Display the generated planning content
    if "planning_info" in st.session_state and st.session_state["planning_info"]:
        st.subheader("📌 Suggested Marketing Planning")

        # Convert JSON string to dictionary
        try:
            planning_data = json.loads(st.session_state["planning_info"])
            for section, content in planning_data.items():
                with st.expander(f"📌 {section.replace('_', ' ').title()}"):
                    st.markdown(content, unsafe_allow_html=True)
        except json.JSONDecodeError:
            st.error("❌ Error: Unable to parse planning data.")

        # # ✅ Modify Planning Section
        # st.text_area("Modify Planning Details (Optional):", key="planning_modifications")

        # if st.button("✏️ Modify Planning"):
        #     response = marketing_agent.run_campaign(
        #         formatted_prompt,
        #         actions=["planning"],
        #         modifications={"planning": st.session_state["planning_info"], "planning_modifications": st.session_state["planning_modifications"]}
        #     )
        #     st.session_state["planning_info"] = response["planning"]
        #     st.rerun()

        # # ✅ Generate the final marketing plan
        # if st.button("✅ Confirm & Generate Marketing Plan"):
        #     response = marketing_agent.run_campaign(
        #         formatted_prompt,
        #         actions=["planning"],
        #         modifications={"planning": st.session_state["planning_info"]},
        #         confirm_final=True
        #     )
        #     st.session_state["planning_text"] = response["planning"]
        #     st.rerun()

    # # ✅ Show Final Marketing Plan
    # if "planning_text" in st.session_state and st.session_state["planning_text"]:
    #     st.subheader("📖 Generated Marketing Plan")
    #     st.markdown(st.session_state["planning_text"], unsafe_allow_html=True)

    #     # ✅ Download Planning Report
    #     st.download_button(
    #         label="📥 Download Marketing Plan",
    #         data=st.session_state["planning_text"],
    #         file_name="marketing_plan.html",
    #         mime="text/html"
    #     )
