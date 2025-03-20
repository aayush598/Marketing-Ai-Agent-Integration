Here's a **detailed README.md** file for your **Marketing AI Agent Integration** project. It includes an **overview, features, setup instructions, usage guide, API details, folder structure, and contribution guidelines**.

---

## 📢 Marketing AI Agent Integration

🚀 **AI-Powered Marketing Campaign Generator** to automate **blog writing, social media posts, ad copy creation, image generation, monitoring, strategy planning, and campaign execution** using **Generative AI (Gemini, GPT), Python (Flask, Streamlit), and APIs**.

### **📌 Table of Contents**

- [Introduction](#introduction)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation Guide](#installation-guide)
- [Usage Guide](#usage-guide)
- [Project Structure](#project-structure)
- [API & Model Integration](#api--model-integration)
- [Contribution Guidelines](#contribution-guidelines)
- [License](#license)

---

## **📌 Introduction**

Marketing AI Agent Integration is a powerful **AI-driven automation tool** for generating **marketing content** across multiple platforms. It utilizes **Large Language Models (LLMs)** like **Gemini AI, GPT, and Generative AI APIs** to craft **blogs, ad copies, social media posts, and marketing strategies** with SEO-optimized content.

🔹 **Designed for:**  
✔️ **Marketers, Content Creators, and Businesses**  
✔️ **AI-Powered Content & Strategy Generation**  
✔️ **Automated SEO & Campaign Execution**

---

## **🚀 Features**

✅ **AI-Powered Blog Generation** – Create long-form, SEO-optimized blog posts.  
✅ **Social Media Post Generation** – Auto-generate posts for Twitter, LinkedIn, Instagram, and Facebook.  
✅ **Ad Copy Writing** – Generate ad copy tailored for different platforms (Email, Facebook, YouTube, etc.).  
✅ **Image Generation** – Create marketing visuals & social media graphics with AI.  
✅ **Campaign Monitoring & Analytics** – Track performance metrics using CSV data.  
✅ **Marketing Strategy Planning** – AI-generated strategies for engagement, brand positioning, and budget allocation.  
✅ **Platform-Specific Content Optimization** – Adapts tone, format, and structure based on the selected platform.  
✅ **Streamlit UI with Interactive Dashboard** – User-friendly interface for campaign management.

---

## **🛠 Tech Stack**

🔹 **Frontend**:

- [Streamlit](https://streamlit.io/) – UI for campaign execution.

🔹 **Backend**:

- [Flask](https://flask.palletsprojects.com/) – Handles API requests & AI model integration.
- [Google Gemini API](https://ai.google.dev/) – Content generation.
- [OpenAI GPT](https://openai.com/) – Advanced AI text generation.

🔹 **Other Tools & APIs**:

- [Google SerpAPI](https://serpapi.com/) – Web scraping for insights.
- [Image Generation APIs](https://platform.openai.com/docs/) – AI-powered visual content creation.
- CSV Data Handling for **Performance Monitoring & Analytics**.

---

## **📥 Installation Guide**

### **1️⃣ Clone the Repository**

```sh
git clone https://github.com/aayush598/Marketing-Ai-Agent-Integration.git
cd Marketing-Ai-Agent-Integration
```

### **2️⃣ Set Up a Virtual Environment**

```sh
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate  # On Windows
```

### **3️⃣ Install Dependencies**

```sh
pip install -r requirements.txt
```

### **4️⃣ Configure API Keys**

To fully utilize the **Marketing AI Agent Integration**, you need to set up and configure API keys for various services. Below are the steps to obtain the required API keys:

---

### **📧 Gmail API Configuration (For Email Campaigns)**

To send emails using Gmail, you must enable **2-Step Verification** and generate an **App Password**:

1. **Enable 2-Step Verification:**

   - Go to **[Google Account Security](https://myaccount.google.com/security)**.
   - Under **"Signing in to Google"**, enable **2-Step Verification**.

2. **Generate a 16-Digit App Password:**
   - Visit **[Google App Passwords](https://myaccount.google.com/apppasswords)**.
   - Select **"Mail"** as the app and **"Your Device"** as the device.
   - Click **Generate** and copy the 16-digit password.
   - Use this password as your **SMTP_PASSWORD** in the `.env` file.

---

### **🐦 Twitter API Configuration (For Social Media Posting)**

To automate **Twitter (X) posts**, you need API keys from the **Twitter Developer Platform**:

1. **Apply for Twitter Developer Access:**

   - Visit **[Twitter Developer Portal](https://developer.x.com/en/apply-for-access)**.
   - Apply for **Essential or Elevated Access** to enable API usage.

2. **Get API Keys:**
   - Go to **[Twitter Developer Dashboard](https://developer.x.com/en/portal/dashboard)**.
   - Click on the **Key Icon** under your project app section.
   - **Regenerate the API Key, API Key Secret, Access Token, and Access Token Secret**.
   - Add them to your `.env` file.

---

### **📺 YouTube API Configuration (For Video Content Automation)**

To manage and post videos on YouTube, you need API credentials from **Google Cloud Console**:

1. **Enable the YouTube API:**

   - Visit **[Google Cloud Console](https://console.cloud.google.com/)**.
   - Create a **New Project** and go to **APIs & Services**.
   - Search for **YouTube Data API v3** and enable it.

2. **Download OAuth 2.0 Credentials:**
   - Go to **Credentials** → **Create Credentials** → **OAuth 2.0 Client ID**.
   - Download the JSON file and place it in your project folder.

---

### **🔍 SerpAPI (For Web Scraping & SEO Analysis)**

To fetch Google search results and keyword trends:

1. Go to **[SerpAPI](https://serpapi.com/)** and sign up.
2. Get your **SerpAPI Key** from the **dashboard**.
3. Add it to the `.env` file as:
   ```
   SERPAPI_KEY="your_serpapi_key"
   ```

---

### **🤖 Gemini AI API (For AI Content Generation)**

Google Gemini is used for **AI-powered blog writing, social media posts, and ad copy**.

1. Visit **[Google AI](https://ai.google.dev/)** and sign up.
2. Generate an API key from the **Google Gemini Console**.
3. Add it to the `.env` file:
   ```
   GEMINI_API_KEY="your_gemini_api_key"
   ```

---

### **⚡ Groq API (For Fast AI Processing)**

Groq provides ultra-fast **AI model inference** for content generation.

1. Sign up at **[Groq Cloud](https://groq.com/)**.
2. Get your **Groq API Key** from the **developer console**.
3. Add it to `.env`:
   ```
   GROQ_API_KEY="your_groq_api_key"
   ```

---

### **🤗 Hugging Face API (For NLP & AI Models)**

Hugging Face is used for **text analysis and advanced AI content processing**.

1. Register at **[Hugging Face](https://huggingface.co/)**.
2. Navigate to **Settings → Access Tokens** and generate a token.
3. Add it to `.env`:
   ```
   HUGGINGFACE_API_KEY="your_huggingface_api_key"
   ```

---

### **📂 Add API Keys to `.env` File**

Once you have obtained all the required API keys, create a `.env` file in the project root and add the keys:

```env
# Gmail SMTP for Email Marketing
SMTP_EMAIL="your_email@gmail.com"
SMTP_PASSWORD="your_generated_16_digit_app_password"

# Twitter API Keys
TWITTER_API_KEY="your_twitter_api_key"
TWITTER_API_SECRET="your_twitter_api_secret"
TWITTER_ACCESS_TOKEN="your_twitter_access_token"
TWITTER_ACCESS_SECRET="your_twitter_access_secret"

# YouTube API
YOUTUBE_CREDENTIALS_PATH="path_to_your_youtube_credentials.json"

# Google Gemini AI
GEMINI_API_KEY="your_gemini_api_key"

# Groq API
GROQ_API_KEY="your_groq_api_key"

# SerpAPI for Web Scraping
SERPAPI_KEY="your_serpapi_key"

# Hugging Face AI
HUGGINGFACE_API_KEY="your_huggingface_api_key"
```

---

Your **Marketing AI Agent** is now fully configured and ready to generate AI-powered marketing content! 🚀

Create a `.env` file and add your API keys:

```
GEMINI_API_KEY="your_info"
SERPAPI_KEY="your_info"
GROQ_API_KEY="your_info"
SENDER_MAIL="your_info"
SENDER_PASSWORD="your_info"
HUGGINGFACE_API="your_info"
CONSUMER_KEY="your_info"
CONSUMER_SECRET="your_info"
BEARER_TOKEN="your_info"
ACCESS_TOKEN="your_info"
ACCESS_TOKEN_SECRET="your_info"
```

### **5️⃣ Run the Application**

```sh
python main.py
```

The app will be accessible at **`http://localhost:8501/`**.

---

## **📖 Usage Guide**

### **🎯 How to Generate Marketing Content**

1️⃣ **Navigate to the Home Page**  
2️⃣ **Enter Product Details** – Add product name, features, audience, and description.  
3️⃣ **Choose Actions** – Select **Blog Post, Ad Copy, Social Media, Monitoring, Strategy, or Planning**.  
4️⃣ **Generate & Modify** – AI-generated content will appear in editable sections.  
5️⃣ **Post or Download** – Export content as HTML or post directly to platforms like **Twitter, YouTube, Email**.

---

## **📂 Project Structure**

```
Marketing-Ai-Agent-Integration/
│── agents/                # AI-based marketing content generation & campaign management
│   ├── __init__.py
│   ├── MarketingAgent.py
│   ├── generate_ad_copy.py
│   ├── generate_blog.py
│   ├── generate_campaign.py
│   ├── generate_hashtags.py
│   ├── generate_images_with_gemini.py
│   ├── generate_social_media_post.py
│   ├── generate_video_script.py
│   ├── monitor_campaign.py
│   ├── planning.py
│   ├── scrape_images_with_serpapi.py
│   ├── strategy_planner.py
│
├── frontend/              # Streamlit UI components and pages
│   ├── __init__.py
│   ├── ad_copy.py
│   ├── blog.py
│   ├── home.py
│   ├── images.py
│   ├── input_form.py
│   ├── inputs.py
│   ├── layout.py
│   ├── monitoring.py
│   ├── planning.py
│   ├── social_media.py
│   ├── strategy.py
│   ├── video_script.py
│
├── config/                # Configuration files
│   ├── config.py
│
├── media/                 # Stored media files & monitoring data
│   ├── monitoring_data/
│   │   ├── budget_utilization.csv
│   │   ├── competitor_activity.csv
│   │   ├── lead_conversion.csv
│   │   ├── operational_efficiency.csv
│   │   ├── sales_data.csv
│   │
│   ├── video/
│   │   ├── video.mp4
│
├── social_media/          # Social media automation & posting
│   ├── email_sender.py
│   ├── social_media_manager.py
│   ├── twitter_post.py
│   ├── youtube_uploader.py
│
├── .env                   # Environment variables (API keys)
├── .gitignore             # Files to ignore in version control
├── audience.py            # Target audience selection
├── campaign.py            # Main campaign execution script
├── client_secret.json     # OAuth credentials for APIs (Google, YouTube, etc.)
├── main.py                # Main entry point of the application
├── render.yaml            # Deployment configuration for Render
├── requirements.txt       # Required Python dependencies
├── README.md              # Project documentation
├── ui.py                  # Streamlit UI logic and navigation

```

---

## **🔗 API & Model Integration**

The **Marketing AI Agent** interacts with **Generative AI APIs**:

### **🔹 Blog Generation**

- Uses **Gemini AI & GPT** to **generate long-form SEO-optimized blogs**.
- Enhances readability, keyword placement, and audience engagement.

### **🔹 Social Media Post Optimization**

- **Platform-specific content creation** for **Twitter, LinkedIn, Facebook, Instagram, YouTube**.
- Auto-generates **trending hashtags & engaging hooks**.

### **🔹 Ad Copy Customization**

- Generates **high-converting ad copy** based on **platform best practices**.
- AI tailors **tone, style, and CTA** for **Email, YouTube, Facebook, LinkedIn, Instagram**.

### **🔹 Image Generation**

- Uses **AI-powered APIs** to **create ad visuals & promotional graphics**.

### **🔹 Campaign Monitoring**

- Reads CSV files for **Sales Tracking, Competitor Analysis, Budget Utilization, and Customer Feedback**.
- Displays **real-time marketing performance analytics**.

---

## **🚀 Instructions to Deploy on Render**

Render is a powerful **cloud platform** for deploying web applications. Follow these steps to deploy this **Marketing AI Agent Integration** project on **Render**.

---

### **🔗 Step 1: Connect GitHub Repository**

1. **Go to [Render](https://dashboard.render.com/)** and sign up (or log in).
2. Click on **“New Web Service”**.
3. Select **“Connect a Repository”** and authorize GitHub access.
4. Select the **GitHub repository** (`Marketing-Ai-Agent-Integration`).
5. Click **“Connect”**.

---

### **⚙️ Step 2: Configure Deployment**

1. **Select Environment:** **Python**
2. **Runtime Environment:** Set to **Python 3.9+**
3. **Build Command:**
   ```
   pip install -r requirements.txt
   ```
4. **Start Command:**
   ```
   python main.py
   ```
5. **Instance Type:** Choose **Free or Starter Plan**
6. **Click on “Create Web Service”** to deploy.

---

### **🔑 Step 3: Set Up Environment Variables**

Since this project requires **API keys**, you need to **upload the `.env` file** for security.

1. Go to **Render Dashboard** → Select the **deployed service**.
2. Navigate to the **"Environment"** tab.
3. Click **"Add Environment Variables"**.
4. Add the following **key-value pairs** from your `.env` file:

   ```
   GEMINI_API_KEY=your_gemini_api_key
   GROQ_API_KEY=your_groq_api_key
   SERPAPI_KEY=your_serpapi_key
   HUGGINGFACE_API_KEY=your_huggingface_api_key
   GMAIL_APP_PASSWORD=your_gmail_16_digit_app_password
   TWITTER_API_KEY=your_twitter_api_key
   YOUTUBE_API_CREDENTIALS_PATH=/path/to/client_secret.json
   ```

5. **Alternatively**, upload the **`.env` file** directly:
   - Go to the **Environment tab**.
   - Click **“Upload Environment File”**.
   - Select `.env` from your local machine.

---

### **🚀 Step 4: Deploy and Run**

1. Click **"Manual Deploy"** or **wait for automatic deployment**.
2. Once the deployment is complete, click on the **Live URL**.
3. Your **AI-powered marketing campaign generator** is now live! 🎉

---

### **🔄 Step 5: Enable Auto Deploy (Optional)**

1. Go to the **Settings tab** in Render Dashboard.
2. Enable **Auto Deploy** to automatically deploy the latest changes from GitHub.
3. Every time you push changes to the **GitHub repository**, Render will redeploy the app.

---

### **✅ Additional Notes**

- If using **Google APIs** (Gmail, YouTube), ensure you **upload the `client_secret.json` file** to **Render’s persistent storage** or reference it correctly in the environment variables.
- Check **Logs** in Render Dashboard for debugging if deployment fails.
- If using **a custom domain**, go to **Settings > Custom Domains** to configure it.

---

### **🎯 Your App is Now Live on Render!**

🚀 Enjoy running **Marketing AI Agent Integration** in the cloud! 🌍🎉

## **👨‍💻 Contribution Guidelines**

Want to improve this project? **Contributions are welcome!** 🎉

1️⃣ **Fork this Repository**  
2️⃣ **Create a Branch** (`git checkout -b feature-branch`)  
3️⃣ **Make Your Changes & Commit** (`git commit -m "Added new feature"`)  
4️⃣ **Push the Branch** (`git push origin feature-branch`)  
5️⃣ **Open a Pull Request** 🚀

---

## **📜 License**

This project is **open-source** and licensed under the **MIT License**.

---

## **📞 Contact & Support**

For any queries or support, reach out via:  
📧 **Email:** [your_email@example.com]  
🌐 **GitHub Issues:** [Submit an Issue](https://github.com/aayush598/Marketing-Ai-Agent-Integration/issues)

---

### ⭐ **If you found this project useful, give it a star!** ⭐

```sh
git clone https://github.com/aayush598/Marketing-Ai-Agent-Integration.git
```

Happy Marketing! 🚀
