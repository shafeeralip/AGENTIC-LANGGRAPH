from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
def weather(location: str) -> str:
    """
    Returns the current weather condition for a given location.
    """
    return f"The weather in {location} is rainy."


if __name__ =="__main__":
    mcp.run(transport ="streamable-http")

    