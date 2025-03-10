def generate_images_with_gemini(self, product_name, product_features, description, audience, platform):
        """Generate images using Gemini model's text-to-image capability."""
        try:
            print(f"Generating images with Gemini for {product_name}")

            prompt = f"""
            Create a detailed and visually appealing advertisement image for:

            Product: {product_name}
            Key Features: {product_features}
            Target Audience: {audience}
            Platform: {platform}

            Description: {description}

            The image should be high-quality, professional, and suitable for a marketing campaign.
            Make it visually striking, with good composition, and clearly showcase the product.

            Generate this as an SVG image that could be used in an advertisement.
            """

            response = self.gemini_vision_model.generate_content(prompt)

            print(f"resposne :{response}")

            # Check if response contains SVG code
            if "<svg" in response.text and "</svg>" in response.text:
                # Extract SVG content
                svg_content = response.text
                start_idx = svg_content.find("<svg")
                end_idx = svg_content.find("</svg>") + 6
                svg_content = svg_content[start_idx:end_idx]

                # Save the SVG file
                image_path = f"generated_images/{product_name.replace(' ', '')}{platform.replace(' ', '_')}.svg"
                with open(image_path, "w") as f:
                    f.write(svg_content)

                return [image_path]
            else:
                # Generate a text description of an image instead
                image_description = response.text

                # Create a simple placeholder image with the description
                from PIL import Image, ImageDraw, ImageFont
                img = Image.new('RGB', (800, 600), color=(73, 109, 137))
                d = ImageDraw.Draw(img)

                # Add text to the image
                d.text((10, 10), f"Product: {product_name}", fill=(255, 255, 255))
                d.text((10, 40), f"Image description:", fill=(255, 255, 255))

                # Break the description into multiple lines
                words = image_description.split()
                lines = []
                current_line = ""
                for word in words:
                    if len(current_line + " " + word) <= 80:
                        current_line += " " + word if current_line else word
                    else:
                        lines.append(current_line)
                        current_line = word
                if current_line:
                    lines.append(current_line)

                # Add the description lines to the image
                for i, line in enumerate(lines[:20]):  # Limit to 20 lines
                    d.text((10, 70 + i*20), line, fill=(255, 255, 255))

                # Save the image
                image_path = f"generated_images/{product_name.replace(' ', '')}{platform.replace(' ', '_')}.png"
                img.save(image_path)

                return [image_path]
        except Exception as e:
            print(f"Error generating images with Gemini: {str(e)}")
            return ["Could not generate image."]
    