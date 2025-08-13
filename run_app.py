import subprocess
import webbrowser
import time
import sys
import os

def install_requirements():
    print("Installing dependencies from requirements.txt...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def start_backend():
    print("Starting FastAPI backend server...")
    # Start uvicorn in a separate process
    # Use --reload for dev (auto reload on code changes)
    return subprocess.Popen([sys.executable, "-m", "uvicorn", "api:app", "--reload"])

def open_frontend():
    # Open the frontend HTML file in default browser
    frontend_path = os.path.abspath("index.html")
    frontend_url = f"file://{frontend_path}"
    print(f"Opening frontend page in browser: {frontend_url}")
    webbrowser.open(frontend_url)

def main():
    try:
        # Optional: install requirements (comment out if already installed)
        # install_requirements()

        backend_process = start_backend()

        # Wait a bit for the server to start before opening browser
        print("Waiting for backend to start...")
        time.sleep(3)

        open_frontend()

        print("Press Ctrl+C to stop the backend server and exit.")

        # Wait until the backend server process is terminated manually
        backend_process.wait()

    except KeyboardInterrupt:
        print("\nShutting down...")
        backend_process.terminate()
        backend_process.wait()
        print("Backend server stopped. Goodbye!")

if __name__ == "__main__":
    main()
