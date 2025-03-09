# Marketing Campaign Generator

This project provides an AI-powered marketing campaign generator using Flask. It allows users to generate ad copies, blogs, social media posts, video scripts, hashtags, and images based on a given product description.

## Features

- Generate marketing campaigns automatically
- Create ad copies, blog posts, and social media posts
- Generate video scripts and hashtags
- Scrape or generate images using AI
- Supports multiple platforms like Web, iOS, and Android

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/aayush598/Marketing-Ai-Agent-Integration.git
   cd Marketing-Ai-Agent-Integration
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the `config` folder and add your API keys:
   ```env
   GROQ_API_KEY=your_groq_api_key
   SERPAPI_KEY=your_serpapi_key
   GEMINI_API_KEY=your_gemini_api_key
   ```

## Running the Application

Start the Flask server:

```bash
python main.py
```

By default, the server will run at `http://127.0.0.1:5000/`.

## API Endpoints

### Generate Marketing Campaign

- **URL:** `/generate_campaign`
- **Method:** `POST`
- **Content-Type:** `application/json`
- **Request Body:**

  ```json
  {
    "prompt": [
      "product_name",
      "product_features",
      "description",
      "audience",
      "platform"
    ],
    "actions": ["campaign_idea", "ad_copy", "generated_images"]
  }
  ```

- **Response Example:**
  ```json
  {
    "campaign_idea": "A marketing campaign focused on 'Work Smarter, Not Harder' featuring real-life case studies of professionals using AI to optimize their daily workflow.",
    "ad_copy": "🚀 Boost your productivity with AI! Automate tasks, get smart reminders, and optimize your workflow effortlessly. Try AI Productivity Assistant today! #WorkSmarter",
    "generated_images": [
      "https://dummyimage.com/600x400/000/fff&text=AI+Productivity+Assistant",
      "https://dummyimage.com/600x400/000/fff&text=Boost+Your+Efficiency",
      "https://dummyimage.com/600x400/000/fff&text=Smart+Reminders+AI"
    ]
  }
  ```

## Project Structure

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
├── config/
│   ├── config.py
├── main.py
├── requirements.txt
├── README.md
```

## Configuration

- **`config/config.py`**: Loads API keys from environment variables.
- **`main.py`**: Main Flask application that exposes the `/generate_campaign` endpoint.
- **`agents/`**: Contains modules for generating different types of marketing content.
  - `generate_ad_copy.py`: Creates ad copies.
  - `generate_blog.py`: Generates blog posts.
  - `generate_campaign.py`: Manages marketing campaigns.
  - `generate_hashtags.py`: Suggests relevant hashtags.
  - `generate_images_with_gemini.py`: Generates images using AI.
  - `generate_social_media_post.py`: Generates social media captions.
  - `generate_video_script.py`: Writes video scripts.
  - `scrape_images_with_serpapi.py`: Scrapes images using SerpAPI.
  - `MarketingAgent.py`: Manages campaign execution.

## Dependencies

Ensure the following dependencies are installed:

```bash
pip install Flask python-dotenv requests serpapi pillow
```

## How It Works

1. The user sends a `POST` request to `/generate_campaign` with a `prompt` and a list of `actions`.
2. The backend processes the request, generating marketing content using AI models.
3. The response includes ad copies, blog posts, hashtags, and generated images.

## License

This project is licensed under the MIT License.
