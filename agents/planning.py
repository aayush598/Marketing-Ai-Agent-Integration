import json
import requests
from config.config import GROQ_API_KEY

# ✅ Function to check available Groq models
def list_groq_models(api_key=GROQ_API_KEY):
    """Lists available Groq models for debugging."""
    try:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        response = requests.get("https://api.groq.com/openai/v1/models", headers=headers)
        if response.status_code == 200:
            models = response.json()["data"]
            print("🔹 Available Groq Models:")
            for model in models:
                print(f"- {model['id']}")
            return models
        else:
            print(f"❌ Error listing models: {response.status_code} - {response.text}")
            return []
    except Exception as e:
        print(f"❌ Error listing models: {str(e)}")
        return []

# ✅ Function to create prompt for planning content generation
def create_prompt(aspect, product_name, product_features, description, audience, platform):
    """
    Creates a detailed prompt for the given planning aspect.

    Args:
        aspect (str): The planning aspect to create a prompt for.
        product_name (str): The product name.
        product_features (list): The product's features.
        description (str): The campaign description.
        audience (str): The target audience.
        platform (str): The marketing platform.

    Returns:
        str: A detailed prompt.
    """
    aspect_name = aspect.replace('_', ' ')
    
    prompt = f"""
    Create a comprehensive {aspect_name} plan for the following product marketing campaign:

    🔹 **Product**: {product_name}
    🔹 **Key Features**: {', '.join(product_features)}
    🔹 **Description**: {description}
    🔹 **Target Audience**: {audience}
    🔹 **Marketing Platform**: {platform}

    🎯 **Guidelines:**
    - Provide clear **strategies and steps** to optimize {aspect_name}.
    - Highlight **best practices and potential challenges**.
    - Suggest **tactics specific to {platform}** for reaching {audience}.
    - Structure the output using **markdown headings, bullet points, and action steps**.
    """

    return prompt

# ✅ Function to generate planning details using Groq API
def generate_planning(product_name, product_features, description, audience, platform):
    """
    Generates a complete planning document covering all aspects.
    """
    plan_aspects = get_plan_aspects()
    planning_content = {}

    for _, aspect in plan_aspects.items():
        prompt = create_prompt(aspect,product_name, product_features, description, audience, platform,)
        _, content = generate_with_groq(prompt, GROQ_API_KEY)  # Replace with actual API key
        planning_content[aspect] = content

    return json.dumps(planning_content, indent=2)

# ✅ Function to modify an existing planning document
def modify_planning(existing_planning, modifications):
    """
    Modify the planning document based on user input.
    
    Args:
        existing_planning (str): The original planning content.
        modifications (str): The modifications provided by the user.

    Returns:
        str: The updated planning document.
    """
    return f"Modified Planning:\n\n{modifications}\n\nOriginal:\n{existing_planning}"

# ✅ Function to generate content using Groq API
def generate_with_groq(prompt, api_key, model_name='llama3-70b-8192'):
    try:
        if not api_key:
            return "❌ Error: Missing Groq API Key", ""

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": model_name,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7,
            "max_tokens": 4000
        }

        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=payload
        )

        if response.status_code == 200:
            return "Success", response.json()["choices"][0]["message"]["content"]
        else:
            return f"❌ Error: {response.status_code} - {response.text}", ""

    except Exception as e:
        return f"❌ Error generating response: {str(e)}", ""

# ✅ Function to get planning aspect names
def get_plan_aspects():
    return {
        0: "marketing_goals",
        1: "budget_allocation",
        2: "resource_planning",
        3: "timeline_milestones",
        4: "pricing_packaging",
        5: "distribution_delivery"
    }
