import google.generativeai as genai

gemini_text_model = genai.GenerativeModel('gemini-2.0-flash-lite')

def generate_blog_structure(product_name, product_features, description, audience, platform):
    """Generate structured details for a blog post."""
    prompt = f"""
    Provide only the following structured details for a blog post:
    - Suitable Tone (Informative, Persuasive, Conversational, Professional etc)
    - SEO Optimization Techniques (Meta title, description, keyword density, internal linking etc)
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
    """Generate a fully SEO-optimized and HTML-formatted blog post."""
    prompt = f"""
    Generate a **high-quality, SEO-optimized, and conversion-focused blog post** in valid **HTML format** based on the structured details below.

    **📌 Blog Structure**:
    {blog_structure}

    **🔍 SEO & Readability Optimization**:
    - Ensure the blog **ranks well on search engines** and follows SEO best practices.
    - Use an **engaging and concise** `<title>` tag with the primary keyword.
    - Include a `<meta name="description">` tag with a **compelling summary (max 160 characters)**.
    - Ensure **primary and secondary keywords** are used naturally throughout the text.
    - Use **short and scannable paragraphs** for mobile-friendly readability.

    **🛠 HTML Formatting Requirements**:
    - **Use `<h1>` for the main blog title**.
    - **Use `<h2>` for key sections** and `<h3>` for subtopics to maintain structure.
    - Ensure **proper `<p>` tags** for paragraphs and **bold important phrases** using `<strong>`.
    - **Use `<ul>` and `<ol>`** for lists and step-by-step guides to enhance readability.
    - Add `<img>` tags with **alt text** to improve accessibility and SEO.
    - Include an **internal linking strategy**, suggesting where to add links to relevant pages.

    **💡 User Engagement Strategies**:
    - Open with a **powerful hook** that captures reader attention.
    - Use **compelling storytelling** and real-world scenarios when applicable.
    - Include a **strong call-to-action (CTA)** inside a `<div class='cta'>` block at the end.
    - Highlight key takeaways in **bold** or **bullet points**.

    **🎯 Example CTA Format**:
    ```html
    <div class='cta'>
        <p><strong>🚀 Ready to take action?</strong></p>
        <a href="https://example.com/product" target="_blank" class="cta-button">Get Started Today!</a>
    </div>
    ```

    **📢 Additional Guidelines**:
    - Make the content **persuasive and action-driven** to encourage engagement.
    - Ensure the HTML **is valid, clean, and properly formatted**.
    - Maintain a **conversational, informative, or persuasive tone** based on the topic.

    **✅ Final Output**:
    Return the **fully structured and SEO-optimized HTML blog post** that is **ready for publishing**.
    """
    response = gemini_text_model.generate_content(prompt)
    return response.text

def modify_generated_blog(blog_content, modifications):
    """Modify an already generated blog post while preserving SEO and HTML formatting."""
    prompt = f"""
    Modify the following blog post based on user input, while ensuring it remains in HTML format with proper SEO optimizations:

    {blog_content}

    **User Modifications**: {modifications}

    **🔍 SEO & Readability Optimization**:
    - Ensure the blog **ranks well on search engines** and follows SEO best practices.
    - Use an **engaging and concise** `<title>` tag with the primary keyword.
    - Include a `<meta name="description">` tag with a **compelling summary (max 160 characters)**.
    - Ensure **primary and secondary keywords** are used naturally throughout the text.
    - Use **short and scannable paragraphs** for mobile-friendly readability.

    **🛠 HTML Formatting Requirements**:
    - **Use `<h1>` for the main blog title**.
    - **Use `<h2>` for key sections** and `<h3>` for subtopics to maintain structure.
    - Ensure **proper `<p>` tags** for paragraphs and **bold important phrases** using `<strong>`.
    - **Use `<ul>` and `<ol>`** for lists and step-by-step guides to enhance readability.
    - Add `<img>` tags with **alt text** to improve accessibility and SEO.
    - Include an **internal linking strategy**, suggesting where to add links to relevant pages.

    **💡 User Engagement Strategies**:
    - Open with a **powerful hook** that captures reader attention.
    - Use **compelling storytelling** and real-world scenarios when applicable.
    - Include a **strong call-to-action (CTA)** inside a `<div class='cta'>` block at the end.
    - Highlight key takeaways in **bold** or **bullet points**.

    **🎯 Example CTA Format**:
    ```html
    <div class='cta'>
        <p><strong>🚀 Ready to take action?</strong></p>
        <a href="https://example.com/product" target="_blank" class="cta-button">Get Started Today!</a>
    </div>
    ```

    **📢 Additional Guidelines**:
    - Make the content **persuasive and action-driven** to encourage engagement.
    - Ensure the HTML **is valid, clean, and properly formatted**.
    - Maintain a **conversational, informative, or persuasive tone** based on the topic.

    **✅ Final Output**:
    Return the **fully structured and SEO-optimized HTML blog post** that is **ready for publishing**.
    """
    response = gemini_text_model.generate_content(prompt)
    return response.text