import google.generativeai as genai

gemini_text_model = genai.GenerativeModel('gemini-2.0-flash-lite')

def generate_video_script_structure(product_name, product_features, description, audience, platform):
    """Generate structured details for a video script."""
    prompt = f"""
    Provide only the following structured details for a video script:
    - Suitable Tone
    - Best Platform for Posting
    - Recommended Video Length
    - Content Headings (For example Hook, Problem, Solution, Features, Social Proof, CTA etc)
    - Keep headings max 3-4 words
    
    Product: {product_name}
    Features: {product_features}
    Target Audience: {audience}
    Platform: {platform}
    """
    response = gemini_text_model.generate_content(prompt)
    return response.text

def modify_video_script_structure(existing_structure, modifications):
    """Modify the structured details of a video script before full generation."""
    prompt = f"""
    Modify the following video script format based on user input:
    {existing_structure}
    
    Modifications: {modifications}

    Instructions:
    Provide only the following structured details for a video script:
    - Suitable Tone
    - Best Platform for Posting
    - Recommended Video Length
    - Content Headings (For example Hook, Problem, Solution, Features, Social Proof, CTA etc)
    - Keep headings max 3-4 words
    """
    response = gemini_text_model.generate_content(prompt)
    return response.text

def generate_video_script_from_structure(video_structure):
    """Generate a complete video script based on structured details."""
    prompt = f"Generate a detailed video script based on the following structured details:\n{video_structure}"
    response = gemini_text_model.generate_content(prompt)
    return response.text

def modify_generated_video_script(video_script, modifications):
    """Modify an already generated full video script based on user input."""
    prompt = f"""
    Modify the following video script based on user input:
    {video_script}

    Modifications: {modifications}

    Ensure the modifications improve clarity, engagement, and video pacing while keeping the original structure intact.
    """
    response = gemini_text_model.generate_content(prompt)
    return response.text
