import os
import time
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def get_authenticated_service():
    """
    Authenticate with YouTube API and return an authorized service object.
    """
    creds = None
    token_file = "token.json"

    if os.path.exists(token_file):
        creds = Credentials.from_authorized_user_file(token_file)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
            creds = flow.run_local_server(port=8080)

        with open(token_file, "w") as token:
            token.write(creds.to_json())

    return build("youtube", "v3", credentials=creds)

def upload_video(file_path, title, description, tags, category_id="22", privacy_status="public"):
    """
    Uploads a video to YouTube.
    """
    youtube = get_authenticated_service()
    request_body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags,
            "categoryId": category_id,
        },
        "status": {
            "privacyStatus": privacy_status,
        },
    }

    media = MediaFileUpload(file_path, chunksize=-1, resumable=True, mimetype="video/*")
    request = youtube.videos().insert(part="snippet,status", body=request_body, media_body=media)

    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"Uploading... {int(status.progress() * 100)}% complete")
        time.sleep(1)

    print("✅ Upload Complete! Video ID:", response["id"])
    return response["id"]

# Test the function if running this script directly
if __name__ == "__main__":
    video_id = upload_video(
        file_path="video.mp4",
        title="My Python Upload Video",
        description="This video was uploaded via Python script using YouTube Data API v3.",
        tags=["python", "youtube api", "automation"],
        category_id="22",
        privacy_status="public"
    )
    print(f"Video uploaded successfully! ID: {video_id}")
