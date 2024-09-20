from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String, Text, Date, TIMESTAMP, Boolean, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from datetime import date

# Create FastAPI instance
app = FastAPI()

# MySQL Database URL (with your credentials)
DATABASE_URL = "mysql+pymysql://sql5732473:xUKVrFsRsN@sql5.freemysqlhosting.net:3306/sql5732473"

# Set up the SQLAlchemy engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# SQLAlchemy base model
Base = declarative_base()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# SQLAlchemy models
class Student(Base):
    __tablename__ = "students"
    student_id = Column(Integer, primary_key=True, index=True)
    student_name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    experience = Column(Integer)
    highest_education_level = Column(String(255))
    major = Column(String(255))
    university = Column(String(255))
    skills = Column(Text)
    street = Column(String(255))
    state = Column(String(100))
    country = Column(String(100))
    zipcode = Column(String(20))

class Job(Base):
    __tablename__ = "jobs"
    job_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    skills_required = Column(Text, nullable=True)
    experience_required = Column(Integer)
    street = Column(String(255))
    state = Column(String(100))
    country = Column(String(100))
    zipcode = Column(String(20))
    company_name = Column(String(255))
    salary_range = Column(String(50))
    employment_type = Column(String(50))
    application_deadline = Column(Date)
    bachelors_needed = Column(Boolean, default=False)
    masters_needed = Column(Boolean, default=False)
    valid_majors = Column(Text)
    created_at = Column(TIMESTAMP, default=None)

# Pydantic models for request/response validation

# Student creation model
class StudentCreate(BaseModel):
    student_name: str
    email: str
    password: str
    experience: int
    highest_education_level: str
    major: str
    university: str
    skills: str
    street: str
    state: str
    country: str
    zipcode: str

# Job creation model (now using `datetime.date` instead of SQLAlchemy's `Date`)
class JobCreate(BaseModel):
    title: str
    description: str
    skills_required: str
    experience_required: int
    street: str
    state: str
    country: str
    zipcode: str
    company_name: str
    salary_range: str
    employment_type: str
    application_deadline: date  # <-- Use Python's `datetime.date`
    bachelors_needed: bool
    masters_needed: bool
    valid_majors: str

# GET endpoint to retrieve all students
@app.get("/students", response_model=List[StudentCreate])
def get_students(db: Session = Depends(get_db)):
    students = db.execute(text("SELECT * FROM students")).fetchall()
    if not students:
        raise HTTPException(status_code=404, detail="No students found")
    
    #print(students)
    # Convert each row to a dictionary
    #return [dict(student) for student in students]
       # Mapping tuple indices to column names
    return [
        {
            "student_name": student[1],  # Name is the second field
            "email": student[2],
            "password": student[3],
            "experience": student[4],
            "highest_education_level": student[5],
            "major": student[6],
            "university": student[7],
            "skills": student[8],
            "street": student[9],
            "state": student[10],
            "country": student[11],
            "zipcode": student[12]
        }
        for student in students
    ]

# GET endpoint to retrieve all jobs
@app.get("/jobs", response_model=List[JobCreate])
def get_jobs(db: Session = Depends(get_db)):
    jobs = db.execute(text("SELECT * FROM jobs")).fetchall()
    if not jobs:
        raise HTTPException(status_code=404, detail="No jobs found")
    
    # Convert each row to a dictionary
    #return [dict(job) for job in jobs]
        # Mapping tuple indices to column names
    return [
        {
            "title": job[1],
            "description": job[2],
            "skills_required": job[3],
            "experience_required": job[4],
            "street": job[5],
            "state": job[6],
            "country": job[7],
            "zipcode": job[8],
            "company_name": job[9],
            "salary_range": job[10],
            "employment_type": job[11],
            "application_deadline": job[12],
            "bachelors_needed": job[13],
            "masters_needed": job[14],
            "valid_majors": job[15]
        }
        for job in jobs
    ]

# POST endpoint to add a student
@app.post("/students", response_model=StudentCreate)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db.execute(
        text("INSERT INTO students (student_name, email, password, experience, highest_education_level, major, university, skills, street, state, country, zipcode) "
             "VALUES (:student_name, :email, :password, :experience, :highest_education_level, :major, :university, :skills, :street, :state, :country, :zipcode)"),
        {"student_name": student.student_name, "email": student.email, "password": student.password,
         "experience": student.experience, "highest_education_level": student.highest_education_level,
         "major": student.major, "university": student.university, "skills": student.skills,
         "street": student.street, "state": student.state, "country": student.country, "zipcode": student.zipcode}
    )
    db.commit()
    return student

# POST endpoint to add a job
@app.post("/jobs", response_model=JobCreate)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    db.execute(
        text("INSERT INTO jobs (title, description, skills_required, experience_required, street, state, country, zipcode, company_name, salary_range, employment_type, application_deadline, bachelors_needed, masters_needed, valid_majors) "
             "VALUES (:title, :description, :skills_required, :experience_required, :street, :state, :country, :zipcode, :company_name, :salary_range, :employment_type, :application_deadline, :bachelors_needed, :masters_needed, :valid_majors)"),
        {"title": job.title, "description": job.description, "skills_required": job.skills_required,
         "experience_required": job.experience_required, "street": job.street, "state": job.state,
         "country": job.country, "zipcode": job.zipcode, "company_name": job.company_name, 
         "salary_range": job.salary_range, "employment_type": job.employment_type,
         "application_deadline": job.application_deadline, "bachelors_needed": job.bachelors_needed,
         "masters_needed": job.masters_needed, "valid_majors": job.valid_majors}
    )
    db.commit()
    return job
