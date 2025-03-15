import google.generativeai as genai

gemini_text_model = genai.GenerativeModel('gemini-1.5-pro')

def generate_blog_structure(product_name, product_features, description, audience, platform):
    """Generate structured details for a blog post."""
    prompt = f"""
    Provide only the following structured details for a blog post:
    - Suitable Tone
    - SEO Optimization Techniques
    - Recommended Content Length
    - Content Headings (For example Intro, Problem, Solution, Features, Benefits, Conclusion, CTA)
    - Keep headings max 3-4 words
    
    Product: {product_name}
    Features: {product_features}
    Target Audience: {audience}
    Platform: {platform}
    """
    response = gemini_text_model.generate_content(prompt)
    return response.text

def modify_blog_structure(existing_structure, modifications):
    """Modify the structured details of a blog post."""
    prompt = f"""
    Modify the following blog post details based on user input:
    {existing_structure}
    
    Modifications: {modifications}

    Instructions :
    Provide only the following structured details for a blog post:
    - Suitable Tone
    - SEO Optimization Techniques
    - Recommended Content Length
    - Content Headings (For example Intro, Problem, Solution, Features, Benefits, Conclusion, CTA etc)
    - Keep headings max 3-4 words
    """
    response = gemini_text_model.generate_content(prompt)
    return response.text

def generate_blog_from_structure(blog_structure):
    """Generate a complete blog post based on structured details."""
    prompt = f"Generate a detailed blog post based on the following structured details:\n{blog_structure}"
    response = gemini_text_model.generate_content(prompt)
    return response.text

def modify_generated_blog(blog_content, modifications):
    """Modify an already generated blog post based on user input."""
    prompt = f"""
    Modify the following blog post based on user input:
    {blog_content}

    Modifications: {modifications}

    Ensure the modifications improve clarity, engagement, and SEO while keeping the original structure intact.
    """
    response = gemini_text_model.generate_content(prompt)
    return response.text