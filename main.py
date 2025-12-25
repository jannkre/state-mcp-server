# my_mcp_server.py
from fastmcp.utilities.types import Image, Audio, File
from fastmcp import FastMCP
import requests

mcp = FastMCP(name="MyDrawingStateServer")

@mcp.tool()
def get_drawing() -> Image:
    """Get the current drawing state."""
    image_url = "https://math-drawings.s3.eu-central-1.amazonaws.com/current_state.png"
    response = requests.get(image_url)
    return Image(data=response.content, format="png")


if __name__ == "__main__":
    mcp.run(transport="streamable-http")