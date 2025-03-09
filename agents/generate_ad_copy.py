def generate_ad_copy(self, product_name, product_features, description, audience, platform):
        """Generate ad copy using Gemini model."""
        try:
            prompt = f"""
            Create compelling and engaging ad copy for a marketing campaign with the following details:

            Product: {product_name}
            Features: {product_features}
            Description: {description}
            Target Audience: {audience}
            Platform: {platform}

            The ad copy should be concise, persuasive, and tailored to the specific platform.
            Include a catchy headline, key benefits, and a clear call to action.
            """

            response = self.gemini_text_model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Error generating ad copy: {str(e)}")
            return f"Check out {product_name} with {product_features}! Perfect for {audience} on {platform}."
