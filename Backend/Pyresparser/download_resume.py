import requests
from datetime import datetime


punctuations = [' ', ':', '.']

def download_resume(url: str, file_name=None):
    if not file_name:
        file_name = file_name or f"{datetime.now()}
        for p in punctuations:
            file_name = file_name.replace(p, '-')
        file_name += ".pdf"
    try:
        with open(f"Data/test_resume/{file_name}", "wb") as file:
            file.write(requests.get(url, timeout=10).content)
    except:
        return False
    return True

# Function to download a PDF from a Google Drive link
def download_pdf_from_drive(drive_link: str, file_path: str):
    try:
        response = requests.get(drive_link, timeout=10)
        if response.status_code == 200:
            with open(file_path, 'wb') as file:
                file.write(response.content)
        else:
            raise HTTPException(status_code=400, detail="Failed to download the PDF.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while downloading the PDF: {str(e)}")

# download_pdf_from_drive("https://drive.google.com/file/d/1NYZglzd10wyNYlzkpF2k6uA05HYlJdIw/view?usp=drive_link", "Data/test_resume/hello.pdf")