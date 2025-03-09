def generate_hashtags(self, product_name, product_features, description, audience, platform):
        """Generate trending hashtags related to the product."""
        prompt = f"""
        Generate a list of trending and relevant hashtags for:
        Product: {product_name}
        Features: {product_features}
        Platform: {platform}

        Include industry-specific, high-engagement hashtags.
        """
        response = self.gemini_text_model.generate_content(prompt)
        return response.text