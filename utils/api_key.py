# utils/api_key.py

import os
from openai import OpenAI

def load_openai_client():
    """
    Secure & portable OpenAI API loader.

    It tries these in order:
    1) Google Colab secrets (if running in Colab)
    2) Environment variable OPENAI_API_KEY
    3) Manual user input (last fallback)

    Returns:
        OpenAI: Initialized OpenAI client.
    """
    api_key = None

    # 1) Google Colab secrets if available
    try:
        from google.colab import userdata
        api_key = userdata.get("OPENAI_API_KEY")
    except Exception:
        pass

    # 2) Environment variables
    if api_key is None:
        api_key = os.getenv("OPENAI_API_KEY")

    # 3) Manual input (fallback)
    if api_key is None:
        api_key = input("Enter your OpenAI API key: ").strip()

    # Make key available globally for other tools/libraries
    os.environ["OPENAI_API_KEY"] = api_key

    # Return initialized client
    return OpenAI(api_key=api_key)
