import google.generativeai as genai

gemini_text_model = genai.GenerativeModel('gemini-2.0-flash-lite')

def generate_strategy(product_name, product_features, description, audience, platform):
    """Generate a comprehensive marketing strategy for a product."""
    
    prompt = f"""
    You are a marketing strategist. Create a **detailed marketing strategy** for the following product:

    🔹 **Product Name**: {product_name}
    🔹 **Key Features**: {', '.join(product_features)}
    🔹 **Description**: {description}
    🔹 **Target Audience**: {audience}
    🔹 **Platform**: {platform}

    **Include the following elements:**
    1️⃣ **Marketing Strategy (Online & Offline Mix)**: Best digital and traditional marketing methods.
    2️⃣ **Brand Positioning & Unique Selling Proposition (USP)**: How to differentiate from competitors.
    3️⃣ **Communication & Content Strategy**: Content style, messaging, and platforms.
    4️⃣ **Sales Strategy (Channels & Methods)**: Best channels to maximize conversions.
    5️⃣ **Customer Engagement & Retention Strategy**: Loyalty programs, support, and engagement techniques.
    6️⃣ **Partnerships & Alliances Strategy**: Potential partnerships for business growth.

    ⚡ Provide actionable insights and best practices!
    """

    response = gemini_text_model.generate_content(prompt)
    return response.text

def modify_strategy(existing_strategy, modifications):
    """Modify an already generated marketing strategy based on user input."""
    prompt = f"""
    Modify the following marketing strategy based on user input:

    🔹 **Original Strategy:**
    {existing_strategy}

    🔹 **User Modifications:**
    {modifications}

    **Ensure the modifications enhance clarity, engagement, and execution feasibility while keeping the structure intact.**
    """

    response = gemini_text_model.generate_content(prompt)
    return response.text
