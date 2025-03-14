from config.config import GROQ_API_KEY, SERPAPI_KEY
from agents.MarketingAgent import MarketingAgent
from social_media.social_media_manager import SocialMediaManager

agent = MarketingAgent(GROQ_API_KEY, SERPAPI_KEY)
social_media_manager = SocialMediaManager()  # Social media handler

def generate_campaign(prompt, actions, blog_modifications=None, confirm_blog=False):
    """
    Generate marketing content based on selected actions.
    
    - Handles blog structure modification if applicable.
    - If `confirm_blog` is True, it generates the final blog.
    
    :param prompt: List containing product details.
    :param actions: List of actions to execute (e.g., ["campaign_idea", "ad_copy"]).
    :param blog_modifications: Optional input for modifying blog structure.
    :param confirm_blog: Boolean flag to confirm and generate final blog.
    :return: Dictionary containing the generated results.
    """
    if not prompt:
        return {"error": "Missing prompt"}

    if not actions or not isinstance(actions, list):
        return {"error": "Invalid or missing 'actions' list"}

    # Run marketing agent with blog modification handling
    result = agent.run_campaign(prompt, actions, blog_modifications, confirm_blog)

    # Check if a social media post should be published
    if "social_media_post" in result:
        platform = prompt[-1]  # Last item in prompt is platform (e.g., Twitter, LinkedIn)
        post_text = result["social_media_post"]

        # Post to the detected platform
        social_media_response = social_media_manager.post(platform, post_text)

        if social_media_response:
            result[f"{platform.lower()}_post_status"] = "Posted successfully"
        else:
            result[f"{platform.lower()}_post_status"] = "Failed to post"
    
    return result
