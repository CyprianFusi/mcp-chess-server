import requests
from typing import Dict, Any

CHESS_API_BASE = "https://api.chess.com/pub"

headers = {"accept": "application/json",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Python/3.10 requests/2.31.0"}

def get_player_profile(player_name: str) -> Dict[str, Any]:
    """
    Fetches the profile information of a chess.com player.
    Args:
        player_name (str): The username of the chess.com player.

    Returns:
        Dict[str, Any]: Player profile information

    Raises:
        requests.exceptions.HTTPError: If the API request fails
    """
    url = f"{CHESS_API_BASE}/player/{player_name}"
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to fetch player profile for {player_name}: {str(e)}")

def get_player_stats(player_name: str) -> Dict[str, Any]:
    """
    Fetches the statistics of a chess.com player.
    Args:
        player_name (str): The username of the chess.com player.

    Returns:
        Dict[str, Any]: Player statistics

    Raises:
        requests.exceptions.HTTPError: If the API request fails
    """
    url = f"{CHESS_API_BASE}/player/{player_name}/stats"
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to fetch player stats for {player_name}: {str(e)}")