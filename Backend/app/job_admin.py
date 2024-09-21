from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import AdminRegisterModel, AdminLoginModel , JobCreate
from app.database import get_db
from fastapi.responses import JSONResponse
from sqlalchemy import text  # <-- Add this import
from typing import List, Optional




router = APIRouter()

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


router.get("/job_admin/postedby/{jobadmin_id}", response_model=List[JobCreate])
def get_jobs_posted_by_admin(jobadmin_id: int, db: Session = Depends(get_db)):
    # Query the jobs table for jobs posted by the specific jobadmin

    print("ccccccccc")
    jobs = db.execute(text("""
        SELECT * FROM jobs 
        WHERE posted_by = :jobadmin_id
    """), {"jobadmin_id": jobadmin_id}).fetchall()

    # Check if any jobs were found
    if not jobs:
        return JSONResponse(status_code=404, detail="No jobs found for this job admin")

    # Return the job details
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
            "posted_by": job[16],
            "created_at": job[17]  # Add posted timestamp
        }
        for job in jobs
    ]
