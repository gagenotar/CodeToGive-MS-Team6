from models import Applicant, Recruiter

def generate_email_body(applicant: Applicant, recruiter: Recruiter = None, email_type: str = "applicant") -> str:
    if email_type == "applicant":
        return f"""
        <p>Hello {applicant.name},</p>
        <p>Thank you for your application. Please find your profile link below:</p>
        <p><a href="{applicant.profile_link}">View Profile</a></p>
        <p>We appreciate your interest and will get back to you soon.</p>
        <p>Best regards,<br>Team 6</p>
        """
    elif email_type == "recruiter":
        return f"""
        <p>Hello {recruiter.name},</p>
        <p>We have received a new application from {applicant.name}.</p>
        <p>Applicant's email: {applicant.email}</p>
        <p>Profile link: <a href="{applicant.profile_link}">View Profile</a></p>
        <p>Please review the application and proceed accordingly.</p>
        <p>Best regards,<br>Team 6</p>
        """
    else:
        raise ValueError("Invalid email type. Must be 'applicant' or 'recruiter'.")
