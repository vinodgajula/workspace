from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import sqlite3
from typing import List

# FastAPI app initialization
app = FastAPI()

# Static and templates setup
#app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Database setup
def init_db():
    conn = sqlite3.connect("crud_app.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT NOT NULL
        )"""
    )
    conn.commit()
    conn.close()

init_db()

# Pydantic model for Item
class Item(BaseModel):
    name: str
    description: str

# Routes
@app.get("/")
async def read_root(request: Request):
    conn = sqlite3.connect("crud_app.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    conn.close()
    return templates.TemplateResponse("index.html", {"request": request, "items": items})

@app.post("/create")
async def create_item(name: str = Form(...), description: str = Form(...)):
    conn = sqlite3.connect("crud_app.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO items (name, description) VALUES (?, ?)", (name, description))
    conn.commit()
    conn.close()
    return RedirectResponse(url="/", status_code=303)

@app.post("/update/{item_id}")
async def update_item(item_id: int, name: str = Form(...), description: str = Form(...)):
    conn = sqlite3.connect("crud_app.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE items SET name = ?, description = ? WHERE id = ?", (name, description, item_id))
    conn.commit()
    conn.close()
    return RedirectResponse(url="/", status_code=303)

@app.get("/delete/{item_id}")
async def delete_item(item_id: int):
    conn = sqlite3.connect("crud_app.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM items WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()
    return RedirectResponse(url="/", status_code=303)

