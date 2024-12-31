from app.database import get_db
import logging

def create_student(name: str, age: int, grade: str):
    try:
        with get_db() as conn:  # Get the database connection using the context manager
            cursor = conn.cursor()
            cursor.execute("INSERT INTO STUDENTS(Name, Age, Grade) VALUES (?, ?, ?)", (name, age, grade))
            conn.commit()
            logging.info(f"Student {name} added successfully")
    except Exception as e:
        logging.error(f"Error creating student: {e}")
        raise

def get_students():
    try:
        with get_db() as conn:  # Get the database connection using the context manager
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM STUDENTS")
            students = cursor.fetchall()
            logging.info(f"Retrieved {len(students)} students")
            return students
    except Exception as e:
        logging.error(f"Error fetching students: {e}")
        raise

def get_student(student_id: int):
    try:
        with get_db() as conn:  # Get the database connection using the context manager
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM STUDENTS WHERE ID = ?", (student_id,))
            student = cursor.fetchone()
            if not student:
                logging.warning(f"Student with ID {student_id} not found")
            return student
    except Exception as e:
        logging.error(f"Error fetching student with ID {student_id}: {e}")
        raise

def update_student(student_id: int, name: str, age: int, grade: str):
    try:
        with get_db() as conn:  # Get the database connection using the context manager
            cursor = conn.cursor()
            cursor.execute("UPDATE STUDENTS SET Name = ?, Age = ?, Grade = ? WHERE ID = ?", (name, age, grade, student_id))
            conn.commit()
            logging.info(f"Student with ID {student_id} updated successfully")
    except Exception as e:
        logging.error(f"Error updating student with ID {student_id}: {e}")
        raise

def delete_student(student_id: int):
    try:
        with get_db() as conn:  # Get the database connection using the context manager
            cursor = conn.cursor()
            cursor.execute("DELETE FROM STUDENTS WHERE ID = ?", (student_id,))
            conn.commit()
            logging.info(f"Student with ID {student_id} deleted successfully")
    except Exception as e:
        logging.error(f"Error deleting student with ID {student_id}: {e}")
        raise
