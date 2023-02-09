import tkinter as tk
from Resume_scrapper import extract_skills,extract_emails,extract_phone_number,extract_education
from pdf_to_text_scrapper_function import get_resume_text as grt
import os

path_ = ''

def smi(path):

    ''' this function calculates a score for a person according to the
    number of matching skills (with JD)'''

    resume_text= grt(path) 
    skills_resume = extract_skills(resume_text)
    skills_resume = set(skills_resume)
    sk_temp = skills_jd - skills_resume
    score = (len(skills_jd) - len(sk_temp))/ len(skills_jd)
    phone_number = extract_phone_number(resume_text)
    return phone_number, score*100

def list_resume(path):

    '''this function returns a list of all the files in the path specified'''

    path_resumes = []
    for filename in os.listdir(path):
        if 'pdf' in filename:
            path_resumes.append(path + '/' + filename)
    return path_resumes
    
def rank_smi(path):

    '''this function returns score of all the resumes present in the directory'''

    score_dict = dict()
    paths = list_resume(path)
    for person in paths:
        phone_number, score = smi(person)
        score_dict[phone_number] = score
    # score_dict = dict(sorted(score_dict.items(), key=lambda x: x[1]))
    return score_dict



def set_job_description(job_description):
    global skills_jd
    skills_jd = set(extract_skills(job_description))

def set_path(path):
    global path_
    path_ = path

def run_analysis():
    score_dict = rank_smi(path_)
    tk.Label(root, text="Scores:").grid(row=3, column=0, pady=10)
    for i, (k, v) in enumerate(score_dict.items()):
        tk.Label(root, text=f"{k}: {v}").grid(row=4+i, column=0, pady=10)

root = tk.Tk()
root.geometry("600x500")
root.configure(bg="#E5E5E5")

tk.Label(root, text="Job Description", bg="#E5E5E5").grid(row=0, column=0, pady=10)
entry_job_description = tk.Text(root, height=10, width=80)
entry_job_description.grid(row=0, column=1, padx=10)
entry_job_description.bind("<FocusOut>", lambda args: set_job_description(entry_job_description.get("1.0", "end-1c")))

tk.Label(root, text="Path to Folder containing Resumes", bg="#E5E5E5").grid(row=1, column=0, pady=10)
entry_path = tk.Entry(root, width=80)
entry_path.grid(row=1, column=1, padx=10)
entry_path.bind("<FocusOut>", lambda args: set_path(entry_path.get()))

run_button = tk.Button(root, text="Run Analysis", command=run_analysis)
run_button.grid(row=2, column=0, pady=10)

root.mainloop()
