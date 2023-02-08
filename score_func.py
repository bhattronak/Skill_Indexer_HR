from Resume_scrapper import extract_skills,extract_emails,extract_phone_number,extract_education
from pdf_to_text_scrapper_function import get_resume_text as grt
import os

job_description = input('enter the JD: ')
path = input('Enter the path of the resume: ')
resume_text= grt(path) 


skills_jd = set(extract_skills(job_description))
# sklls_resume = extract_skills(resume_text)
    

    

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
    score_dict = dict(sorted(score_dict.items(), key=lambda x: x[1]))
    return score_dict
