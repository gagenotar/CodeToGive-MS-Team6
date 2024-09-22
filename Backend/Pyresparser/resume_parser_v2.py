from pyresparser import ResumeParser
import os
import json
import requests
from fastapi import HTTPException
from typing import Optional
import re

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
    

# temp_pdf_path = 'temp_resume_test.pdf'
# resume_link = 'https://drive.google.com/file/d/1gjYozBUTNN_X9N9LfCy251-QFkKrkjeA/view?usp=drive_link'

# download_pdf_from_drive(resume_link, temp_pdf_path)


def get_drive_file_id(drive_link: str) -> str:
    """
    Extract the file ID from the Google Drive shareable link.
    """
    match = re.search(r'/d/([a-zA-Z0-9_-]+)', drive_link)
    if match:
        return match.group(1)
    else:
        raise ValueError("Invalid Google Drive link format. Could not extract file ID.")

def download_pdf_from_drive2(drive_link: str, file_path: str):
    file_id = get_drive_file_id(drive_link)
    download_url = f"https://drive.google.com/uc?id={file_id}&export=download"

    # Ensure the directory exists
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory) and directory:
        os.makedirs(directory)

    try:
        response = requests.get(download_url, stream=True)
        if response.status_code == 200:
            with open(file_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            print("File downloaded successfully.")
        else:
            raise RuntimeError("Failed to download the PDF. Status code: " + str(response.status_code))
    except Exception as e:
        print(f"An error occurred while downloading the PDF: {str(e)}")

# Example usage
drive_link = "https://drive.google.com/file/d/1gjYozBUTNN_X9N9LfCy251-QFkKrkjeA/view?usp=drive_link"
temp_pdf_path = "temp_resume_test.pdf"
download_pdf_from_drive2(drive_link, temp_pdf_path)