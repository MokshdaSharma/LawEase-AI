import os
from dotenv import load_dotenv


load_dotenv()

class Settings:
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    STORAGE_PATH: str = os.getenv("STORAGE_PATH", "uploads")
    VOICE_OUTPUT_PATH: str = os.getenv("VOICE_OUTPUT_PATH", "voice_outputs")

settings = Settings()
