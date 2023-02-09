import tkinter as tk
from tkinter import filedialog
import os
from Resume_scrapper import extract_skills, extract_phone_number
from pdf_to_text_scrapper_function import get_resume_text as grt

def smi(path):
    resume_text = grt(path)
    skills_resume = extract_skills(resume_text)
    skills_resume = set(skills_resume)
    sk_temp = skills_jd - skills_resume
    score = (len(skills_jd) - len(sk_temp)) / len(skills_jd)
    phone_number = extract_phone_number(resume_text)
    return phone_number, score * 100

def list_resume(path):
    path_resumes = []
    for filename in os.listdir(path):
        if 'pdf' in filename:
            path_resumes.append(path + '/' + filename)
    return path_resumes

def rank_smi(path):
    score_dict = dict()
    paths = list_resume(path)
    for person in paths:
        phone_number, score = smi(person)
        score_dict[phone_number] = score
    score_dict = dict(sorted(score_dict.items(), key=lambda x: x[1]))
    return score_dict

class ResumeRankerApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Resume Ranker")
        self.geometry("500x500")
        self.resizable(False, False)

        self.job_description_label = tk.Label(self, text="Enter Job Description:")
        self.job_description_label.pack()
        self.job_description_entry = tk.Entry(self)
        self.job_description_entry.pack()

        self.resume_directory_label = tk.Label(self, text="Enter Resume Directory:")
        self.resume_directory_label.pack()
        self.resume_directory_entry = tk.Entry(self)
        self.resume_directory_entry.pack()
        self.browse_button = tk.Button(self, text="Browse", command=self.browse)
        self.browse_button.pack()

        self.rank_button = tk.Button(self, text="Rank", command=self.rank)
        self.rank_button.pack()

        self.results_label = tk.Label(self, text="Results:")
        self.results_label.pack()
        self.results_text = tk.Text(self, height=20, width=50)
        self.results_text.pack()

    def browse(self):
        directory = filedialog.askdirectory()
        self.resume_directory_entry.delete(0, tk.END)
        self.resume_directory_entry.insert(0, directory)
