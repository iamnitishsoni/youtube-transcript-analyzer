# YouTube Transcript Processor (2025)

A modular Python project that extracts YouTube video transcripts, summarizes key points using the Perplexity API, categorizes video content, and offers a simple web frontend powered by FastAPI.

---

## Project Overview

This project processes YouTube videos by:

1. Extracting the transcript from any given video URL or ID.
2. Summarizing the transcript into 5 concise, categorized bullet points using the Perplexity API.
3. Categorizing the video content into topics like Education, Sports, Technology using a simple ML classifier.
4. Providing a user-friendly web frontend to analyze videos interactively.

---

## Features

- **Transcript Extraction** using `youtube-transcript-api`.
- **Summarization** via Perplexity API with OpenAI-compatible client.
- **Video Categorization** using TF-IDF + Naive Bayes classifier.
- **Clean separation** of each step into modular Python scripts.
- **FastAPI backend** exposing `/analyze` API endpoint for frontend integration.
- **Simple HTML/JS frontend** to enter URLs and display results.
- Works with full YouTube URLs, shortened URLs, or video IDs.

---

## Folder Structure

youtube_transcript_project/
├── app/
│ ├── init.py
│ ├── extractor.py # Transcript extraction functions
│ ├── summarizer.py # Summarization logic via Perplexity API
│ ├── classifier.py # Video categorization model & functions
│ └── pipeline.py # Orchestrates full pipeline usage
├── api.py # FastAPI server exposing backend to frontend
├── index.html # Frontend web page (HTML + JavaScript)
├── PPLX_API_KEY.txt # Your Perplexity API key (keep secure)
├── requirements.txt # Python dependencies
├── README.md # This documentation file
└── README.md


---

## Setup Instructions

### 1. **Clone or Download This Repository**

Create a folder on your PC and add the files as structured above.

### 2. **Install Python Dependencies**

Make sure Python 3.7+ is installed, then in your project directory run:

pip install -r requirements.txt


This installs:

- `fastapi`
- `uvicorn`
- `youtube-transcript-api`
- `openai`
- `scikit-learn`
- `python-dotenv`

### 3. **Add Your Perplexity API Key**

- Create (or copy) the file `PPLX_API_KEY.txt` in the project root.
- Paste your Perplexity API key as a single line, no extra spaces or newlines.

### 4. **Run the Backend API**

Start the FastAPI server by running:

uvicorn api:app --reload


This runs your backend on:

http://localhost:8000/


You can visit `http://localhost:8000/docs` to see auto-generated API documentation and test endpoints.

### 5. **Open the Frontend**

Open `index.html` in a web browser (by double-clicking or using "Open with live server" in VS Code).

### 6. **Use the Web UI**

- Paste a YouTube video URL or Video ID into the input box.
- Click **Analyze**.
- View category, 5-line summary, and transcript (expandable).

---

## Usage Details

### API Endpoint

- **POST** `/analyze`
- **Request body:**

{
"youtube_url": "https://www.youtube.com/watch?v=videoID"
}


- **Response body:**

{
"video_id": "videoID",
"summary": [
"Headline 1",
"Headline 2",
"Headline 3",
"Headline 4",
"Headline 5"
],
"category": "Education",
"transcript": "Full transcript text ..."
}


---

## Development Notes

- Each Python module focuses on one task for easy testing and debugging.
- Transcripts are extracted using the instance-based `youtube-transcript-api`.
- Summarization is done via Perplexity API’s OpenAI-compatible interface.
- The classification uses a fallback ML model trained on sample data for demo purposes.
- Future improvements can include caching results, batch processing, or richer frontend UX.

---

## Troubleshooting

- **No transcript found:** Make sure the YouTube video has subtitles enabled.
- **API key errors:** Ensure your Perplexity API key is valid and placed correctly in `PPLX_API_KEY.txt`.
- **CORS errors:** When testing locally, your browser might block requests; use the backend’s CORS middleware as configured.
- **Port conflicts:** If port 8000 is busy, run Uvicorn on a different port using `--port` flag.

---

## License

[MIT License](LICENSE) (you can add a license file if you want to open source it)

---

## Acknowledgments

- The `youtube-transcript-api` library by `@jwvw`.
- [Perplexity AI](https://perplexity.ai) for their API and support.
- OpenAI API client for easy integration.
- FastAPI team for an excellent async web framework.

---

## Contact

For questions or help, reach out to:

- **Nitish Soni** (nitishkumarsanjaysoni@gmail.com)

---

Happy coding and analyzing! 🚀
