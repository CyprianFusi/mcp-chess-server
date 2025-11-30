from mcp.server.fastmcp import FastMCP
from typing import Dict, Any

mcp = FastMCP('Chess.com')

from .chess_api import get_player_profile, get_player_stats

@mcp.tool()
def get_chess_player_profile(player_name: str) -> Dict[str, Any]:
    """Get the public profile for a Chess.com player by player_name."""
    return get_player_profile(player_name)

@mcp.tool()
def get_chess_player_stats(player_name: str) -> Dict[str, Any]:
    """Get the stats for a Chess.com player by player_name."""
    return get_player_stats(player_name)

def main() -> None:
    mcp.run()

if __name__ == "__main__":
    main()
