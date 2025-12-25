# State MCP Server

A FastMCP server providing mathematical operations and chart generation capabilities.

## Features

- **Mathematical Operations**: Add and multiply numbers
- **User Greeting**: Personalized greeting functionality
- **Chart Generation**: Generate and serve chart images

## Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/state-mcp-server.git
cd state-mcp-server
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the server:
```bash
python main.py
```

The server will start on `0.0.0.0` using the streamable-http transport protocol.

## Tools

- `add_numbers(a: int, b: int)` - Add two numbers together
- `multiply_numbers(a: int, b: int)` - Multiply two numbers together
- `greet_user(name: str)` - Greet a user by name
- `get_chart()` - Generate a chart image

## Requirements

- Python 3.7+
- mcp
- fastmcp

## License

MIT

