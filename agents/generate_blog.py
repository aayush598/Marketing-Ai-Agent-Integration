def generate_blog_structure(self, product_name, product_features, description, audience, platform):
    """Generate an initial blog structure with headings and subheadings."""
    prompt = f"""
    Generate a structured blog outline (headings and subheadings) for:
    
    Product: {product_name}
    Features: {product_features}
    Description: {description}
    Target Audience: {audience}
    Platform: {platform}

    The structure should be well-organized and SEO-friendly. Do not write the full blog, only the outline.
    """
    response = self.gemini_text_model.generate_content(prompt)
    return response.text  # Return only the structure

def modify_blog_structure(self, current_structure, modification_prompt):
    """Modify the existing blog structure based on user input."""
    prompt = f"""
    Here is the current blog structure:

    {current_structure}

    The user wants the following modifications:
    {modification_prompt}

    Update the structure accordingly while keeping it well-organized and SEO-friendly.
    """
    response = self.gemini_text_model.generate_content(prompt)
    return response.text  # Return updated structure

def generate_blog_from_structure(self, final_structure):
    """Generate the full blog content based on the confirmed structure."""
    prompt = f"""
    Based on the following blog structure, generate a full detailed blog post:

    {final_structure}

    Ensure the blog is engaging, informative, and SEO-optimized.
    """
    response = self.gemini_text_model.generate_content(prompt)
    return response.text  # Return full blog content
