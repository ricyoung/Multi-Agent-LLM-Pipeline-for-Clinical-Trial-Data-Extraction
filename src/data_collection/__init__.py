
"""
Functions for fetching clinical trial data from ClinicalTrials.gov.
"""

import requests
import pandas as pd
import time
from typing import Dict, List, Any

def fetch_clinical_trials(query: str, max_trials: int = 100) -> pd.DataFrame:
    """
    Fetch clinical trials from ClinicalTrials.gov API.
    
    Args:
        query: Search query
        max_trials: Maximum number of trials to retrieve
        
    Returns:
        DataFrame containing trial data
    """
    base_url = "https://clinicaltrials.gov/api/v2/studies"
    all_results = []
    
    # Add pagination and error handling
    offset = 0
    page_size = 100
    
    while offset < max_trials:
        params = {
            "query": query,
            "format": "json",
            "offset": offset,
            "limit": min(page_size, max_trials - offset)
        }
        
        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            data = response.json()
            
            if 'studies' not in data:
                break
                
            all_results.extend(data['studies'])
            
            # Check if we've reached the end
            if len(data['studies']) < page_size:
                break
                
            offset += page_size
            time.sleep(1)  # Avoid rate limiting
            
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error fetching clinical trials: {e}")
    
    return pd.DataFrame(all_results)
