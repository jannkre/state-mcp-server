# my_mcp_server.py
from fastmcp.utilities.types import Image, Audio, File
from fastmcp import FastMCP

mcp = FastMCP(name="MyDrawingStateServer")

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
    return Image(path="chart.png")


if __name__ == "__main__":
    mcp.run(transport="streamable-http")