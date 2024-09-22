import requests as req
from datetime import datetime


punctuations = [' ', ':', '.']

def download_resume(url, ext="pdf", file_name=None):
    file_name = file_name or str(datetime.now())
    for p in punctuations:
        time = time.replace(p, '-')

    try:
        with open(f"resumes/{file_name}.{ext}", "wb") as file:
            file.write(req.get(url, timeout=10).content)
    except:
        return False

    return True
