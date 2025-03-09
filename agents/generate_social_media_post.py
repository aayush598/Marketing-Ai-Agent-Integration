def generate_social_media_post(self, product_name, product_features, description, audience, platform):
        """Generate social media captions tailored for the platform."""
        prompt = f"""
        Create an engaging social media post for:
        Product: {product_name}
        Features: {product_features}
        Target Audience: {audience}
        Platform: {platform}

        Keep it short, catchy, and aligned with current social media trends.
        """
        response = self.gemini_text_model.generate_content(prompt)
        return response.text