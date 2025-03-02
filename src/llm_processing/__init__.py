
"""
Functions for processing clinical trial data with LLMs.
"""

import json
import os
import requests
import time
from typing import Dict, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def send_llm_request(model_name: str, prompt: str, max_retries: int = 3) -> Dict:
    """
    Send request to LLM via OpenRouter API.
    
    Args:
        model_name: Name of the model to use
        prompt: Prompt to send to the model
        max_retries: Maximum number of retries
        
    Returns:
        Dictionary containing the model response
    """
    from src.utils import extract_json_from_text, retry_with_backoff
    
    if not OPENROUTER_API_KEY:
        raise ValueError("OpenRouter API key not found. Set OPENROUTER_API_KEY in .env file.")
    
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENROUTER_API_KEY}"
    }
    
    data = {
        "model": model_name,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.5,
        "max_tokens": 1500
    }
    
    def _make_request():
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        
        response_data = response.json()
        if "choices" in response_data and len(response_data["choices"]) > 0:
            content = response_data["choices"][0]["message"]["content"]
            return extract_json_from_text(content)
        else:
            raise ValueError("Invalid response format from OpenRouter API")
    
    return retry_with_backoff(_make_request, max_retries=max_retries, initial_backoff=1)
