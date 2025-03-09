from agents.generate_campaign import generate_campaign
from agents.generate_ad_copy import generate_ad_copy
from agents.scrape_images_with_serpapi import scrape_images
from agents.generate_images_with_gemini import generate_images
from agents.generate_blog import generate_blog
from agents.generate_video_script import generate_video_script
from agents.generate_social_media_post import generate_social_media_post
from agents.generate_hashtags import generate_hashtags

class MarketingAgent:
    def __init__(self, groq_api_key, serpapi_key):
        self.groq_api_key = groq_api_key
        self.serpapi_key = serpapi_key

    def run_campaign(self, prompt, actions=None):
        """
        Run selected marketing actions based on the provided list.
        If actions is None, an empty dictionary is returned.
        
        :param prompt: The prompt to generate marketing content.
        :param actions: List of actions to execute (e.g., ["campaign_idea", "ad_copy"]).
        :return: Dictionary containing only the requested results.
        """
        if actions is None:
            return {}

        results = {}

        # Map action names to their respective functions
        action_map = {
            "campaign_idea": lambda: generate_campaign(prompt),
            "ad_copy": lambda: generate_ad_copy(prompt),
            "blog_post": lambda: generate_blog(prompt),
            "video_script": lambda: generate_video_script(prompt),
            "social_media_post": lambda: generate_social_media_post(prompt),
            "hashtags": lambda: generate_hashtags(prompt),
            "scraped_images": lambda: scrape_images(prompt, self.serpapi_key),
            "generated_images": lambda: generate_images(prompt, self.groq_api_key),
        }

        # Execute only the selected actions
        for action in actions:
            if action in action_map:
                results[action] = action_map[action]()

        return results
