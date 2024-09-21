from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import JobCreate
from app.database import get_db
from fastapi.responses import JSONResponse
from datetime import datetime
import cohere
import os
from typing import List, Optional
from sqlalchemy import text  # <-- Add this import


# Load environment variables
from dotenv import load_dotenv
load_dotenv()


from sqlalchemy.orm import Session
from app.models import Student, Job  # Import models from models.py
from app.database import get_db  # Import DB session from database.py



router = APIRouter()

# Create a job posting
@router.post("/jobs")
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    result = db.execute(
        text("INSERT INTO jobs (title, description, skills_required, experience_required, street, state, country, zipcode, company_name, salary_range, employment_type, application_deadline, bachelors_needed, masters_needed, valid_majors, posted_by) "
             "VALUES (:title, :description, :skills_required, :experience_required, :street, :state, :country, :zipcode, :company_name, :salary_range, :employment_type, :application_deadline, :bachelors_needed, :masters_needed, :valid_majors, :posted_by)"),
        {"title": job.title, "description": job.description, "skills_required": job.skills_required,
         "experience_required": job.experience_required, "street": job.street, "state": job.state,
         "country": job.country, "zipcode": job.zipcode, "company_name": job.company_name, 
         "salary_range": job.salary_range, "employment_type": job.employment_type,
         "application_deadline": job.application_deadline, "bachelors_needed": job.bachelors_needed,
         "masters_needed": job.masters_needed, "valid_majors": job.valid_majors,
         "posted_by": job.posted_by  # Insert the posted_by value provided in the request
        }
    )
    db.commit()

    new_job_id = result.lastrowid
    return {"message": "Job posting successful", "job_id": new_job_id}

# Get all jobs
# GET endpoint to retrieve all jobs
@router.get("/jobs", response_model=List[JobCreate])
def get_jobs(db: Session = Depends(get_db)):
    jobs = db.execute(text("SELECT * FROM jobs")).fetchall()

    print(jobs)

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
            "valid_majors": job[15],
            "posted_at":job[16],
            "posted_by": job[17]
        }
        for job in jobs
    ]

# Fetch a single job by its job_id
@router.get("/jobs/{job_id}")
def get_job(job_id: int, db: Session = Depends(get_db)):
    job = db.execute(text("SELECT * FROM jobs WHERE job_id = :job_id order by created_at desc"  ), {"job_id": job_id}).fetchone()
    if not job:
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
        "posted_at":job[16],
        "valid_majors": job[15],
        "posted_by": job[17]

    }

# Match job to user profile
