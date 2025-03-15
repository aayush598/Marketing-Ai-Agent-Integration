import google.generativeai as genai

gemini_text_model = genai.GenerativeModel('gemini-1.5-pro')

def generate_social_media_structure(product_name, product_features, description, audience, platform):
    """Generate structured details for a social media post."""
    prompt = f"""
    Provide ONLY the following structured details for a social media post:
    - Engagement Strategies (storytelling, CTA, question-based)
    - Use of Emojis & Readability (How to make the post visually appealing, scannable)
    - Best Tone (Casual, professional, humorous, inspiring, persuasive, etc.)
    
    Product: {product_name}
    Features: {product_features}
    Target Audience: {audience}
    Platform: {platform}
    """
    response = gemini_text_model.generate_content(prompt)
    return response.text

def modify_social_media_structure(existing_structure, modifications):
    """Modify structured social media post details."""
    prompt = f"""
    Modify the following social media post details based on user input:
    {existing_structure}
    
    Modifications: {modifications}
    """
    response = gemini_text_model.generate_content(prompt)
    return response.text

def generate_social_media_post(post_structure):
    """Generate a complete social media post from structured details."""
    prompt = f"Generate a detailed social media post based on the following structured details:\n{post_structure}"
    response = gemini_text_model.generate_content(prompt)
    return response.text
