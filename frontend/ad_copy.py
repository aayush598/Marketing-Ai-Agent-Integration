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
                modifications={"ad_copy_structure": st.session_state["ad_copy_structure"], "ad_copy_modifications": st.session_state["ad_copy_modifications"]}
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

        if "ad_copy_text" in st.session_state and st.session_state["ad_copy_text"]:
            st.subheader("✅ Final Ad Copy")
            st.markdown(st.session_state["ad_copy_text"], unsafe_allow_html=True)

            # # ✅ **Dropdown for Ad Posting Selection**
            # ad_platform = st.selectbox("📌 Select Platform to Post:", ["Google Ads", "Facebook Ads", "Instagram Ads"])

            # # ✅ Button to post to selected ad platform
            # if st.button("🚀 Post Ad Copy"):
            #     response = marketing_agent.run_campaign(
            #         formatted_prompt, 
            #         actions=["ad_copy"], 
            #         modifications={
            #             "ad_copy": st.session_state["ad_copy_text"], 
            #             "ad_platform": ad_platform
            #         }
            #     )

            #     # ✅ Handle response and show success or failure message
            #     if "ad_copy_post_result" in response and response["ad_copy_post_result"]:
            #         st.success(f"✅ Successfully posted to {ad_platform}!")
            #     else:
            #         st.error(f"❌ Failed to post to {ad_platform}.")
