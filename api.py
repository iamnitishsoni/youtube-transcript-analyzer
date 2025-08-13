# api.py

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

from app.extractor import extract_transcript, extract_video_id
from app.summarizer import summarize_five_lines
from app.classifier import load_classifier, categorize

# Initialize FastAPI app
app = FastAPI()

# Initialize the rate limiter with remote IP as key
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

# Register rate limit exceeded handler
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Enable CORS for local development; adjust allowed origins for production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class AnalyzeRequest(BaseModel):
    youtube_url: str

# Endpoint with rate limiting: 5 requests per minute per IP
@app.post("/analyze")
@limiter.limit("5/minute")
def analyze_video(request: Request, req: AnalyzeRequest):
    try:
        video_id = extract_video_id(req.youtube_url)
        transcript = extract_transcript(video_id)
        if not transcript:
            raise HTTPException(status_code=404, detail="Transcript not found.")
        summary = summarize_five_lines(transcript)
        clf, vectorizer, categories = load_classifier()
        category = categorize(transcript, clf, vectorizer, categories)

        return {
            "video_id": video_id,
            "summary": summary,
            "category": category,
            "transcript": transcript
        }

    except HTTPException:
        # Re-raise HTTP exceptions (like 404) as is
        raise

    except Exception as e:
        # Return 500 for other unhandled exceptions
        raise HTTPException(status_code=500, detail=str(e))
