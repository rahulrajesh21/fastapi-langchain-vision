import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") or os.getenv("API_KEY", "")
MODEL_NAME = os.getenv("MODEL_NAME","google_genai:gemini-3.5-flash-lite")