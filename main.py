from flask import Flask, request, jsonify
from config.config import GROQ_API_KEY, SERPAPI_KEY
from agents.MarketingAgent import MarketingAgent
from social_media.social_media_manager import SocialMediaManager

app = Flask(__name__)
agent = MarketingAgent(GROQ_API_KEY, SERPAPI_KEY)
social_media_manager = SocialMediaManager()  # Social media handler

@app.route("/generate_campaign", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt")
    actions = data.get("actions")  # Get list of actions from request
    
    if not prompt:
        return jsonify({"error": "Missing prompt"}), 400
    
    if not actions or not isinstance(actions, list):
        return jsonify({"error": "Invalid or missing 'actions' list"}), 400

    result = agent.run_campaign(prompt, actions)

    # Check if a social media post should be published
    if "social_media_post" in result:
        platform = prompt[-1]  # Last item in prompt is platform (e.g., Twitter, LinkedIn)
        post_text = result["social_media_post"]

        # Post to the detected platform
        social_media_response = social_media_manager.post(platform, post_text)

        if social_media_response:
            result[f"{platform.lower()}_post_status"] = "Posted successfully"
        else:
            result[f"{platform.lower()}_post_status"] = "Failed to post"
            
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
