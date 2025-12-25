# my_mcp_server.py
from fastmcp.utilities.types import Image, Audio, File
from mcp.server.fastmcp import FastMCP
from starlette.responses import JSONResponse

mcp = FastMCP(host="0.0.0.0", stateless_http=True)

@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two numbers together"""
    return a + b

@mcp.tool()
def multiply_numbers(a: int, b: int) -> int:
    """Multiply two numbers together"""
    return a * b

@mcp.tool()
def greet_user(name: str) -> str:
    """Greet a user by name"""
    return f"Hello, {name}! Nice to meet you."

@mcp.tool()
def get_chart() -> Image:
    """Generate a chart image."""
    return {"image": Image(path="chart.png").to_image_content()}


if __name__ == "__main__":
    mcp.run(transport="streamable-http")