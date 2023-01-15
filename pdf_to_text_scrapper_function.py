import PyPDF2 as pp
from PyPDF2 import PdfReader

def get_resume_text(path):
    a=pp.PdfReader(path)
    # print(a.metadata) # Meta Data
    # print(len(a.pages)) # To get no of pages
    #print(a.pages[1]) # Return many objects
    #print(a.pages[i].extract_text) #1 is page number printed
    resume_text=''
    for i in range(0,len(a.pages)):   
        resume_text+=a.pages[i].extract_text()

    with open('Resume_text.txt','w',encoding='UTF-8') as f:
        f.write(resume_text)
    return resume_text
