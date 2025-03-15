import google.generativeai as genai

gemini_text_model = genai.GenerativeModel('gemini-1.5-pro')

def generate_video_script(product_name, product_features, description, audience, platform):
    """Generate structured details for a video script."""
    prompt = f"""
    Provide only the following structured details for a video script:
    - Suitable Tone
    - Best Platform for Posting
    - Recommended Video Length
    - Content Headings only (Hook, Problem, Solution, Features, Social Proof, CTA)
    - Keep headings max 3-4 words
    
    Product: {product_name}
    Features: {product_features}
    Target Audience: {audience}
    Platform: {platform}
    """
    response = gemini_text_model.generate_content(prompt)
    return response.text

def modify_video_script(existing_script, modifications):
    """Modify a generated video script."""
    prompt = f"""
    Modify the following video script based on user input:
    {existing_script}
    
    Modifications: {modifications}
    """
    response = gemini_text_model.generate_content(prompt)
    return response.text
