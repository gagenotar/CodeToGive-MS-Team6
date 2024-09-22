from pyresparser import ResumeParser
import os
import json
import requests
from fastapi import HTTPException
from typing import Optional

# Function to download a PDF from a Google Drive link
def download_pdf_from_drive(drive_link: str, file_path: str):
    try:
        response = requests.get(drive_link, stream=True)
        if response.status_code == 200:
            with open(file_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
        else:
            raise HTTPException(status_code=400, detail="Failed to download the PDF.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while downloading the PDF: {str(e)}")

# Function to parse a PDF and extract resume data
def parse_pdf(file_path: str) -> dict:
    try:
        data = ResumeParser(file_path).get_extracted_data()
        return {
            'skills': data.get('skills'),
            'experience': data.get('experience'),
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while parsing the resume: {str(e)}")
