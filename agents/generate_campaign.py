from agents.generate_ad_copy import generate_ad_copy_structure 
from agents.scrape_images_with_serpapi import scrape_images_with_serpapi
from agents.generate_images_with_gemini import image_generator

def generate_campaign(self, product_name, product_features, description, audience, platform):
        """Generate a marketing campaign with ad copy and images."""

        # Generate ad copy using Gemini API
        ad_copy = generate_ad_copy_structure(self,product_name, product_features, description, audience, platform)

        # Try to get images via web scraping first
        images = scrape_images_with_serpapi(self, product_name, product_features, description, audience, platform)

        # If no images found via scraping, generate images with Gemini
        # if not images or images[0].startswith("Could not"):
        images = image_generator.generate_images(product_name, product_features, description, audience, platform)


        return ad_copy, images