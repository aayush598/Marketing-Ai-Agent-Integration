from flask import Flask, request, jsonify
from config.config import GROQ_API_KEY, SERPAPI_KEY
from agents.MarketingAgent import MarketingAgent

app = Flask(__name__)
agent = MarketingAgent(GROQ_API_KEY, SERPAPI_KEY)

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
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
