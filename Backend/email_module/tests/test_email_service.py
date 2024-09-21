import pytest
from services.email_service import EmailService

@pytest.fixture
def email_service():
    return EmailService()

def test_send_email_success(email_service):
    response = email_service.send_email(
        subject="Test Email",
        body="<p>This is a test email.</p>",
        recipients=["rodrigo.vena.g@gmail.com"]
    )
    assert response is not None
    assert 'id' in response  # message ID if successful

def test_send_email_failure(email_service, monkeypatch):
    # force failure
    def mock_build(*args, **kwargs):
        raise Exception("Invalid credentials")

    monkeypatch.setattr(email_service, 'service', mock_build)
    
    response = email_service.send_email(
        subject="Test Email",
        body="<p>This is a test email.</p>",
        recipients=["rodrigo.vena.g@gmail.com"]
    )
    assert response is None
