import google.generativeai as genai

gemini_text_model = genai.GenerativeModel('gemini-2.0-flash-lite')

def generate_ad_copy_structure(product_name, product_features, description, audience, platform):
    """Generate a structured ad copy format optimized for high conversion and engagement."""
    
    platform_ad_guidelines = {
        "Twitter": "Short, engaging, high-impact. Use power words, avoid fluff, and include 1-2 trending hashtags.",
        "LinkedIn": "Professional, data-driven, and persuasive. Emphasize business value and industry leadership.",
        "Instagram": "Emotion-driven storytelling, visually appealing, conversational, and CTA-focused.",
        "Facebook": "Mix of storytelling and direct response. Engaging intro, pain point solution, CTA.",
        "YouTube": "Strong hook in the first 5 seconds, benefits upfront, fast-paced storytelling.",
        "Email": "Hyper-personalized subject line, clear CTA, and structured for skimmability."
    }

    platform_guideline = platform_ad_guidelines.get(platform, "High-impact, persuasive marketing copy.")

    prompt = f"""
    You are a **world-class marketing strategist**. Craft an **elite-level ad copy structure** designed for **high engagement & conversions**.

    **🔹 Product Details**
    - **Product Name**: {product_name}
    - **Key Features**: {', '.join(product_features)}
    - **Description**: {description}
    - **Target Audience**: {audience}
    - **Platform**: {platform}

    **📌 Ad Copy Structure (Pro-Level Format)**
    1️⃣ **Powerful Headline** (Hook that grabs attention immediately)
    2️⃣ **Compelling Offer / Unique Selling Proposition (USP)** (What makes this product irresistible?)
    3️⃣ **Key Benefits (Max 3-4, written persuasively)**
    4️⃣ **Emotional Hook (Make them feel something - FOMO, exclusivity, excitement, trust)**
    5️⃣ **Social Proof (Testimonial, expert opinion, brand trust, influencer backing)**
    6️⃣ **Strong Call to Action (CTA) (Drive immediate action, make it urgent & clear)**

    **📢 Platform-Specific Ad Strategy**: {platform_guideline}

    **🚀 Key Rules for High-Performance Ads**
    - Use **bold power words** and **active voice** to maximize impact.
    - **Trigger emotions** through storytelling or direct persuasion.
    - **Avoid generic marketing terms** – make it feel exclusive & action-driven.
    - **Write like the best-performing ads on {platform}**.
    - **Also add the platform name in the structure for optimization.**

    📌 **Final Output:** A structured, **persuasive**, and **platform-optimized** ad copy format designed to maximize conversions.
    """
    
    response = gemini_text_model.generate_content(prompt)
    return response.text


def modify_ad_copy_structure(existing_structure, modifications):
    """Modify the structured details of an ad copy while keeping it competitive and engaging."""
    
    prompt = f"""
    Modify the following **high-converting ad copy structure** based on user input while preserving its **persuasive impact**:

    **Existing Structure:**
    {existing_structure}

    ✏ **User Requested Modifications:**
    {modifications}

    🔥 **Ensure the final output meets elite marketing standards:**
    - **Powerful opening hook** that grabs attention.
    - **Platform-optimized** engagement techniques.
    - **Psychological triggers** (exclusivity, trust, urgency, FOMO).
    - **A strong, irresistible CTA** to drive conversions.

    **🎯 Final Output:** A high-impact, **refined**, and **conversion-driven** ad copy format.
    """
    
    response = gemini_text_model.generate_content(prompt)
    return response.text


