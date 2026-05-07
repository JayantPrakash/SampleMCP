# SampleMCP

A simple Python project demonstrating how to build and connect MCP servers using `FastMCP`, LangChain MCP adapters, LangGraph, and OpenAI.

## Features

* Math MCP server using `stdio`
* Weather MCP server using `streamable-http`
* LangChain MCP client connecting to multiple MCP servers
* LangGraph ReAct agent using MCP tools
* Example tool calls for math and weather queries

## Project Structure

```text
SampleMCP/
├── client.py          # MCP client + LangGraph agent
├── mathserver.py      # Math MCP server with add/multiply tools
├── weather.py         # Weather MCP server using streamable HTTP
├── main.py            # Basic sample entry point
├── pyproject.toml     # Project metadata and dependencies
├── requirements.txt   # Python dependencies
└── README.md
```

## Requirements

* Python 3.12+
* OpenAI API key
* Optional: Groq API key

## Installation

Clone the repository:

```bash
git clone https://github.com/JayantPrakash/SampleMCP.git
cd SampleMCP
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Or using `uv`:

```bash
uv sync
```

## Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
GROQ_API_KEY=your_groq_api_key
```

## Running the MCP Servers

### 1. Start the Weather Server

The weather server uses `streamable-http`.

```bash
python weather.py
```

By default, it exposes the MCP endpoint at:

```text
http://localhost:8000/mcp
```

### 2. Math Server

The math server uses `stdio` and is started automatically by the client through:

```python
"command": "python",
"args": ["mathserver.py"],
"transport": "stdio"
```

## Running the Client

In a separate terminal, run:

```bash
python client.py
```

The client connects to:

* `mathserver.py` through `stdio`
* `weather.py` through `streamable_http`

It then creates a LangGraph ReAct agent and asks:

```text
what's (3 + 5) x 12?
```

and:

```text
what is the weather in California?
```

## MCP Tools

### Math Server

Defined in `mathserver.py`.

```python
add(a: int, b: int) -> int
```

Adds two numbers.

```python
multiple(a: int, b: int) -> int
```

Multiplies two numbers.

### Weather Server

Defined in `weather.py`.

```python
get_weather(location: str) -> str
```

Returns a sample weather response for a given location.

## Notes

* `mathserver.py` uses `transport="stdio"`.
* `weather.py` uses `transport="streamable-http"`.
* In `client.py`, the streamable HTTP transport is configured as `streamable_http`.
* Make sure the weather server is running before executing `client.py`.

## Example Output

```text
Math response: 96
Weather response: It's always raining in California
```
