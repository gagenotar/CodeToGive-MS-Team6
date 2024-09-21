from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import AdminRegisterModel, AdminLoginModel
from app.database import get_db
from fastapi.responses import JSONResponse
from sqlalchemy import text  # <-- Add this import

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
