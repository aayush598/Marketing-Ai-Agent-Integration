def generate_campaign(self, product_name, product_features, description, audience, platform):
        """Generate a marketing campaign with ad copy and images."""

        # Generate ad copy using Gemini API
        ad_copy = self.generate_ad_copy(product_name, product_features, description, audience, platform)

        # Try to get images via web scraping first
        images = self.scrape_images_with_serpapi(product_name, product_features)

        # If no images found via scraping, generate images with Gemini
        if not images or images[0].startswith("Could not"):
            images = self.generate_images_with_gemini(product_name, product_features, description, audience, platform)

        return ad_copy, images