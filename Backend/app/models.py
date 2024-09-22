from sqlalchemy import Column, Integer, String, Text, Date, TIMESTAMP, Boolean, ForeignKey
from pydantic import BaseModel
from sqlalchemy.ext.declarative import declarative_base

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



Base = declarative_base()

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
    resume_link = Column(String(255)) # New column for resume link

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
    posted_by = Column(Integer, ForeignKey('job_admin.jobadmin_id'), nullable=False)  # References job_admin

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
    resume_link: Optional[str] = None

# Job creation model (now using `datetime.date` instead of SQLAlchemy's `Date`)
class JobCreate(BaseModel):
    #job_id: str
    title: str
    description: str
    skills_required: Optional[str]
    experience_required: Optional[int]
    street: str
    state: str
    country: str
    zipcode: str
    company_name: str
    salary_range: str
    employment_type: str
    application_deadline: Optional[date]  # <-- Use Python's `datetime.date`
    bachelors_needed: Optional[bool]
    masters_needed: Optional[bool]
    valid_majors: str
    #posted_by: int  # Add this field to track who posted the job
    posted_by: Optional[int]
    posted_at: Optional[datetime]
    

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
    resume_link: Optional[str] = None



# Pydantic models for login
class LoginModel(BaseModel):
    email: str
    password: str



# Pydantic model for login request
class AdminLoginModel(BaseModel):
    email: str
    password: str


# Pydantic model for job admin registration
class AdminRegisterModel(BaseModel):
    name: str
    email: str
    password: str
