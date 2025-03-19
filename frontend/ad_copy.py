import streamlit as st
from agents.MarketingAgent import MarketingAgent

def display_ad_copy_section():
    """Displays the ad copy generation UI."""
    st.title("📢 Generate Ad Copy")

    if "formatted_prompt" not in st.session_state:
        st.warning("⚠️ Please enter product details in the **Input Form** first.")
        return

    formatted_prompt = st.session_state["formatted_prompt"]
    marketing_agent = MarketingAgent(groq_api_key="your_api_key", serpapi_key="your_serp_api_key")

    if st.button("Generate Ad Copy Structure"):
        response = marketing_agent.run_campaign(formatted_prompt, actions=["ad_copy"])
        st.session_state["ad_copy_structure"] = response.get("ad_copy_structure", "")

    if "ad_copy_structure" in st.session_state and st.session_state["ad_copy_structure"]:
        st.subheader("📑 Suggested Ad Copy Structure")
        st.write(st.session_state["ad_copy_structure"])

        st.text_area("Modify Ad Copy Structure (Optional):", key="ad_copy_modifications")

        if st.button("Modify Ad Copy Structure"):
            response = marketing_agent.run_campaign(
                formatted_prompt,
                actions=["ad_copy"],
                modifications={
                    "ad_copy_structure": st.session_state["ad_copy_structure"], 
                    "ad_copy_modifications": st.session_state["ad_copy_modifications"]
                }
            )
            st.session_state["ad_copy_structure"] = response["ad_copy_structure"]
            st.rerun()

        if st.button("Confirm & Generate Ad Copy"):
            response = marketing_agent.run_campaign(
                formatted_prompt,
                actions=["ad_copy"],
                modifications={"ad_copy_structure": st.session_state["ad_copy_structure"]},
                confirm_final=True
            )
            st.session_state["ad_copy_text"] = response["ad_copy"]
            st.rerun()

    # ✅ **Final Ad Copy Section with Modification Option**
    if "ad_copy_text" in st.session_state and st.session_state["ad_copy_text"]:
        st.subheader("✅ Final Ad Copy")
        st.markdown(st.session_state["ad_copy_text"], unsafe_allow_html=True)

        # ✅ **Add a Text Area for Modifying the Final Ad Copy**
        st.text_area("Modify Final Ad Copy (Optional):", key="generated_ad_copy_modifications")

        # ✅ **Button to Modify the Final Ad Copy**
        if st.button("Modify Final Ad Copy"):
            response = marketing_agent.run_campaign(
                formatted_prompt,
                actions=["ad_copy"],
                modifications={
                    "ad_copy": st.session_state["ad_copy_text"], 
                    "generated_ad_copy_modifications": st.session_state["generated_ad_copy_modifications"]
                }
            )
            st.session_state["ad_copy_text"] = response["ad_copy"]
            st.rerun()

        # ✅ **Download Ad Copy as a Text File**
        ad_copy_text = st.session_state["ad_copy_text"]
        st.download_button(
            label="📥 Download Ad Copy",
            data=ad_copy_text,
            file_name="ad_copy.txt",
            mime="text/plain"
        )
