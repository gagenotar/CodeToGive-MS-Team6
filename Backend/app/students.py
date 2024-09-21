from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy import create_engine, Column, Integer, String, Text, Date, TIMESTAMP, Boolean, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from datetime import date, datetime
from dotenv import load_dotenv
import os
import cohere
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.models import * # Import models from models.py
from app.database import get_db  # Import DB session from database.py
from fastapi import APIRouter, Depends, HTTPException  # Import APIRouter here


router = APIRouter()

COHERE_API_KEY = os.getenv("COHERE_API_KEY")
co = cohere.Client(COHERE_API_KEY)

# Register a new student
@router.post("/students/register")
def create_student(student: StudentRegister, db: Session = Depends(get_db)):
    try:
        db.execute(
            text("INSERT INTO students (student_name, email, password) VALUES (:student_name, :email, :password)"),
            {"student_name": student.student_name, "email": student.email, "password": student.password}
        )
        db.commit()
        return {"message": "Student successfully registered"}
    except Exception as e:
        if "Duplicate entry" in str(e):
            return JSONResponse(status_code=400, content="Email already registered")
        return JSONResponse(status_code=500, content="An error occurred")

# GET endpoint to retrieve all students
@router.get("/students", response_model=List[StudentCreate])
def get_students(db: Session = Depends(get_db)):
    students = db.execute(text("SELECT * FROM students")).fetchall()
    if not students:
        #raise HTTPException(status_code=404, detail="No students found")
        return JSONResponse(status_code=404, content={"detail": "Students not found"})

    return [
        {
            "student_id": student[0],
            "student_name": student[1] or "Unknown",  # Handle NULL with a default value
            "email": student[2] or "No email provided",  # Handle NULL with a default value
            "password": student[3] or "No password set",  # Handle NULL with a default value
            "experience": student[4] or 0,  # Handle NULL with a default integer value
            "highest_education_level": student[5] or "Unknown",  # Handle NULL with a default value
            "major": student[6] or "Unknown",  # Handle NULL with a default value
            "university": student[7] or "Unknown",  # Handle NULL with a default value
            "skills": student[8] or "No skills listed",  # Handle NULL with a default value
            "street": student[9] or "No street provided",  # Handle NULL with a default value
            "state": student[10] or "No state provided",  # Handle NULL with a default value
            "country": student[11] or "No country provided",  # Handle NULL with a default value
            "zipcode": student[12] or "No zipcode provided"  # Handle NULL with a default value
        }
        for student in students
    ]

@router.post("/students/update/{student_id}")
def update_student(student_id: int, student: StudentUpdate, db: Session = Depends(get_db)):
    # Fetch the student by ID
    existing_student = db.execute(text("SELECT * FROM students WHERE student_id = :student_id"), {"student_id": student_id}).fetchone()
    if not existing_student:
        return JSONResponse(status_code=404, content={"message": "Student not found"})

    # Build dynamic query for updating only provided fields
    update_fields = {}
    
    if student.experience is not None:
        update_fields["experience"] = student.experience
    if student.highest_education_level is not None:
        update_fields["highest_education_level"] = student.highest_education_level
    if student.major is not None:
        update_fields["major"] = student.major
    if student.university is not None:
        update_fields["university"] = student.university
    if student.skills is not None:
        update_fields["skills"] = student.skills
    if student.street is not None:
        update_fields["street"] = student.street
    if student.state is not None:
        update_fields["state"] = student.state
    if student.country is not None:
        update_fields["country"] = student.country
    if student.zipcode is not None:
        update_fields["zipcode"] = student.zipcode

    # If no fields are provided for update, return error
    if not update_fields:
        return JSONResponse(status_code=400, content={"message": "No fields to update"})
    
    # Prepare SQL query dynamically
    set_clause = ", ".join([f"{key} = :{key}" for key in update_fields])
    update_query = f"UPDATE students SET {set_clause} WHERE student_id = :student_id"

    # Execute the query
    db.execute(text(update_query), {"student_id": student_id, **update_fields})
    db.commit()

    return {"message": "Student details updated successfully"}


# Fetch a single student by their student_id
# Fetch a single student by their student_id
@router.get("/students/{student_id}")
def get_student(student_id: int, db: Session = Depends(get_db)):
    # Query for the student
    student = db.execute(
        text("SELECT * FROM students WHERE student_id = :student_id"),
        {"student_id": student_id}
    ).fetchone()

    # If student is not found, return a JSONResponse with a 404 status
    if not student:
        return JSONResponse(status_code=404, content="Student not found")

    # Return the student details while handling possible `None` values
    return {
        "student_id": student[0],
        "student_name": student[1],
        "email": student[2],
        "experience": student[4] if student[4] is not None else 0,
        "highest_education_level": student[5] if student[5] is not None else "",
        "major": student[6] if student[6] is not None else "",
        "skills": student[8] if student[8] is not None else "",
        "street": student[9] if student[9] is not None else "",
        "state": student[10] if student[10] is not None else "",
        "country": student[11] if student[11] is not None else "",
        "zipcode": student[12] if student[12] is not None else ""
    }


@router.get("/match_job/{student_id}")
def match_job_to_user(student_id: int, db: Session = Depends(get_db)):
    # Fetch student data
    student = db.execute(text("""
        SELECT student_name, highest_education_level, major, skills, experience 
        FROM students 
        WHERE student_id = :student_id
    """), {"student_id": student_id}).fetchone()

    if not student:
        return JSONResponse(status_code=404, content="Student not found")

    student_name, highest_education_level, major, student_skills, student_experience = student

    # Fetch jobs where deadline hasn't expired and degree matches
    jobs = db.execute(text("""
        SELECT job_id, title, description, skills_required, experience_required, application_deadline, valid_majors
        FROM jobs 
        WHERE application_deadline >= :current_date
        AND (
            (bachelors_needed = 1 AND :highest_education_level = 'Bachelors')
            OR (masters_needed = 1 AND :highest_education_level = 'Masters')
        )
    """), {
        "current_date": datetime.today().date(),
        "highest_education_level": highest_education_level
    }).fetchall()

    if not jobs:
        return JSONResponse(status_code=404, content="No matching jobs found")

    # Filter jobs based on student's major
    valid_jobs = []
    for job in jobs:
        job_id, title, description, skills_required, experience_required, application_deadline, valid_majors = job
        if valid_majors:
         valid_majors_list = [major.strip().lower() for major in valid_majors.split(',')]
        if major.lower() in valid_majors_list:
            valid_jobs.append(job)

    if not valid_jobs:
        return JSONResponse(status_code=404, content="No jobs matched with the student's major")

    job_matches = []
    for job in valid_jobs:
        job_id, title, description, skills_required, experience_required, application_deadline, _ = job

        prompt = f"""
        Job Title: {title}
        Job Description: {description}
        Required Skills: {skills_required}
        Required Experience: {experience_required} years
        
        Student Profile:
        Name: {student_name}
        Skills: {student_skills}
        Experience: {student_experience} years
        
        Based on the job description and student's profile, return a match score between 0 and 1 and provide reasoning.
        """
        response = co.generate(
            model='command-xlarge-nightly',
            prompt=prompt,
            max_tokens=100,
            temperature=0.7,
            stop_sequences=["\n"]
        )
        match_score = response.generations[0].text.strip()

        job_matches.append({
            "job_id": job_id,
            "job_title": title,
            "match_score": match_score,
            "application_deadline": application_deadline
        })

    return job_matches
