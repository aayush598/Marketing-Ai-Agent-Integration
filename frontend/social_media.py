import streamlit as st
from agents.MarketingAgent import MarketingAgent

def display_social_media_section():
    """Displays the social media post generation UI."""
    st.title("📢 Generate Social Media Post")

    if "formatted_prompt" not in st.session_state:
        st.warning("⚠️ Please enter product details in the **Input Form** first.")
        return

    formatted_prompt = st.session_state["formatted_prompt"]
    marketing_agent = MarketingAgent(groq_api_key="your_api_key", serpapi_key="your_serp_api_key")

    if st.button("Generate Social Media Post"):
        response = marketing_agent.run_campaign(formatted_prompt, actions=["social_media_post"])
        st.session_state["social_media_info"] = response.get("social_media_structure", "")

    if "social_media_info" in st.session_state and st.session_state["social_media_info"]:
        st.subheader("📑 Suggested Social Media Post")
        st.write(st.session_state["social_media_info"])

        st.text_area("Modify Social Media Post (Optional):", key="social_media_modifications")

        if st.button("Modify Social Media Post"):
            response = marketing_agent.run_campaign(
                formatted_prompt,
                actions=["social_media_post"],
                modifications={"social_media_structure": st.session_state["social_media_info"], "social_media_modifications": st.session_state["social_media_modifications"]}
            )
            st.session_state["social_media_info"] = response["social_media_structure"]
            st.rerun()

        if st.button("Confirm & Generate Social Media Post"):
            response = marketing_agent.run_campaign(
                formatted_prompt,
                actions=["social_media_post"],
                modifications={"social_media_structure": st.session_state["social_media_info"]},
                confirm_final=True
            )
            st.session_state["social_media_post_text"] = response["social_media_post"]
            st.rerun()

        if "social_media_post_text" in st.session_state and st.session_state["social_media_post_text"]:
            st.subheader("✅ Final Social Media Post")
            st.markdown(st.session_state["social_media_post_text"], unsafe_allow_html=True)

            # ✅ **Dropdown for Social Media Platform Selection**
            social_media_platform = st.selectbox("📌 Select Platform to Post:", ["Twitter", "YouTube", "Email"])

            # ✅ Button to post to selected social media platform
            if st.button("🚀 Post to Social Media"):
                response = marketing_agent.run_campaign(
                    formatted_prompt, 
                    actions=["social_media_post"], 
                    modifications={
                        "social_media_post": st.session_state["social_media_post_text"], 
                        "social_media_platform": social_media_platform
                    }
                )

                # ✅ Handle response and show success or failure message
                if "social_media_post_result" in response and response["social_media_post_result"]:
                    st.success(f"✅ Successfully posted to {social_media_platform}!")
                else:
                    st.error(f"❌ Failed to post to {social_media_platform}.")
