import json
import os
import requests as req


from dotenv import load_dotenv


load_dotenv()

def send_mail(email, message):
    """Function to send email"""
    body = {
        "email": email,
        "message": message
    }
    url = os.getenv("EMAIL_API")
    try:
        response = req.post(url, json=body, timeout=10)
        status = json.loads(response.text)
    except Exception:
        return False
    
    return status["sent"]
    