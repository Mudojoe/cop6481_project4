import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()  # This loads the .env file at the application startup

def get_openai_client():
    """
    Initializes and returns an OpenAI client configured with an API key from environment variables.

    Returns:
        OpenAI: A client object ready to interact with OpenAI API.

    Raises:
        ValueError: If the API key is not found.
    """
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("API Key not found. Set OPENAI_API_KEY environment variable.")
    return OpenAI(api_key=api_key)
