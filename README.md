# **Marketing Campaign Generator**

This project provides an **AI-powered marketing campaign generator**. It allows users to generate **ad copies, blogs, social media posts, video scripts, hashtags, and images** based on a given product description.  
The project now runs as a **standalone function** for campaign generation, with a separate **Streamlit-based UI** for user interaction.

---

## **Features**

✅ Generate **marketing campaigns** automatically  
✅ Create **ad copies, blog posts, and social media posts**  
✅ Generate **video scripts and hashtags**  
✅ Scrape or generate **images using AI**  
✅ Supports **multiple platforms** like Twitter, LinkedIn, Instagram, YouTube, etc.

---

## **Installation**

1. **Clone the repository:**

   ```bash
   git clone https://github.com/aayush598/Marketing-Ai-Agent-Integration.git
   cd Marketing-Ai-Agent-Integration
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**  
   Create a `.env` file in the `config` folder and add your API keys:
   ```env
   GROQ_API_KEY=your_groq_api_key
   SERPAPI_KEY=your_serpapi_key
   GEMINI_API_KEY=your_gemini_api_key
   ```

---

## **Running the Application**

**Run the main.py file:**

```bash
python main.py
```

---

## **How to Use**

- Open the **Streamlit UI** in your browser.
- Enter details such as:
  - **Product Name**
  - **Product Features**
  - **Campaign Description**
  - **Target Audience**
  - **Platform (Twitter, LinkedIn, etc.)**
  - **Actions** (Select one or more from the available options)
- Click on **Generate Campaign**.
- The generated campaign details will be displayed in JSON format.

---

## **Available Actions**

| Action Name         | Description                             |
| ------------------- | --------------------------------------- |
| `campaign_idea`     | Generate a marketing campaign idea      |
| `ad_copy`           | Create an ad copy for promotion         |
| `blog_post`         | Generate a blog post about the product  |
| `video_script`      | Generate a video script for an ad       |
| `social_media_post` | Generate social media posts             |
| `hashtags`          | Generate hashtags for social media      |
| `scraped_images`    | Fetch images using SerpAPI              |
| `generated_images`  | Generate AI-powered images using Gemini |

---

## **Project Structure**

```
├── agents/
│   ├── generate_ad_copy.py
│   ├── generate_blog.py
│   ├── generate_campaign.py
│   ├── generate_hashtags.py
│   ├── generate_images_with_gemini.py
│   ├── generate_social_media_post.py
│   ├── generate_video_script.py
│   ├── scrape_images_with_serpapi.py
│   ├── MarketingAgent.py
├── social_media/
│   ├── social_media_manager.py
├── config/
│   ├── config.py
│   ├── .env
├── ui.py          # Streamlit UI file
├── campaign.py    # Standalone function for campaign generation
├── main.py        # Main file to run the project
├── requirements.txt
├── README.md
```

---

## **How It Works**

1. The user **fills in details** in the **Streamlit UI**.
2. The UI **formats the input** and sends it to `generate_campaign()`.
3. The backend processes the request using **AI models**.
4. The **result is displayed** on the UI in a structured format.

---

## **License**

This project is licensed under the **MIT License**.
