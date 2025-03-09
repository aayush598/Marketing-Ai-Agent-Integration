def generate_video_script(self, product_name, product_features, description, audience, platform):
        """Generate a video script for product marketing."""
        prompt = f"""
        Create a compelling video script for:
        Product: {product_name}
        Features: {product_features}
        Target Audience: {audience}
        Platform: {platform}

        The script should be engaging, persuasive, and include a call to action. It should fit within 60 seconds for short-form videos.
        """
        response = self.gemini_text_model.generate_content(prompt)
        return response.text