from serpapi import GoogleSearch
import pathlib
from urllib.parse import urlparse
import urllib

def scrape_images_with_serpapi(self, product_name, product_features, description, audience, platform):
        """Scrape images related to the product using SerpAPI."""
        try:
            print(f"Attempting to scrape images for {product_name}")
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
                        # Parse URL to get file extension
                        parsed_url = urlparse(img_url)
                        path = parsed_url.path
                        ext = pathlib.Path(path).suffix
                        if not ext:
                            ext = '.jpg'  # Default extension

                        # Download and save the image
                        image_path = f"generated_images/{product_name.replace(' ', '')}{i}{ext}"
                        urllib.request.urlretrieve(img_url, image_path)
                        downloaded_images.append(image_path)
                        print(f"Downloaded image: {image_path}")
                    except Exception as e:
                        print(f"Error downloading image {img_url}: {str(e)}")

                if downloaded_images:
                    return downloaded_images

            return ["Could not scrape any relevant images."]
        except Exception as e:
            print(f"Error scraping images with SerpAPI: {str(e)}")
            return ["Could not scrape images. Falling back to image generation."]
