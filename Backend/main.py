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
from fastapi.middleware.cors import CORSMiddleware

# Load the .env file
load_dotenv()

# Create FastAPI instance
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify the domains you want to allow, e.g., ["http://localhost", "https://example.com"]
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers
)

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

# Pydantic model for minimal student registration (only name and password)
class StudentRegister(BaseModel):
    student_name: str
    email: str
    password: str        

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
    student_id: str
    student_name: str
    email: str
    password: str
    experience: Optional[int] = None
    highest_education_level: Optional[str] = None
    major: Optional[str] = None
    university: Optional[str] = None
    skills: Optional[str] = None
    street: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    zipcode: Optional[str] = None

# Job creation model (now using `datetime.date` instead of SQLAlchemy's `Date`)
class JobCreate(BaseModel):
    job_id: str
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

# Pydantic model for updating student details (only optional fields)
class StudentUpdate(BaseModel):
    experience: Optional[int] = None
    highest_education_level: Optional[str] = None
    major: Optional[str] = None
    university: Optional[str] = None
    skills: Optional[str] = None
    street: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    zipcode: Optional[str] = None



# Error handling for duplicate email
@app.exception_handler(HTTPException)
def http_exception_handler(request, exc):
    return {"error": str(exc.detail)}




# Pydantic models for login
class LoginModel(BaseModel):
    email: str
    password: str

@app.post("/login")
def login(user: LoginModel, db: Session = Depends(get_db)):
    # Check if the user exists
    existing_user = db.execute(
        text("SELECT * FROM students WHERE email = :email"),
        {"email": user.email}
    ).fetchone()

    if not existing_user:
        return JSONResponse(status_code=404, content={"detail": "User not found"})

    # Check if the password matches
    if existing_user[3] != user.password:  # Assuming password is the 4th field in the row
        return JSONResponse(status_code=400, content={"detail": "Invalid password"})

    # Return student_id and success message
    return {"message": "Login successful", "student_id": existing_user[0]}  # Assuming student_id is the 1st field





# GET endpoint to retrieve all students
@app.get("/students", response_model=List[StudentCreate])
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
# Fetch a single student by their student_id
# Fetch a single student by their student_id
# Fetch a single student by their student_id
@app.get("/students/{student_id}")
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


# GET endpoint to retrieve all jobs
@app.get("/jobs", response_model=List[JobCreate])
def get_jobs(db: Session = Depends(get_db)):
    jobs = db.execute(text("SELECT * FROM jobs")).fetchall()
    if not jobs:
        #raise HTTPException(status_code=404, detail="No jobs found")
        return JSONResponse(status_code=404, content={"No jobs found"})

    return [

        {
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
        for job in jobs
    ]

# POST endpoint to add a student (for registration)
@app.post("/students/register")
def create_student(student: StudentRegister, db: Session = Depends(get_db)):
    try:
        # Insert the student data into the database
        db.execute(
            text("INSERT INTO students (student_name, email, password) "
                 "VALUES (:student_name, :email, :password)"),
            {"student_name": student.student_name, "email": student.email, "password": student.password}
        )
        db.commit()
        return {"message":"student successfully registered"}
    except Exception as e:
        # Handle duplicate email case
        if "Duplicate entry" in str(e):
            return JSONResponse(status_code=400, content="Email already registered")
        else:
            return JSONResponse(status_code=500, content="An error occurred while creating the student")

# PUT endpoint to update student details
from fastapi.responses import JSONResponse

@app.post("/students/update/{student_id}")
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


# Fetch a single job by its job_id
@app.get("/jobs/{job_id}")
def get_job(job_id: int, db: Session = Depends(get_db)):
    job = db.execute(text("SELECT * FROM jobs WHERE job_id = :job_id"), {"job_id": job_id}).fetchone()
    if not job:
        #raise HTTPException(status_code=404, detail="Job not found")
        return JSONResponse(status_code=404, content="Job not found")

    return {
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
    # Fetch student data
    student = db.execute(text("""
        SELECT student_name, highest_education_level, major, skills, experience 
        FROM students 
        WHERE student_id = :student_id
    """), {"student_id": student_id}).fetchone()

    if not student:
        #raise HTTPException(status_code=404, detail="Student not found")
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
        #raise HTTPException(status_code=404, detail="No matching jobs found")
        return JSONResponse(status_code=404, content="No matching jobs found")


    # Filter jobs based on student's major
    valid_jobs = []
    for job in jobs:
        job_id, title, description, skills_required, experience_required, application_deadline, valid_majors = job
        valid_majors_list = [major.strip().lower() for major in valid_majors.split(',')]
        if major.lower() in valid_majors_list:
            valid_jobs.append(job)

    if not valid_jobs:
        #raise HTTPException(status_code=404, detail="No jobs matched with the student's major")
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
