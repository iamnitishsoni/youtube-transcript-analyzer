from setuptools import setup, find_packages

setup(
    name="youtube_transcript_project",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "youtube-transcript-api",
        "openai",
        "scikit-learn",
        "python-dotenv",
        "slowapi"
    ],
    author="Your Name",
    description="YouTube Transcript Analyzer: Extract, Summarize, Categorize",
    python_requires=">=3.7",
)

# to install this
# pip install -e .
