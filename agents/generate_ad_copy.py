import google.generativeai as genai

gemini_text_model = genai.GenerativeModel('gemini-2.0-flash-lite')

def generate_ad_copy_structure(product_name, product_features, description, audience, platform):
    """Generate a structured ad copy format optimized for the platform."""
    platform_ad_guidelines = {
        "Twitter": "Keep it short, engaging, and include relevant hashtags. Max 280 characters.",
        "LinkedIn": "Professional tone, emphasize business benefits, and use data-driven messaging.",
        "Instagram": "Conversational, emotional appeal, and include emojis & trending hashtags.",
        "Facebook": "Storytelling approach, mix of text & visuals, casual but informative.",
        "YouTube": "Engaging hook in the first 5 seconds, highlight benefits quickly.",
        "Email": "Personalized subject line, clear CTA, and structured content for readability."
    }

    platform_guideline = platform_ad_guidelines.get(platform, "Standard persuasive marketing copy.")

    prompt = f"""
    Provide ONLY the following structured details for a platform-specific ad copy:

    🔹 **Product**: {product_name}
    🔹 **Key Features**: {', '.join(product_features)}
    🔹 **Description**: {description}
    🔹 **Target Audience**: {audience}
    🔹 **Platform**: {platform}

    📌 **Ad Copy Structure:**
    - **Attention-Grabbing Headline**
    - **Compelling Offer / Unique Selling Proposition (USP)**
    - **Key Benefits (2-3 points)**
    - **Emotional Hook (Optional)**
    - **Strong Call to Action (CTA)**

    ⚡ **Platform-Specific Strategy:** {platform_guideline}

    🎯 *Ensure the structure is optimized for high engagement and conversions!*
    """

    response = gemini_text_model.generate_content(prompt)
    return response.text


def modify_ad_copy_structure(existing_structure, modifications):
    """Modify the structured details of an ad copy."""
    prompt = f"""
    Modify the following structured ad copy format based on user input:

    {existing_structure}

    ✏ **Modifications Requested**:
    {modifications}

    🔍 Ensure the updated structure maintains clarity, platform-optimization, and conversion-focus.
    """
    response = gemini_text_model.generate_content(prompt)
    return response.text


def generate_ad_copy_from_structure(ad_copy_structure):
    """Generate a full ad copy from the structured format."""
    prompt = f"""
    Based on the following structured ad copy format, generate a **complete, engaging ad copy**:

    {ad_copy_structure}

    ✅ Ensure the copy is **concise, persuasive, and platform-optimized**.
    """
    response = gemini_text_model.generate_content(prompt)
    return response.text


def modify_generated_ad_copy(existing_ad_copy, modifications):
    """Modify an already generated ad copy."""
    prompt = f"""
    Modify the following ad copy based on user input:

    {existing_ad_copy}

    ✏ **Modifications Requested**:
    {modifications}

    🔥 Ensure the ad remains compelling, persuasive, and platform-optimized.
    """
    response = gemini_text_model.generate_content(prompt)
    return response.text
