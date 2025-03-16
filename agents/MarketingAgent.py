from agents.generate_campaign import generate_campaign
from agents.generate_ad_copy import modify_generated_ad_copy, modify_ad_copy_structure, generate_ad_copy_from_structure,generate_ad_copy_structure
from agents.scrape_images_with_serpapi import scrape_images_with_serpapi
from agents.generate_images_with_gemini import generate_images_with_gemini
from agents.generate_blog import generate_blog_structure, modify_blog_structure, generate_blog_from_structure, modify_generated_blog
from agents.generate_video_script import generate_video_script_from_structure, modify_generated_video_script, generate_video_script_structure, modify_video_script_structure
from agents.generate_social_media_post import generate_social_media_structure, modify_social_media_structure, generate_social_media_post_from_structure, modify_generated_social_media_post, post_social_media_content
from agents.generate_hashtags import generate_hashtags

import google.generativeai as genai

class MarketingAgent:
    def __init__(self, groq_api_key, serpapi_key):
        self.groq_api_key = groq_api_key
        self.serpapi_key = serpapi_key
        self.gemini_text_model = genai.GenerativeModel('gemini-2.0-flash-lite')
        self.gemini_vision_model = genai.GenerativeModel('gemini-2.0-flash-lite')

    def run_campaign(self, prompt, actions=None, modifications=None, confirm_final=False):
        """
        Run selected marketing actions based on the provided list.
        - Handles blog, video script, and social media post generation.
        - Applies modifications when requested.
        - Confirms final content when requested.
        """
        if not actions:
            return {}

        results = {}

        product_name, product_features, description, audience, platform = prompt

        # Map actions to respective functions
        action_map = {
            "campaign_idea": lambda: generate_campaign(self, product_name, product_features, description, audience, platform),
            "hashtags": lambda: generate_hashtags(self, product_name, product_features, description, audience, platform),
            "scraped_images": lambda: scrape_images_with_serpapi(self, product_name, product_features, description, audience, platform),
            "generated_images": lambda: generate_images_with_gemini(self, product_name, product_features, description, audience, platform),
        }

        # Handle Blog Generation
        if "blog_post" in actions:
            blog_data = modifications.get("blog_structure", None) if modifications else None
            blog_modifications = modifications.get("blog_modifications", None) if modifications else None
            blog_post_modifications = modifications.get("blog_post_modifications", None) if modifications else None
            
            if confirm_final and blog_data:
                results["blog_post"] = generate_blog_from_structure(blog_data)
            
            elif blog_modifications and blog_data:
                results["blog_structure"] = modify_blog_structure(blog_data, blog_modifications)

            elif blog_post_modifications and "blog_post" in modifications:
                results["blog_post"] = modify_generated_blog(modifications["blog_post"], blog_post_modifications)

            else:
                results["blog_structure"] = generate_blog_structure(product_name, product_features, description, audience, platform)

        # Handle Video Script Generation
        if "video_script" in actions:
            video_data = modifications.get("video_script_structure", None) if modifications else None
            video_modifications = modifications.get("video_script_modifications", None) if modifications else None
            generated_video_modifications = modifications.get("generated_video_script_modifications", None) if modifications else None

            if confirm_final and video_data:
                results["video_script"] = generate_video_script_from_structure(video_data)

            elif video_modifications and video_data:
                results["video_script_structure"] = modify_video_script_structure(video_data, video_modifications)

            elif generated_video_modifications and "video_script" in modifications:
                results["video_script"] = modify_generated_video_script(modifications["video_script"], generated_video_modifications)

            else:
                results["video_script_structure"] = generate_video_script_structure(product_name, product_features, description, audience, platform)

        # Handle Social Media Post Generation
        if "social_media_post" in actions:
            social_media_data = modifications.get("social_media_structure", None) if modifications else None
            social_media_modifications = modifications.get("social_media_modifications", None) if modifications else None
            generated_social_media_modifications = modifications.get("generated_social_media_post_modifications", None) if modifications else None
            social_media_platform = modifications.get("social_media_platform", None) if modifications else None
            social_media_post = modifications.get("social_media_post", None) if modifications else None

            if confirm_final and social_media_data:
                results["social_media_post"] = generate_social_media_post_from_structure(social_media_data)

            elif social_media_modifications and social_media_data:
                results["social_media_structure"] = modify_social_media_structure(social_media_data, social_media_modifications)

            elif generated_social_media_modifications and "social_media_post" in modifications:
                results["social_media_post"] = modify_generated_social_media_post(modifications["social_media_post"], generated_social_media_modifications)

            elif social_media_platform and social_media_post:
                results["social_media_post"] = social_media_post
            else:
                results["social_media_structure"] = generate_social_media_structure(product_name, product_features, description, audience, platform)

            print(f"results: {results}")
            # ✅ If platform is provided, post the content
            if social_media_platform and "social_media_post" in results:
                post_result = post_social_media_content(social_media_platform, results["social_media_post"])
                results["social_media_post_result"] = post_result

        # Handle Ad Copy Generation
        if "ad_copy" in actions:
            ad_copy_data = modifications.get("ad_copy_structure", None) if modifications else None
            ad_copy_modifications = modifications.get("ad_copy_modifications", None) if modifications else None
            generated_ad_copy_modifications = modifications.get("generated_ad_copy_modifications", None) if modifications else None
            ad_copy = modifications.get("ad_copy",None) if modifications else None

            print(f"ad_copy_data : {ad_copy_data} | ad_copy_modifications : {ad_copy_modifications} | generated_ad_copy_modifications : {generated_ad_copy_modifications} | ad_copy : {ad_copy}")

            if confirm_final and ad_copy_data:
                results["ad_copy"] = generate_ad_copy_from_structure(ad_copy_data)

            elif ad_copy_modifications and ad_copy_data:
                results["ad_copy_structure"] = modify_ad_copy_structure(ad_copy_data, ad_copy_modifications)

            elif generated_ad_copy_modifications and ad_copy:
                print(f"ad_copy : {ad_copy} | generated_ad_copy_modifications : {generated_ad_copy_modifications}")
                results["ad_copy"] = modify_generated_ad_copy(modifications["ad_copy"], generated_ad_copy_modifications)
                print(f"Result : {results}")

            else:
                results["ad_copy_structure"] = generate_ad_copy_structure(product_name, product_features, description, audience, platform)


        # Execute other actions
        for action in actions:
            if action in action_map:
                results[action] = action_map[action]()

        return results
