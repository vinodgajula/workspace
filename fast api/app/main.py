from fastapi import FastAPI
from app.database import create_table
from app.routes.student_routes import router as student_router
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Initialize FastAPI
app = FastAPI()

# Include Routes
app.include_router(student_router)

# Initialize Database
create_table()

@app.get("/")
async def home():
    logging.info("Home endpoint accessed")
    return {"message": "Welcome to the Student Management API"}
