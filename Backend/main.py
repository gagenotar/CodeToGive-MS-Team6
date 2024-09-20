from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String, Text, Date, TIMESTAMP, Boolean, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from datetime import date, datetime
from dotenv import load_dotenv
import os
import cohere

# Load the .env file
load_dotenv()


# Create FastAPI instance
app = FastAPI()



# Cohere API setup
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
co = cohere.Client(COHERE_API_KEY)

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
    

    # Load the .env file
    load_dotenv()

    # Retrieve the API key from the environment variables
    COHERE_API_KEY = os.getenv('COHERE_API_KEY')
    #print(COHERE_API_KEY)
    #COHERE_API_KEY="7WcD3PeQenuLegXolg2KwuD1riM4YGdgPlEwgblm"
    # Initialize the Cohere client with the API key
    co = cohere.Client(COHERE_API_KEY)

    if not COHERE_API_KEY:
        raise Exception("Cohere API Key is missing. Set the COHERE_API_KEY environment variable.")
        
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



# Fetch a single student by their student_id
@app.get("/student/{student_id}")
def get_student(student_id: int, db: Session = Depends(get_db)):
    # Fetch student from the database using their student_id
    student = db.execute(text("SELECT * FROM students WHERE student_id = :student_id"), {"student_id": student_id}).fetchone()
    
    # If student does not exist, raise a 404 error
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Return student details
    return {
        "student_id": student[0],
        "student_name": student[1],
        "email": student[2],
        "experience": student[4],
        "highest_education_level": student[5],
        "major": student[6],
        "skills": student[8],
        "street": student[9],
        "state": student[10],
        "country": student[11],
        "zipcode": student[12]
    }

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


# Fetch a single job by its job_id
@app.get("/jobs/{job_id}")
def get_job(job_id: int, db: Session = Depends(get_db)):
    # Fetch job from the database using its job_id
    job = db.execute(text("SELECT * FROM jobs WHERE job_id = :job_id"), {"job_id": job_id}).fetchone()
    
    # If job does not exist, raise a 404 error
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    
    # Return job details as a dictionary
    return {
        "job_id": job[0],
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




# Match job to user profile
@app.get("/match_job/{student_id}")
def match_job_to_user(student_id: int, db: Session = Depends(get_db)):
    # Fetch student data from the students table
    student = db.execute(text("""
        SELECT student_name, highest_education_level, major, skills, experience 
        FROM students 
        WHERE student_id = :student_id
    """), {"student_id": student_id}).fetchone()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Unpack student data
    student_name, highest_education_level, major, student_skills, student_experience = student

    # Fetch jobs where deadline hasn't expired and bachelor's or master's required and matching valid majors
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

    print ()

    if not jobs:
        raise HTTPException(status_code=404, detail="No matching jobs found")

    # Filter jobs based on the student's major
    valid_jobs = []
    for job in jobs:
        job_id, title, description, skills_required, experience_required, application_deadline, valid_majors = job
        valid_majors_list = [major.strip().lower() for major in valid_majors.split(',')]
        
        # Check if the student's major is in the valid majors for the job
        if major.lower() in valid_majors_list:
            valid_jobs.append(job)

    if not valid_jobs:
        raise HTTPException(status_code=404, detail="No jobs matched with the student's major")

    # Prepare job matches
    job_matches = []
    
    for job in valid_jobs:
        job_id, title, description, skills_required, experience_required, application_deadline, _ = job
        
        # Prepare a prompt for Cohere API
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
        cleaned_prompt = prompt.strip()
        # Call Cohere API to generate match score
        response = co.generate(
            model='command-xlarge-nightly',  # Cohere's advanced model
            prompt=prompt,
            max_tokens=100,  # Adjust max tokens for a concise response
            temperature=0.7,  # Balance between deterministic and creative responses
            stop_sequences=["\n"]
        )
        match_score = response.generations[0].text.strip()

        # Add the match result to the list
        job_matches.append({
            "job_id": job_id,
            "job_title": title,
            "match_score": match_score,
            "application_deadline": application_deadline
        })

    return job_matches
