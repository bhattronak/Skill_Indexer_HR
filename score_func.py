from Resume_scrapper import extract_skills,extract_emails,extract_phone_number,extract_education
from pdf_to_text_scrapper_function import get_resume_text as grt
import os
import nltk

# def smi(path, JD):

#     ''' this function calculates a score for a person according to the
#     number of matching skills (with JD)'''

#     resume_text= grt(path) 
#     skills_resume = extract_skills(resume_text)
#     skills_resume = set(skills_resume)
#     skills_jd = extract_skills(JD)
#     skills_jd = set(skills_jd)    
#     sk_temp = skills_jd - skills_resume
#     score = (len(skills_jd) - len(sk_temp))/ len(skills_jd)
#     phone_number = extract_phone_number(resume_text)
#     return phone_number, score*100

def smi(path, JD):

    ''' this function calculates a score for a person according to the
    number of matching skills (with JD)'''

    words1 = nltk.word_tokenize(JD)
    resume_text= grt(path) 
    words2 = nltk.word_tokenize(resume_text)

    stopwords = nltk.corpus.stopwords.words('english')
    words1 = [w.lower() for w in words1 if w.lower() if w.isalpha() and w not in stopwords]
    words2 = [w.lower() for w in words2 if w.lower() if w.isalpha() and w not in stopwords]

    bigrams1 = set(nltk.bigrams(words1))
    bigrams2 = set(nltk.bigrams(words2))
    trigrams1 = set(nltk.trigrams(words1))
    trigrams2 = set(nltk.trigrams(words2))

    common_bigrams = bigrams1.intersection(bigrams2)
    common_trigrams = trigrams1.intersection(trigrams2)

    num_common_bigrams = len(common_bigrams)
    num_common_trigrams = len(common_trigrams)

    skills_resume = extract_skills(resume_text)
    skills_resume = set(skills_resume)
    skills_jd = extract_skills(JD)
    skills_jd = set(skills_jd)    
    sk_temp = skills_jd - skills_resume
    score = 2*len(sk_temp) + num_common_bigrams + num_common_trigrams
    # phone_number = extract_phone_number(resume_text)
    base_name = os.path.basename(path)
    file_name, extension = os.path.splitext(base_name)
    # return phone_number, score
    return file_name, score


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
        file_name, score = smi(person, JD)
        score_dict[file_name] = score
    score_dict = {k: v for k, v in sorted(score_dict.items(), key=lambda item: item[1], reverse=True)}
    return score_dict

