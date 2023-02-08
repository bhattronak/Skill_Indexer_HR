import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from Resume_scrapper import extract_skills, extract_emails, extract_phone_number, extract_education
from pdf_to_text_scrapper_function import get_resume_text as grt
import os

root = tk.Tk()
root.title("Resume Sorter")

job_description = ""
path = ""
skills_jd = set()

def browse_folder():
    global path
    path = filedialog.askdirectory()

def get_rank():
    # set_job_description()
    global job_description, path
    if not job_description:
        messagebox.showerror("Error", "Please enter the Job Description")
    elif not path:
        messagebox.showerror("Error", "Please browse the folder containing resumes")
    else:
        result = rank_smi(path)
        messagebox.showinfo("Result", result)

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
    score_dict = dict(sorted(score_dict.items(), key=lambda x: x[1]))
    return score_dict

# Job Description Input
tk.Label(root, text="Job Description").grid(row=0, column=0, pady=10)
entry_job_description = tk.Entry(root, width=80)
entry_job_description.grid(row=0, column=1, padx=10)
entry_job_description.bind("<FocusOut>", lambda args: set_job_description(entry_job_description.get()))

def set_job_description(value):
    global job_description
    job_description = value
    skills_jd = set(extract_skills(value))

# Browse Folder Button
browse_folder_button = tk.Button(root, text="Browse", command=browse_folder)
browse_folder_button.grid(row=1, column=0, pady=10)

# Get Rank Button
get_rank_button = tk.Button(root, text="Get Rank", command=get_rank)
get_rank_button.grid(row=1, column=1, padx=10)

root.mainloop()
