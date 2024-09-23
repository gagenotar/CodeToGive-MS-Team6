import requests
from ..models import Applicant, Recruiter
from ..schemas import EmailRequest
from ..utils.email_templates import generate_email_body

BASE_URL = "http://127.0.0.1:8000"

def test_send_email():
    url = f"{BASE_URL}/send-email/"
    payload = {
        "subject": "Test Email",
        "body": "<p>This is a test email for the endpoint send-email.</p>",
        "recipients": ["team6codetogive@gmail.com"],
        "use_word_spinner": False
    }
    response = requests.post(url, json=payload)
    print(response.json())
    assert response.status_code == 200
    assert response.json() == {"message": "Email sent successfully"}

def test_notify_applicant():
    url = f"{BASE_URL}/send-email/"
    applicant = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "profile_link": "http://example.com/profile/johndoe"
    }
    email_request = EmailRequest(
        subject = "Application Received",
        body = generate_email_body(Applicant(**applicant), email_type="applicant"),
        recipients = ["team6codetogive@gmail.com"],
        use_word_spinner = False
    ).model_dump()
    response = requests.post(url, json=email_request)
    print(response.json())
    assert response.status_code == 200
    assert response.json() == {"message": "Email sent successfully"}

def test_notify_recruiter():
    url = f"{BASE_URL}/notify-recruiter/"
    applicant = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "profile_link": "http://example.com/profile/johndoe"
    }
    payload = {
        "recruiter_email": "team6codetogive@gmail.com",
        "applicant": applicant
    }
    response = requests.post(url, json=payload)
    print(response.json())
    assert response.status_code == 200
    assert response.json() == {"message": "Notification sent successfully"}

def test_applicant_interest():
    url = f"{BASE_URL}/applicant-interest/"
    applicant = {
        "name": "John Doe",
        "email": "team6codetogive@gmail.com",
        "profile_link": "http://example.com/profile/johndoe"
    }
    recruiter = {
        "name": "Recruiter Name",
        "email": "team6codetogive@gmail.com"
    }
    payload = {
        "applicant": applicant,
        "recruiter": recruiter
    }
    response = requests.post(url, json=payload)
    print(response.json())
    assert response.status_code == 200
    assert response.json() == {"message": "Interest email sent successfully"}

def test_recruiter_interest():
    url = f"{BASE_URL}/recruiter-interest/"
    applicant = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "profile_link": "http://example.com/profile/johndoe"
    }
    recruiter = {
        "name": "Recruiter Name",
        "email": "team6codetogive@gmail.com"
    }
    payload = {
        "applicant": applicant,
        "recruiter": recruiter
    }
    response = requests.post(url, json=payload)
    print(response.json())
    assert response.status_code == 200
    assert response.json() == {"message": "Interest email sent successfully"}
