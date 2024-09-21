from pyresparser import ResumeParser
import os
import json

def find_path(folder_name):
    curr_dir = os.getcwd()
    while True:
        if folder_name in os.listdir(curr_dir):
            return os.path.join(curr_dir, folder_name)
        else:
            parent_dir = os.path.dirname(curr_dir)
            if parent_dir == "/":
                break
            curr_dir = parent_dir
    raise ValueError(f"Folder '{folder_name}' not found.")



cwd = find_path('Backend')
resume_folder = os.path.join(cwd, 'Pyresparser', 'Data', 'Resumes\\')

for resume_file in os.listdir(resume_folder) :
    resume_path = os.path.join(resume_folder, resume_file)

    if resume_path.endswith(('.pdf')):
        try:
            data = ResumeParser(resume_path).get_extracted_data()
            data_dict = {
                'name' : data.get('name'),
                'skills' : data.get('skills'),
                'experience' : data.get('experience'),
                'degree' : data.get('degree'),
                'total_experience' : data.get('total_experience')
            }

        except Exception as e:
            print(f"Error ocurred while parsing resume: {str(e)}")

output_file = os.path.join(cwd, 'Pyresparser', 'processed_resume.json')

with open(output_file, 'w', encoding='utf-8') as json_file :
    json.dump(data_dict, json_file, ensure_ascii=False, indent=4)

print(f'Data has been saved to {output_file}')