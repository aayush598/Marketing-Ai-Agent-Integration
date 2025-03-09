def generate_blog(self, product_name, product_features, description, audience, platform):
        """Generate a blog post tailored for the target audience and platform."""
        prompt = f"""
        Write a detailed, engaging blog post about:
        Product: {product_name}
        Features: {product_features}
        Description: {description}
        Target Audience: {audience}
        Platform: {platform}

        The blog should be SEO-friendly, informative, and engaging, aligned with the latest market trends.
        """
        response = self.gemini_text_model.generate_content(prompt)
        return response.text