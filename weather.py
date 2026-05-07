from mcp.server.fastmcp import FastMCP

mcp=FastMCP("Weather")

@mcp.tool()
async def get_weather(location: str) -> str:
    """Return the weather report for the given location or region."""
    return "It's always raining in California"

if __name__=="__main__":
    mcp.run(transport="streamable-http")
