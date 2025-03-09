from social_media.twitter_post import TwitterClient

class SocialMediaManager:
    def __init__(self):
        """Initialize social media managers with necessary credentials."""
        self.platforms = {
            "twitter": TwitterClient(),  # ✅ No need to pass credentials
            # "linkedin": LinkedInClient(),  # Future
            # "facebook": FacebookClient()   # Future
        }

    def post(self, platform, text):
        """Handles posting to different social media platforms."""
        platform = platform.lower()
        if platform in self.platforms:
            return self.platforms[platform].post(text)
        else:
            print(f"❌ Platform '{platform}' is not yet supported.")
            return None
