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

            print(f"Results in scrape : {results}")

            if "images_results" in results and len(results["images_results"]) > 0:
                image_urls = [item["original"] for item in results["images_results"][:3]]
                return image_urls

            return ["Could not scrape any relevant images."]
        except Exception as e:
            print(f"Error scraping images with SerpAPI: {str(e)}")
            return ["Could not scrape images. Falling back to image generation."]
