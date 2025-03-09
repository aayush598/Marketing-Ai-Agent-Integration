from social_media.twitter_post import TwitterClient
from social_media.youtube_uploader import upload_video
from social_media.email_sender import EmailSender

class SocialMediaManager:
    def __init__(self):
        """
        Initialize all social media clients.
        """
        self.twitter_client = TwitterClient()
        self.email_client = EmailSender()

    def post(self, platform, text):
        """
        Handles posting to different social media platforms.
        """
        platform = platform.lower()

        if (platform.lower() == "twitter") or (platform.lower() == "x") or (platform.lower() == "x.com"):
            return self.twitter_client.post(text)
        elif (platform.lower() == "youtube") or (platform.lower() == "yt"):
            return upload_video(
                file_path="media/video/video.mp4",  # Replace with actual file path
                title="Auto Uploaded Video",
                description=text,
                tags=["automation", "ai", "marketing"],
                category_id="22",
                privacy_status="public"
            )
        elif (platform.lower() == "email") or (platform.lower() == "gmail") or (platform.lower() == "mail"):
            return self.email_client.send_email(
                recipient_email="raiseracademy.sap@gmail.com",
                subject="Automated Email",
                body=text
            )
        else:
            print(f"❌ Platform '{platform}' is not yet supported.")
            return None
