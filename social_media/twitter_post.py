import tweepy
import os
from dotenv import load_dotenv

load_dotenv("./.env")

class TwitterClient:
    def __init__(self):
        """Initialize the Twitter API client using environment variables."""
        self.bearer_token = os.getenv("BEARER_TOKEN")
        self.consumer_key = os.getenv("CONSUMER_KEY")
        self.consumer_secret = os.getenv("CONSUMER_SECRET")
        self.access_token = os.getenv("ACCESS_TOKEN")
        self.access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

        if not all([self.bearer_token, self.consumer_key, self.consumer_secret, self.access_token, self.access_token_secret]):
            raise ValueError("❌ Missing Twitter API credentials in environment variables")

        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True)

        self.client = tweepy.Client(
            bearer_token=self.bearer_token,
            consumer_key=self.consumer_key,
            consumer_secret=self.consumer_secret,
            access_token=self.access_token,
            access_token_secret=self.access_token_secret,
            wait_on_rate_limit=True,
        )

    def post(self, text):
        """Posts a tweet with the given text."""
        try:
            response = self.client.create_tweet(text=str(text))
            print("✅ Tweet posted successfully!")
            return response.data
        except tweepy.TweepyException as e:
            print(f"❌ Error posting tweet: {e}")
            return None
