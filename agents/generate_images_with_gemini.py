import os
import requests
from PIL import Image, ImageDraw
from io import BytesIO
from urllib.parse import urlparse
import urllib
from config.config import HUGGINGFACE_API

class ImageGenerator:
    def __init__(self, gemini_model=None, huggingface_api_key=HUGGINGFACE_API, serpapi_key=None):
        """Initialize with Google Gemini model, Hugging Face API key, and SerpAPI key."""
        self.gemini_model = gemini_model  # Google Gemini Model Instance
        self.huggingface_api_key = huggingface_api_key  # Hugging Face API Key
        self.serpapi_key = serpapi_key  # SerpAPI Key for image scraping
        os.makedirs("generated_images", exist_ok=True)  # Ensure folder exists

    def generate_images_with_gemini(self, product_name, product_features, description, audience, platform):
        """Generate product images using Gemini API."""
        try:
            print(f"✨ Generating images with Gemini for {product_name}...")

            prompt = f"""
            Create a visually appealing advertisement image for:
            - Product: {product_name}
            - Key Features: {product_features}
            - Target Audience: {audience}
            - Platform: {platform}
            - Description: {description}
            Make it professional and high quality.
            """

            response = self.gemini_model.generate_content(prompt)

            if response and "<svg" in response.text and "</svg>" in response.text:
                # Extract SVG content
                start_idx = response.text.find("<svg")
                end_idx = response.text.find("</svg>") + 6
                svg_content = response.text[start_idx:end_idx]

                # Save as an SVG file
                image_path = f"generated_images/{product_name.replace(' ', '')}_{platform}.svg"
                with open(image_path, "w") as f:
                    f.write(svg_content)

                return [image_path]

        except Exception as e:
            print(f"⚠ Error generating with Gemini: {str(e)}")

        return ["Could not generate images."]

    def scrape_images_with_serpapi(self, product_name, product_features, description, audience, platform):
        """Scrape images related to the product using SerpAPI."""
        try:
            from serpapi import GoogleSearch  # Import only if available

            print(f"🔍 Scraping images for {product_name} using SerpAPI...")

            search_query = f"{product_name} {product_features} product"

            search_params = {
                "engine": "google_images",
                "q": search_query,
                "api_key": self.serpapi_key
            }

            search = GoogleSearch(search_params)
            results = search.get_dict()

            if "images_results" in results and len(results["images_results"]) > 0:
                image_urls = [item["original"] for item in results["images_results"][:3]]
                downloaded_images = []

                for i, img_url in enumerate(image_urls):
                    try:
                        parsed_url = urlparse(img_url)
                        ext = os.path.splitext(parsed_url.path)[1] or '.jpg'  # Get extension

                        # Download and save the image
                        image_path = f"generated_images/{product_name.replace(' ', '')}{i}{ext}"
                        urllib.request.urlretrieve(img_url, image_path)
                        downloaded_images.append(image_path)
                        print(f"✅ Downloaded image: {image_path}")
                    except Exception as e:
                        print(f"⚠ Error downloading image {img_url}: {str(e)}")

                return downloaded_images if downloaded_images else ["No images found."]
            
        except Exception as e:
            print(f"⚠ Error scraping images with SerpAPI: {str(e)}")
            return ["Could not scrape images."]

    def generate_placeholder_image(self, product_name, platform):
        """Creates a placeholder image when AI image generation fails."""
        print(f"❌ Could not generate an image. Creating a placeholder for {product_name}...")

        img = Image.new('RGB', (800, 600), color=(73, 109, 137))
        d = ImageDraw.Draw(img)
        d.text((10, 10), f"Product: {product_name}", fill=(255, 255, 255))
        d.text((10, 40), "Image could not be generated.", fill=(255, 255, 255))

        image_path = f"generated_images/{product_name.replace(' ', '')}_{platform}_placeholder.png"
        img.save(image_path)

        return [image_path]

    def generate_images(self, product_name, product_features, description, audience, platform):
        """Try to generate images with Gemini first, then Hugging Face, then fallback to scraping, and finally a placeholder."""
        images = self.generate_images_with_gemini(product_name, product_features, description, audience, platform)
        
        if "Could not generate images." in images and self.huggingface_api_key:
            images = self.generate_images_with_huggingface(product_name, product_features, description, audience, platform)

        if "Could not generate images." in images and self.serpapi_key:
            images = self.scrape_images_with_serpapi(product_name, product_features, description, audience, platform)

        if "Could not generate images." in images:
            images = self.generate_placeholder_image(product_name, platform)

        return images

    def generate_images_with_huggingface(self, product_name, product_features, description, audience, platform):
        """Generate images using Hugging Face API as a fallback."""
        try:
            print(f"⚡ Generating images with Hugging Face API for {product_name}...")

            url = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3.5-large"
            headers = {"Authorization": f"Bearer {self.huggingface_api_key}"}
            payload = {"inputs": f"High-quality marketing image of {product_name}. {description}"}

            response = requests.post(url, headers=headers, json=payload)

            if response.status_code == 200:
                img = Image.open(BytesIO(response.content))

                # Save the image
                image_path = f"generated_images/{product_name.replace(' ', '')}_{platform}.png"
                img.save(image_path)

                print(f"✅ Image generated successfully: {image_path}")
                return [image_path]

        except Exception as e:
            print(f"⚠ Error generating with Hugging Face API: {str(e)}")

        return ["Could not generate images."]


SERPAPI_KEY = "your_serpapi_key"  # Replace with your actual SerpAPI key
gemini_model = None  # Replace with Google Gemini model instance if available

image_generator = ImageGenerator(gemini_model, HUGGINGFACE_API, SERPAPI_KEY)

# Generate an image for a product
product_name = "iPhone X"
product_features = "Edge-to-edge display, Face ID, Wireless Charging"
description = "A revolutionary smartphone with advanced security and immersive display."
audience = "Tech enthusiasts aged 18-40"
platform = "Instagram"

# image_paths = image_generator.generate_images(product_name, product_features, description, audience, platform)

# # ✅ Display the generated image paths
# for path in image_paths:
#     print(f"📁 Image saved at: {path}")
