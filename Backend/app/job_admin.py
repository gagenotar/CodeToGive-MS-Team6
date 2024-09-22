from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import AdminRegisterModel, AdminLoginModel , JobCreate
from app.database import get_db
from fastapi.responses import JSONResponse
from sqlalchemy import text  # <-- Add this import
from typing import List, Optional
import cohere
import os



router = APIRouter()

COHERE_API_KEY = os.getenv("COHERE_API_KEY")
co = cohere.Client(COHERE_API_KEY)

# Job admin login
@router.post("/job_admin/login")
def admin_login(admin: AdminLoginModel, db: Session = Depends(get_db)):
    existing_admin = db.execute(text("SELECT * FROM job_admin WHERE email = :email"), {"email": admin.email}).fetchone()
    if not existing_admin:
        return JSONResponse(status_code=404, content={"detail": "Admin not found"})
    if existing_admin[3] != admin.password:
        return JSONResponse(status_code=400, content={"detail": "Invalid password"})
    return {"message": "Login successful", "job_admin_id": existing_admin[0]}

# Job admin register
@router.post("/job_admin/register")
def register_job_admin(admin: AdminRegisterModel, db: Session = Depends(get_db)):
    db.execute(
        text("INSERT INTO job_admin (name, email, password) VALUES (:name, :email, :password)"),
        {"name": admin.name, "email": admin.email, "password": admin.password}
    )
    db.commit()
    return {"message": "Job admin registered successfully"}




# API to fetch job admin details based on jobadmin_id
@router.get("/job_admin/{jobadmin_id}")
def get_job_admin(jobadmin_id: int, db: Session = Depends(get_db)):
    # Fetch job admin from the database using the provided ID
    job_admin = db.execute(
        text("SELECT jobadmin_id, name, email FROM job_admin WHERE jobadmin_id = :jobadmin_id"),
        {"jobadmin_id": jobadmin_id}
    ).fetchone()

    # If the job admin does not exist, return a 404 error
    if not job_admin:
        return JSONResponse(status_code=404, detail="Job Admin not found")

    # Return the job admin details as a dictionary
    return {
        "jobadmin_id": job_admin[0],
        "name": job_admin[1],
        "email": job_admin[2]
    }

@router.get("/job_admin/postedby/{jobadmin_id}", response_model=List[JobCreate])
def get_jobs_posted_by_admin(jobadmin_id: int, db: Session = Depends(get_db)):
    # Fetch jobs by jobadmin_id
    jobs = db.execute(
        text("SELECT * FROM jobs WHERE posted_by = :jobadmin_id"),
        {"jobadmin_id": jobadmin_id}
    ).fetchall()

    # Handle case where no jobs are found for the admin
    if not jobs:
        raise JSONResponse(status_code=404, detail="No jobs found for this admin")

    # Return the jobs in the expected format, handling None values
    return [
        {
            "job_id": job[0],
            "title": job[1] or "No Title Provided",  # Handle None for title
            "description": job[2] or "No Description Provided",  # Handle None for description
            "skills_required": job[3] or "No Skills Provided",  # Handle None for skills
            "experience_required": job[4] if job[4] is not None else 0,  # Handle None for experience
            "street": job[5] or "No Street Provided",  # Handle None for street
            "state": job[6] or "No State Provided",  # Handle None for state
            "country": job[7] or "No Country Provided",  # Handle None for country
            "zipcode": job[8] or "No Zipcode Provided",  # Handle None for zipcode
            "company_name": job[9] or "No Company Name Provided",  # Handle None for company name
            "salary_range": job[10] or "No Salary Range Provided",  # Handle None for salary range
            "employment_type": job[11] or "Unknown",  # Handle None for employment type
            "application_deadline": job[12] if job[12] is not None else None,  # Keep it as None for FastAPI to validate
            "bachelors_needed": job[13] if job[13] is not None else False,  # Handle None for bachelors_needed
            "masters_needed": job[14] if job[14] is not None else False,  # Handle None for masters_needed
            "valid_majors": job[15] or "No Majors Specified",  # Handle None for valid majors
            "posted_by": int(job[17]) if job[16] is not None else 0,  # Handle None for posted_by
            "created_at": job[16].strftime('%Y-%m-%d %H:%M:%S') if job[17] is not None else "No Created At Date"  # Handle None for created_at
        }
        for job in jobs
    ]

@router.get("/job_admin/match_student/{job_id}")
def match_student_to_job(job_id: int, db: Session = Depends(get_db)):
    # Fetch the job details using job_id
    job = db.execute(text("""
        SELECT title, description, skills_required, experience_required, bachelors_needed, masters_needed, valid_majors 
        FROM jobs 
        WHERE job_id = :job_id
    """), {"job_id": job_id}).fetchone()

    if not job:
        return JSONResponse(status_code=404, content="Job not found")

    title, description, skills_required, experience_required, bachelors_needed, masters_needed, valid_majors = job

    # Fetch students who match the job criteria
    # query = """
    # SELECT student_id, student_name, skills, experience, highest_education_level, major
    # FROM students
    # WHERE experience >= :experience_required
    # AND (
    #     (:bachelors_needed = 0 OR (highest_education_level = 'Bachelors' AND :bachelors_needed = 1))
    #     OR (:masters_needed = 0 OR (highest_education_level = 'Masters' AND :masters_needed = 1))
    # )
    # AND FIND_IN_SET(LOWER(major), LOWER(:valid_majors)) > 0
    # """


    query = """
    SELECT student_id, student_name, skills, experience, highest_education_level, major
    FROM students
    WHERE (
        (:bachelors_needed = 0 OR (highest_education_level = 'Bachelors' AND :bachelors_needed = 1))
        OR (:masters_needed = 0 OR (highest_education_level = 'Masters' AND :masters_needed = 1))
    )
    AND FIND_IN_SET(LOWER(major), LOWER(:valid_majors)) > 0
    """



#     query = """
#     SELECT student_id, student_name, skills, experience, highest_education_level, major
#     FROM students
#     WHERE (
#         (:bachelors_needed = 0 OR (highest_education_level = 'Bachelors' AND :bachelors_needed = 1))
#         OR (:masters_needed = 0 OR (highest_education_level = 'Masters' AND :masters_needed = 1))
# )
#     """


    students = db.execute(text(query), {
        "experience_required": experience_required,
        "bachelors_needed": bachelors_needed,
        "masters_needed": masters_needed,
        "valid_majors": valid_majors
    }).fetchall()

    if not students:
        return JSONResponse(status_code=404, content="No matching students found")

    # Using LLM to generate match scores for each student
    student_matches = []
    for student in students:
        student_id, student_name, student_skills, student_experience, highest_education_level, student_major = student

        # Create a prompt for the LLM to evaluate the student against the job
        prompt = f"""
        Job Title: {title}
        Job Description: {description}
        Required Skills: {skills_required}
        Required Experience: {experience_required} years

        Student Profile:
        Name: {student_name}
        Skills: {student_skills}
        Experience: {student_experience} years
        Based on the job description and student's profile, return a match score between 0 and 1 (just number).
        """

        response = co.generate(
            model='command-xlarge-nightly',
            prompt=prompt,
            max_tokens=100,
            temperature=0.7,
            stop_sequences=["\n"]
        )

        match_score = response.generations[0].text.strip()

        # Add the student's match score to the result
        student_matches.append({
            "student_id": student_id,
            "student_name": student_name,
            "match_score": match_score,
            "experience": student_experience,
            "highest_education_level": highest_education_level,
            "major": student_major,
            "skills": student_skills
        })

    return student_matches
