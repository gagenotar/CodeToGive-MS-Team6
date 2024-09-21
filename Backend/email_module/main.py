from fastapi import FastAPI, HTTPException
from models import Applicant, Recruiter
from schemas import EmailRequest, NotificationRequest
from services.email_service import EmailService
from utils.email_templates import generate_email_body

app = FastAPI()
email_service = EmailService()

@app.post("/send-email/")
def send_email(email_request: EmailRequest, email_type: str = "generic"):
    if email_type == "applicant":
        applicant = Applicant(**email_request.body)
        body = generate_email_body(applicant, email_type="applicant")
    elif email_type == "recruiter":
        applicant = Applicant(**email_request.body)
        recruiter = Recruiter(name="Recruiter Name", email="recruiter@example.com")  # Example recruiter data
        body = generate_email_body(applicant, recruiter, email_type="recruiter")
    else:
        body = email_request.body

    response = email_service.send_email(
        email_request.subject,
        body,
        email_request.recipients,
        email_request.use_word_spinner
    )
    if response:
        return {"message": "Email sent successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to send email")

@app.post("/notify-recruiter/")
def notify_recruiter(notification_request: NotificationRequest):
    applicant = Applicant(**notification_request.applicant)
    recruiter = Recruiter(name="Recruiter Name", email=notification_request.recruiter_email)
    body = generate_email_body(applicant, recruiter, email_type="recruiter")
    subject = f"New application from {applicant.name}"
    response = email_service.send_email(
        subject,
        body,
        [notification_request.recruiter_email]
    )
    if response:
        return {"message": "Notification sent successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to send notification")
