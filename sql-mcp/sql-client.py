from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client

import asyncio

async def main():
    async with streamable_http_client("http://localhost:8000/mcp") as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session :

            await session.initialize()
            tools = await session.list_tools()
            print("="*100)

            for tool in tools.tools:
                print(f"Tool: {tool.name}")
                print(f"Description: {tool.description}")
                print("="*100)

            result = await session.call_tool("get_users", {})
            for content in result.content:
                print(content.text)

asyncio.run(main())
