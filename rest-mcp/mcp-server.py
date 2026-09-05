from mcp.server.mcpserver import MCPServer 
import httpx
mcp = MCPServer("JsonPlaceholderMCPServer")
BASE_URL = "https://jsonplaceholder.typicode.com"

@mcp.tool()
async def get_users():
    """
    Get a list of users from the JSONPlaceholder API.
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/users")
        response.raise_for_status()
        return response.json()


@mcp.tool()
async def get_posts(post_id: int):
    """
    Get a specific post by ID from the JSONPlaceholder API.
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/posts/{post_id}")
        response.raise_for_status()
        return response.json()

### Skills
@mcp.tool()
async def get_user_posts(user_id: int):
    """
    User Analysis Skill: Get all posts for a specific user from the JSONPlaceholder API.
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{BASE_URL}/posts", 
            params={"userId": user_id})
        response.raise_for_status()
        user =  response.json()

        response = await client.get(
            f"{BASE_URL}/posts",
            params={"userId": user_id})
        response.raise_for_status() 
        posts = response.json()

        return {"skill": "User Analysis - get_user_posts", "user": user, "posts": posts}

if __name__ == "__main__":
    # mcp.run(transport="streamable-http", host="127.0.0.1", port=8000)
    mcp.run(transport="sse", host="127.0.0.1", port=8000)