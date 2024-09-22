from .database import engine, Base  # Use relative imports for app modules
from app.students import router as students_router
from app.jobs import router as jobs_router
from app.job_admin import router as job_admin_router
from app.events import router as events_router

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

# Create FastAPI instance
app = FastAPI()

# Initialize the database (create tables if not exist)
Base.metadata.create_all(bind=engine)

# Include all routers
app.include_router(students_router)
app.include_router(jobs_router)
app.include_router(job_admin_router)
app.include_router(events_router)
