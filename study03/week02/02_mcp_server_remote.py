from typing import Optional
from datetime import datetime
from mcp.server.fastmcp import FastMCP

import pytz

mcp = FastMCP(
    "TimeService", # Name of the MCP
    instructions="You are a time assistant that can provide the current time for different timezones.",  # Instructions for the LLM on how to use this tool
    host="0.0.0.0",
    auth_server_provider=None,
    port=8005
)

@mcp.tool()
async def get_current_time(timezone: Optional[str] = "Asia/Seoul") -> str:
    """
    Get current time for the specified timezone.
    
    This function returns the current time for the specified timezone.
    If no timezone is specified, the default timezone is "Asia/Seoul".

    Args:
        timezone (str): The timezone to get the current time for. Default is "Asia/Seoul".

    Returns:
        str: A string containing the current time for the specified timezone.
    """
    try:
        print(f"Getting current time for {timezone}")
        
        # Get the timezone object
        timezone = pytz.timezone(timezone)
        # Get the current time
        current_time = datetime.now(timezone)
        # Format the current time
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        # Return the formatted time
        return f"Current time in {timezone}: {formatted_time}"  
    except pytz.exceptions.UnknownTimeZoneError:
        return f"Error: Invalid timezone '{timezone}'. Please use a valid timezone name."
    except Exception as e:
        return f"Error: {str(e)}"
    
if __name__ == "__main__":
    print("Starting MCP server...")
    mcp.run(transport="sse")
