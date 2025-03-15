from agents.generate_campaign import generate_campaign
from agents.generate_ad_copy import generate_ad_copy
from agents.scrape_images_with_serpapi import scrape_images_with_serpapi
from agents.generate_images_with_gemini import generate_images_with_gemini
from agents.generate_blog import generate_blog_structure, modify_blog_structure, generate_blog_from_structure
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

    def run_campaign(self, prompt, actions=None, blog_modifications=None, confirm_blog=False,social_media_modifications=None, confirm_social_media=False):
        """
        Run selected marketing actions based on the provided list.
        - Handles blog structure modification.
        - Ensures blog_structure exists before modification.
        """

        if actions is None:
            return {}

        results = {}

        product_name, product_features, description, audience, platform = prompt

        # Map actions to their respective functions
        action_map = {
            "campaign_idea": lambda: generate_campaign(self, product_name, product_features, description, audience, platform),
            "ad_copy": lambda: generate_ad_copy(self, product_name, product_features, description, audience, platform),
            "video_script": lambda: generate_video_script(self, product_name, product_features, description, audience, platform),
            "social_media_post": lambda: generate_social_media_post(self, product_name, product_features, description, audience, platform),
            "hashtags": lambda: generate_hashtags(self, product_name, product_features, description, audience, platform),
            "scraped_images": lambda: scrape_images_with_serpapi(self, product_name, product_features, description, audience, platform),
            "generated_images": lambda: generate_images_with_gemini(self, product_name, product_features, description, audience, platform),
        }

        # Blog Post Handling
        if "blog_post" in actions:
            if blog_modifications is None:
                # Step 1: Generate Initial Structure
                results["blog_structure"] = generate_blog_structure(self, product_name, product_features, description, audience, platform)
            elif not confirm_blog:
                # Step 2: Modify Structure (Ensure blog_structure exists)
                if "blog_structure" not in results:
                    results["blog_structure"] = generate_blog_structure(self, product_name, product_features, description, audience, platform)
                
                results["blog_structure"] = modify_blog_structure(self, results["blog_structure"], blog_modifications)
            else:
                # Step 3: Confirm & Generate Final Blog
                results["blog_post"] = generate_blog_from_structure(self, blog_modifications)

        if "social_media_post" in actions:
            response = self.gemini_text_model.generate_content(
                f"""
                For a social media post about:
                - Product: {product_name}
                - Features: {product_features}
                - Target Audience: {audience}
                
                Provide ONLY the following details:
                1️⃣ **Engagement Strategies**: (e.g., storytelling, CTA, question-based)  
                2️⃣ **Use of Emojis & Readability**: (How to make the post visually appealing, scannable)  
                3️⃣ **Best Tone**: (Casual, professional, humorous, inspiring, persuasive, etc.)  

                🚨 *DO NOT* include the full post or any other details. Focus only on these aspects. 
                """
            )
            results["social_media_post"] = response.text

        # Execute other actions
        for action in actions:
            if action in action_map and ((action != "blog_post") or (action != "social_media_post")):
                results[action] = action_map[action]()
        

        if "social_media_post" in actions and social_media_modifications:
            modified_response = self.gemini_text_model.generate_content(
                f"""
                Modify the following social media post details:
                {results.get("social_media_post", "")}
                
                Modifications: {social_media_modifications}
                """
            )
            results["social_media_post"] = modified_response.text

        if "social_media_post" in actions and confirm_social_media:
            final_response = self.gemini_text_model.generate_content(
                f"""
                Generate a final, polished social media post based on the structured details:
                {results.get("social_media_post", "")}
                """
            )
            results["social_media_post"] = final_response.text

        return results
