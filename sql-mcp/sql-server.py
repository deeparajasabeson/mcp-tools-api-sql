from mcp.server.mcpserver import MCPServer 
from mssql_python import connect
from dotenv import load_dotenv
import os
import traceback

load_dotenv()

mcp = MCPServer("SQL SERVER MCP")
DATABASE_URL = os.getenv("DATABASE_URL")

def get_connection():
    return connect(DATABASE_URL)

@mcp.tool()
def get_users():
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM dbo.users")

            rows = cursor.fetchall()

            print(f"Rows returned: {len(rows)}")
            return [tuple(row) for row in rows]
        
    except Exception as e:
        print("ERROR in get_users:")
        print(type(e).__name__)
        print(str(e))
        traceback.print_exc()
        raise

if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="127.0.0.1", port=8000)
