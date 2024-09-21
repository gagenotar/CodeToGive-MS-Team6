import os
import base64
from email.mime.text import MIMEText
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from config import config
from utils.unsubscribe_link import generate_unsubscribe_link
from services.word_spinner import WordSpinner

class EmailService:
    def __init__(self):
        self.creds = None
        if os.path.exists('token.json'):
            self.creds = Credentials.from_authorized_user_file('token.json', config.SCOPES)
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(config.CLIENT_SECRET_FILE, config.SCOPES)
                self.creds = flow.run_local_server(port=0)
            with open('token.json', 'w') as token:
                token.write(self.creds.to_json())
        self.service = build('gmail', 'v1', credentials=self.creds)

    def send_email(self, subject, body, recipients, use_word_spinner=False):
        if use_word_spinner:
            body = WordSpinner.spin(body)
        
        body += generate_unsubscribe_link()
        
        message = MIMEText(body, 'html')
        message['to'] = ', '.join(recipients)
        message['from'] = config.EMAIL_FROM
        message['subject'] = subject

        raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
        message = {'raw': raw}

        try:
            message = (self.service.users().messages().send(userId="me", body=message).execute())
            return message
        except Exception as e:
            print(f"Error sending email: {e}")
            return None
