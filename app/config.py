import os
from dotenv import load_dotenv

load_dotenv()

# Get the key without raising an immediate error
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def validate_config():
    """Call this only when you are about to use the LLM"""
    if not OPENAI_API_KEY or OPENAI_API_KEY == "your_key_here_later":
        raise ValueError(
            "OPENAI_API_KEY is missing. Please add it to your .env file "
            "or switch to a local model like Ollama."
        )
