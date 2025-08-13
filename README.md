# YouTube Transcript Analyzer

## How to Run

1. Clone or download this project.
2. Create and activate a Python virtual environment (recommended).
3. Install required packages:  

pip install -r requirements.txt

4. Place your Perplexity AI API key in a file named `PPLX_API_KEY.txt` in the project root.  
5. Start the app:  

python run_app.py

This will launch the backend server and automatically open the frontend UI in your browser.  
6. Paste any YouTube video URL or ID in the input field and hit Analyze to get results.

## What This Project Does

- Extracts English transcripts from YouTube videos using `youtube-transcript-api`.
- Generates precise 5-point summaries leveraging the Perplexity AI API.
- Classifies video content into categories using a trained machine learning model (TF-IDF + Naive Bayes).
- Displays results in a simple and responsive web frontend with transcript toggling.
- Saves transcript, summary, and category to text files for recording and review.
- Keeps your API key secure on the backend.
- Designed for quick setup, easy use, and extensibility.

## Strong Points

- **Modular Architecture:** Clear separation of extraction, summarization, classification, and API layers for easy maintenance and future extension.
- **Easy to Run:** Single Python script (`run_app.py`) to start backend and open frontend, no complex environment setup.
- **AI-Powered Summaries:** Uses advanced AI to generate concise, useful summaries.
- **Secure and Lightweight:** API keys never exposed; no heavy database dependency, keeping it simple and portable.
- **Manual Data Tracking:** Text file outputs allow easy record keeping or manual processing.
- **Ready for Improvement:** Supports manual category editing and data collection for future model training.

Feel free to reach out if you want to add features like rate limiting, database persistence, or Docker deployment!
