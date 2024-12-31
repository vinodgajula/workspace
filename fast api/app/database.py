import sqlite3
from contextlib import contextmanager
import logging

DB_NAME = "STUDENTS.DB"

# Set up logging
logging.basicConfig(level=logging.INFO)

def create_table():
    try:
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute(''' 
                CREATE TABLE IF NOT EXISTS STUDENTS(
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT NOT NULL,
                    Age INTEGER,
                    Grade TEXT NOT NULL
                )
            ''')
            conn.commit()
            logging.info("Database and table initialized successfully")
    except Exception as e:
        logging.error(f"Error initializing database: {e}")
# Assuming get_db() is defined as in the previous code
@contextmanager
def get_db():
    conn = None
    try:
        conn = sqlite3.connect(DB_NAME)
        yield conn  # Yield the actual database connection
    except Exception as e:
        logging.error(f"Database connection error: {e}")
        raise
    finally:
        if conn:
            conn.close()
            logging.info("Database connection closed")

