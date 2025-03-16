import requests

from config.config import SERPAPI_KEY , GROQ_API_KEY


def search_target_audience(product_name, product_features, description):
    """
    Uses SerpAPI to search for the target audience of a given product.
    Extracts only audience-related insights.
    """
    query = f"Who is the target audience for {product_name}? {product_features} {description}"

    url = f"https://serpapi.com/search.json?q={query}&hl=en&api_key={SERPAPI_KEY}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            audience_info = []
            for result in data.get("organic_results", []):
                snippet = result.get("snippet")
                if snippet:
                    audience_info.append(snippet)

            if audience_info:
                return audience_info[0]  # Return the first audience-related insight
    except Exception:
        pass

    return None  # Return None if API fails


def generate_target_audience_groq(product_name, product_features, description):
    """
    Uses Groq API (Llama 3) to infer the target audience based on product details.
    Extracts only audience-related information.
    """
    url = "https://api.groq.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""
    Based on the following product details, determine the ideal target audience:

    *Product Name:* {product_name}
    *Key Features:* {product_features}
    *Description:* {description}

    Only return the audience details in a short, direct format, like:
    "Tech Enthusiasts, Entrepreneurs, College Students, Business Professionals"
    """

    payload = {
        "model": "llama3-8b-8192",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"].strip()
    except Exception:
        pass

    return None  # Return None if API fails


def get_target_audience(product_name, product_features, description):
    """
    Determines the *target audience only* using *SerpAPI (Web)* and *Groq API (AI)*.
    Falls back to a default target audience if both fail.
    """
    # 1️⃣ *Try Searching via SerpAPI*
    audience = search_target_audience(product_name, product_features, description)
    if audience:
        return audience

    # 2️⃣ *Fallback: Use AI-based NLP Analysis with Groq API*
    audience = generate_target_audience_groq(product_name, product_features, description)
    if audience:
        return audience

    # 3️⃣ *Final Fallback: Return Default Audience*
    return "General Consumers, Tech Enthusiasts, Working Professionals"
