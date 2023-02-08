from Resume_scrapper import extract_skills,extract_emails,extract_phone_number,extract_education
from pdf_to_text_scrapper_function import get_resume_text as grt
# from UI import browse_file as path
# path = input('Enter the path of the resume: ')
resume_text= grt(path) 

print('Phone Number of candidate is',extract_phone_number(resume_text))
print('Email of candidate is',extract_emails(resume_text))
print('Education of candidate is',extract_education(resume_text))
print('Matching skills of candidate are',extract_skills(resume_text))
