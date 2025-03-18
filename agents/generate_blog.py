import google.generativeai as genai

gemini_text_model = genai.GenerativeModel('gemini-2.0-flash-lite')

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
    """Generate a complete blog post based on structured details with SEO-optimized HTML format."""
    prompt = f"""
    Generate a detailed and SEO-optimized blog post in proper HTML format based on the following structured details:

    {blog_structure}

    **SEO Guidelines**:
    - Include an <title> tag for the blog.
    - Provide a <meta name="description" content="..."> tag with a concise and compelling description.
    - Use <h1> for the main title, <h2> for sections, and <h3> for sub-sections.
    - Ensure keyword placement is natural throughout the content.
    - Add an <img> tag with an "alt" attribute for image descriptions.

    **Blog Formatting Requirements**:
    - Start with a strong headline inside <h1>.
    - Use <h2> for major sections and <h3> for subtopics.
    - Keep paragraphs short and easy to read with <p>.
    - Include an unordered list <ul> when listing benefits.
    - Add a call-to-action inside <div class='cta'> at the end.
    - Ensure HTML is properly formatted and clean.
    """
    response = gemini_text_model.generate_content(prompt)
    return response.text

def modify_generated_blog(blog_content, modifications):
    """Modify an already generated blog post while preserving SEO and HTML formatting."""
    prompt = f"""
    Modify the following blog post based on user input, while ensuring it remains in HTML format with proper SEO optimizations:

    {blog_content}

    **User Modifications**: {modifications}

    **Guidelines**:
    - Maintain the HTML structure, ensuring correct <h1>, <h2>, <h3>, <p>, and <ul> usage.
    - Improve clarity, engagement, and SEO optimization.
    - Preserve image placeholders with alt text.
    - Keep metadata such as <title> and <meta description>.
    - Ensure it remains mobile-friendly and easy to read.

    **Final Output**:
    - Return a well-structured and SEO-optimized HTML blog post.
    """
    response = gemini_text_model.generate_content(prompt)
    return response.text