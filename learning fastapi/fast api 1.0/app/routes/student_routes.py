from fastapi import APIRouter, HTTPException, Depends
from app.schemas import Student
from app.database import get_db
from app.crud import create_student, get_students, get_student, update_student, delete_student
import logging

router = APIRouter(prefix="/students", tags=["Students"])

@router.post("/")
def add_student(student: Student):
    try:
        create_student(student.name, student.age, student.grade)
        return {"message": "Student created successfully"}
    except Exception as e:
        logging.error(f"Failed to create student: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/")
def list_students():
    try:
        students = get_students()
        return {"students": students}
    except Exception as e:
        logging.error(f"Failed to retrieve students: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/{student_id}")
def retrieve_student(student_id: int):
    try:
        student = get_student(student_id)
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
        return {"student": student}
    except HTTPException as http_ex:
        raise http_ex
    except Exception as e:
        logging.error(f"Failed to retrieve student with ID {student_id}: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.put("/{student_id}")
def modify_student(student_id: int, student: Student):
    try:
        update_student(student_id, student.name, student.age, student.grade)
        return {"message": "Student updated successfully"}
    except Exception as e:
        logging.error(f"Failed to update student with ID {student_id}: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.delete("/{student_id}")
def remove_student(student_id: int):
    try:
        delete_student(student_id)
        return {"message": "Student deleted"}
    except Exception as e:
        logging.error(f"Failed to delete student with ID {student_id}: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
