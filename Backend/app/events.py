from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import *
from sqlalchemy import text  # <-- Add this import


router = APIRouter()



# Endpoint to list all events with full fields
@router.get("/events", response_model=List[EventResponse])
def get_events(db: Session = Depends(get_db)):
    # Query to fetch all fields from the events table
    events = db.execute(text("SELECT event_id, event_name, event_type, description, sponsor_id FROM events")).fetchall()

    if not events:
        raise HTTPException(status_code=404, detail="No events found")

    # Return all events in structured format
    return [
        {
            "event_id": event.event_id,
            "event_name": event.event_name,
            "event_type": event.event_type,
            "description": event.description,
            "sponsor_id": event.sponsor_id
        }
        for event in events
    ]
