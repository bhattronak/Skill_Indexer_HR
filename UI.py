import tkinter as tk
from tkinter import filedialog

# importing the functions created locally
from Resume_scrapper import extract_skills,extract_emails,extract_phone_number,extract_education
from pdf_to_text_scrapper_function import get_resume_text as grt
# from UI import browse_file as path

def browse_file():
    file_path = filedialog.askopenfilename(initialdir = "/", title = "Select a file", filetypes = (("PDF Files", "*.pdf"), ("Text Files", "*.txt"), ("all files", "*.*")))
    return file_path

def process_file(file_path):
    resume_text= grt(file_path) 
    # print('Phone Number of candidate is',extract_phone_number(resume_text))
    # print('Email of candidate is',extract_emails(resume_text))
    # print('Education of candidate is',extract_education(resume_text))
    # print('Matching skills of candidate are',extract_skills(resume_text))
    return extract_skills(resume_text)

def display_output(output):
    output_label.config(text=output)

root = tk.Tk()
root.title("File Processing UI")

browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack()

output_label = tk.Label(root, text="")
output_label.pack()

root.mainloop()