def generate_ad_copy_from_structure(ad_copy_structure):
    """Generate a fully formatted, high-converting ad copy tailored to the inferred platform, without any extra details or explanations."""

    prompt = f"""
    You are an expert ad copywriter for high-performance marketing campaigns.  
    Your task is to generate a **directly usable, professionally structured ad copy** based on the provided structure.

    **📌 Structure Provided:**  
    {ad_copy_structure}

    **🚀 Key Requirements:**  
    - **NO extra explanations, NO feedback, NO additional details** – only the ad copy content.  
    - **The copy must be immediately ready to post.**  
    - **Format the output correctly for the inferred platform (Email, Twitter, LinkedIn, Instagram, YouTube, etc.).**  
    - **Ensure it is highly persuasive, conversion-driven, and platform-optimized.**  
    - **Only return the content which will be send to user directly just by simple copy paste.**
    - **No requirement for making changes to the content should be required.**
    - **Generate content by keeping in mind that this will be send to user directly**
    - Remove all structural labels like **"Powerful Headline," "Compelling Offer," "Key Benefits," "Emotional Hook," "Social Proof," "CTA"** and similar headings.
    - Keep only the **raw ad copy content** in a natural flow, ensuring a seamless, persuasive structure.
    - Ensure the **content remains highly engaging** and maintains readability without unnecessary formatting markers.

    **📝 Output Rules:**  
    - If Email → **Generate the full email body** (with subject line).  
    - If Twitter → **Short, punchy, and hashtag-optimized (max 280 chars).**  
    - If LinkedIn → **Professional, insight-driven, and engagement-focused.**  
    - If Instagram → **Conversational, emotional, and visually engaging.**  
    - If YouTube → **Strong hook in first 5 seconds + compelling CTA.**  


    Return a **fully formatted ad copy** that can be **directly copied and pasted** for posting **without labels or headings**—only the advertisement itself.
    """

    response = gemini_text_model.generate_content(prompt)
    return response.text


def modify_generated_ad_copy(existing_ad_copy, modifications):
    """Modify the ad copy while ensuring it remains **formatted, persuasive, and platform-optimized**."""

    prompt = f"""
    Modify the following **high-performing, professionally formatted ad copy** while **preserving its persuasive power and platform-specific optimization**:

    **📢 Existing Ad Copy:**  
    {existing_ad_copy}

    **✏ User Requested Modifications:**  
    {modifications}

    **🚀 Key Rules for High-Impact Optimization:**  
    - **Maintain readability & persuasive storytelling.**  
    - **Enhance emotional triggers & conversion-driven elements.**  
    - **Ensure the CTA remains strong and compelling.**  
    - **Keep messaging aligned with the inferred platform style.**  

    **📌 Your Task:**  
    - Modify the ad copy based on the **user's requested changes**.  
    - Ensure the output remains **structured, fully formatted, and immediately usable**.  
    - Maintain high **clarity, engagement, and persuasive effectiveness**. 

    **🚀 Key Requirements:**  
    - **NO extra explanations, NO feedback, NO additional details** – only the ad copy content.  
    - **The copy must be immediately ready to post.**  
    - **Format the output correctly for the inferred platform (Email, Twitter, LinkedIn, Instagram, YouTube, etc.).**  
    - **Ensure it is highly persuasive, conversion-driven, and platform-optimized.**  
    - **Only return the content which will be send to user directly just by simple copy paste.**
    - **No requirement for making changes to the content should be required.**
    - **Generate content by keeping in mind that this will be send to user directly**
    - Remove all structural labels like **"Powerful Headline," "Compelling Offer," "Key Benefits," "Emotional Hook," "Social Proof," "CTA"** and similar headings.
    - Keep only the **raw ad copy content** in a natural flow, ensuring a seamless, persuasive structure.
    - Ensure the **content remains highly engaging** and maintains readability without unnecessary formatting markers.

    **📝 Output Rules:**  
    - If Email → **Generate the full email body** (with subject line).  
    - If Twitter → **Short, punchy, and hashtag-optimized (max 280 chars).**  
    - If LinkedIn → **Professional, insight-driven, and engagement-focused.**  
    - If Instagram → **Conversational, emotional, and visually engaging.**  
    - If YouTube → **Strong hook in first 5 seconds + compelling CTA.**  


    Return a **fully formatted ad copy** that can be **directly copied and pasted** for posting **without labels or headings**—only the advertisement itself.
 

    **🎯 Final Output:** A refined, **fully formatted** and **high-impact ad copy**, ready for direct use in marketing campaigns.
    """

    response = gemini_text_model.generate_content(prompt)
    return response.text
