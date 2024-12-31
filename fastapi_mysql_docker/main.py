from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector
from mysql.connector import Error

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host="mysql",
        user="root",
        password="rootpassword",
        database="fastapi_db"
    )

@app.post("/add_item/")
async def add_item(item: Item):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO items (name, description) VALUES (%s, %s)", (item.name, item.description))
        conn.commit()
        cursor.close()
        conn.close()
        return {"message": "Item added successfully!"}
    except Error as e:
        return {"error": str(e)}

@app.get("/items/")
async def get_items():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM items")
        items = cursor.fetchall()
        cursor.close()
        conn.close()
        return {"items": items}
    except Error as e:
        return {"error": str(e)}
