import google.generativeai as genai
from social_media.social_media_manager import SocialMediaManager
from config.config import GEMINI_API_KEY
genai.configure(api_key=GEMINI_API_KEY)

gemini_text_model = genai.GenerativeModel('gemini-2.0-flash-lite')
social_media_manager = SocialMediaManager()

def generate_social_media_structure(product_name, product_features, description, audience, platform):
    """Generate structured details for a social media post."""
    prompt = f"""
    Provide ONLY the following structured details for a social media post:
    - Engagement Strategies (storytelling, CTA, question-based)
    - Use of Emojis & Readability (How to make the post visually appealing, scannable)
    - Best Tone (Casual, professional, humorous, inspiring, persuasive, etc.)
    - Platform
    
    Product: {product_name}
    Features: {product_features}
    Target Audience: {audience}
    Platform: {platform}

    
    """
    response = gemini_text_model.generate_content(prompt)
    return response.text

def modify_social_media_structure(existing_structure, modifications):
    """Modify structured social media post details before full post generation."""
    prompt = f"""
    Modify the following structured social media post format based on user input:
    {existing_structure}
    
    Modifications: {modifications}

    Instructions :
    Provide ONLY the following structured details for a social media post:
    - Engagement Strategies (storytelling, CTA, question-based)
    - Use of Emojis & Readability (How to make the post visually appealing, scannable)
    - Best Tone (Casual, professional, humorous, inspiring, persuasive, etc.)
    """
    response = gemini_text_model.generate_content(prompt)
    return response.text

def generate_social_media_post_from_structure(post_structure):
    """Generate a complete social media post from structured details."""
    prompt = f"""Generate a detailed social media post based on the following 
    structured details with no extra stars and do not use any special characters,
    only use characters and hashtag and also do not use emojis, do add any stars 
    or emojis, content size and format must be same as the platform provided:\n{post_structure}

    **✅ Ensure the modified post includes:**
    - **Platform-Specific Formatting:** (e.g., concise for Twitter, professional for LinkedIn, storytelling for Instagram)
    - **Improved Readability:** Short sentences, proper spacing, clarity.
    - **Enhanced Engagement Strategy:** More compelling hooks, stronger CTA.
    - **Increased Shareability:** Relevant hashtags, persuasive messaging.

    **📌 Platform Formatting Rules:**
    - **Twitter (X):** Max 280 characters, punchy, hashtags, direct CTA.
    - **Instagram:** Caption format, short storytelling, strong CTA, no long paragraphs.
    - **LinkedIn:** Thought leadership, engaging opening, structured value, CTA.
    - **Facebook:** Community-driven, emotional appeal, storytelling, CTA.
    - **YouTube:** Video-friendly script, catchy hooks, keyword-rich description, CTA.
    - **Email:** Personal, warm, attention-grabbing subject line, persuasive body, CTA.

    **📢 Generate content ONLY using characters, words, and hashtags**. 
    **🚫 Do NOT use emojis or special characters like stars, bullets, or symbols.**

    """
    response = gemini_text_model.generate_content(prompt)
    return response.text

def modify_generated_social_media_post(post_content, modifications):
    """Modify an already generated social media post based on user input."""
    prompt = f"""
    Modify the following social media post based on user input:
    {post_content}

    Modifications: {modifications}

    Ensure that:
    - The readability and engagement strategies are improved.
    - The modifications align with the target audience and platform.

    **✅ Ensure the modified post includes:**
    - **Platform-Specific Formatting:** (e.g., concise for Twitter, professional for LinkedIn, storytelling for Instagram)
    - **Improved Readability:** Short sentences, proper spacing, clarity.
    - **Enhanced Engagement Strategy:** More compelling hooks, stronger CTA.
    - **Increased Shareability:** Relevant hashtags, persuasive messaging.

    **📌 Platform Formatting Rules:**
    - **Twitter (X):** Max 280 characters, punchy, hashtags, direct CTA.
    - **Instagram:** Caption format, short storytelling, strong CTA, no long paragraphs.
    - **LinkedIn:** Thought leadership, engaging opening, structured value, CTA.
    - **Facebook:** Community-driven, emotional appeal, storytelling, CTA.
    - **YouTube:** Video-friendly script, catchy hooks, keyword-rich description, CTA.
    - **Email:** Personal, warm, attention-grabbing subject line, persuasive body, CTA.

    **📢 Generate content ONLY using characters, words, and hashtags**. 
    **🚫 Do NOT use emojis or special characters like stars, bullets, or symbols.**
    """
    response = gemini_text_model.generate_content(prompt)
    return response.text

def post_social_media_content(platform, content):
    print(f"Platform : {platform} | Content {content}")
    """Post generated content to social media platforms."""
    return social_media_manager.post(platform, content)