from agents.generate_campaign import generate_campaign
from agents.generate_ad_copy import generate_ad_copy
from agents.scrape_images_with_serpapi import scrape_images_with_serpapi
from agents.generate_images_with_gemini import generate_images_with_gemini
from agents.generate_blog import generate_blog
from agents.generate_video_script import generate_video_script
from agents.generate_social_media_post import generate_social_media_post
from agents.generate_hashtags import generate_hashtags
import google.generativeai as genai

class MarketingAgent:
    def __init__(self, groq_api_key, serpapi_key):
        self.groq_api_key = groq_api_key
        self.serpapi_key = serpapi_key
        self.gemini_text_model = genai.GenerativeModel('gemini-1.5-pro')
        self.gemini_vision_model = genai.GenerativeModel('gemini-1.5-pro')

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

        product_name, product_features, description, audience, platform = prompt

        # Map action names to their respective functions
        action_map = {
            "campaign_idea": lambda: generate_campaign(self,product_name, product_features, description, audience, platform),
            "ad_copy": lambda: generate_ad_copy(self,product_name, product_features, description, audience, platform),
            "blog_post": lambda: generate_blog(self,product_name, product_features, description, audience, platform),
            "video_script": lambda: generate_video_script(self,product_name, product_features, description, audience, platform),
            "social_media_post": lambda: generate_social_media_post(self,product_name, product_features, description, audience, platform),
            "hashtags": lambda: generate_hashtags(self,product_name, product_features, description, audience, platform),
            "scraped_images": lambda: scrape_images_with_serpapi(self,product_name, product_features, description, audience, platform),
            "generated_images": lambda: generate_images_with_gemini(self,product_name, product_features, description, audience, platform),
        }

        # Execute only the selected actions
        for action in actions:
            if action in action_map:
                results[action] = action_map[action]()


        return results
