# utils/api_key.py

import os
from getpass import getpass
from openai import OpenAI

def load_openai_client():
    """
    Secure & portable OpenAI API loader.

    It tries these in order:
    1) Google Colab secrets (if available)
    2) Environment variable OPENAI_API_KEY
    3) Secure user prompt (fallback)

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
    if not api_key:
        api_key = os.getenv("OPENAI_API_KEY")

    # 3) Secure promt (fallback)
    if not api_key:
        api_key = getpass("Enter your OpenAI API key: ").strip()

    # Make key available during session
    os.environ["OPENAI_API_KEY"] = api_key

    # Return initialized client
    return OpenAI(api_key=api_key)
