from Resume_scrapper import extract_skills,extract_emails,extract_phone_number,extract_education
from pdf_to_text_scrapper_function import get_resume_text as grt
import os

def smi(path, JD):

    ''' this function calculates a score for a person according to the
    number of matching skills (with JD)'''

    resume_text= grt(path) 
    skills_resume = extract_skills(resume_text)
    skills_resume = set(skills_resume)
    skills_jd = extract_skills(JD)
    skills_jd = set(skills_jd)    
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
    
def rank_smi(path, JD):

    '''this function returns score of all the resumes present in the directory'''

    score_dict = {}
    paths = list_resume(path)
    for person in paths:
        phone_number, score = smi(person, JD)
        score_dict[phone_number] = score
    score_dict = {k: v for k, v in sorted(score_dict.items(), key=lambda item: item[1], reverse=True)}
    return score_dict

