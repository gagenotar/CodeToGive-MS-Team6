from pydantic import BaseModel, EmailStr

class Applicant(BaseModel):
    name: str
    email: EmailStr
    profile_link: str

class Recruiter(BaseModel):
    name: str
    email: EmailStr

