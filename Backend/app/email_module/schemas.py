from pydantic import BaseModel, EmailStr
from typing import List

class EmailRequest(BaseModel):
    subject: str
    body: str
    recipients: List[EmailStr]
    use_word_spinner: bool = False

class NotificationRequest(BaseModel):
    recruiter_email: EmailStr
    applicant: dict
