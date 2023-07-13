import requests

# Make a request to the Streamlit server shutdown endpoint
requests.get("http://localhost:8501/stop", params={"key": "your_secret_key"})
