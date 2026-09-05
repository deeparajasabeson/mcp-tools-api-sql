from dotenv import load_dotenv
from mssql_python import connect
import os

load_dotenv()

connection_string = os.getenv("DATABASE_URL")

print(connection_string)

conn = connect(connection_string)

print("CONNECTED")

cursor = conn.cursor()

cursor.execute("SELECT DB_NAME()")
print("Database:", cursor.fetchone())

cursor.execute("""
    SELECT TABLE_SCHEMA, TABLE_NAME
    FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_NAME = 'users'
""")

print("Tables:", cursor.fetchall())

cursor.execute("SELECT * FROM dbo.users")

rows = cursor.fetchall()

print("Users:")
for row in rows:
    print(row)

conn.close()