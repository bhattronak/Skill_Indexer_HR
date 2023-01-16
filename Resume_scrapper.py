import docx2txt
import nltk
from pdf_to_text_scrapper_function import get_resume_text as grt

path = input('Enter the path of the resume: ')
resume_text= grt(path)

# To Get Skills of Resume! Better your SKILL_DB, Better the results
nltk.download('stopwords')
# you may read the database from a pdf file or some other database
SKILLS_DB = ['C','C++','Java',
    'machine learning',
    'data science',
    'python',
    'word',
    'excel',
    'English'
]
def extract_skills(input_text):
    stop_words = set(nltk.corpus.stopwords.words('english'))
    word_tokens = nltk.tokenize.word_tokenize(input_text)
 
    # remove the stop words
    filtered_tokens = [w for w in word_tokens if w not in stop_words]
 
    # remove the punctuation
    filtered_tokens = [w for w in word_tokens if w.isalpha()]
 
    # generate bigrams and trigrams (such as artificial intelligence)
    bigrams_trigrams = list(map(' '.join, nltk.everygrams(filtered_tokens, 2, 3)))
 
    # we create a set to keep the results in.
    found_skills = set()
 
    # we search for each token in our skills database
    for token in filtered_tokens:
        if token.lower() in SKILLS_DB:
            found_skills.add(token)
 
    # we search for each bigram and trigram in our skills database
    for ngram in bigrams_trigrams:
        if ngram.lower() in SKILLS_DB:
            found_skills.add(ngram)
 
    return found_skills

################################################################################################

# Phone Number Extractor


import re
import subprocess  # noqa: S404
 
PHONE_REG = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]')
 
def doc_to_text_catdoc(file_path):
    try:
        process = subprocess.Popen(  # noqa: S607,S603
            ['catdoc', '-w', file_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
        )
    except (
        FileNotFoundError,
        ValueError,
        subprocess.TimeoutExpired,
        subprocess.SubprocessError,
    ) as err:
        return (None, str(err))
    else:
        stdout, stderr = process.communicate()
 
    return (stdout.strip(), stderr.strip())
 
 
def extract_phone_number(resume_text):
    phone = re.findall(PHONE_REG, resume_text)
 
    if phone:
        number = ''.join(phone[0])
 
        if resume_text.find(number) >= 0 and len(number) <= 16:
            return number
    return None

################################################################################################

# Email Extractor

import re
 
from pdfminer.high_level import extract_text
 
EMAIL_REG = re.compile(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+')
 
 
def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)
 
 
def extract_emails(resume_text):
    return re.findall(EMAIL_REG, resume_text)
 
################################################################################################

# Skills Extractor

import docx2txt
import nltk
 
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
 
 
RESERVED_WORDS = ['University',
    'school',
    'college',
    'univers',
    'academy',
    'faculty',
    'institute',
    'faculdades',
    'Schola',
    'schule',
    'lise',
    'lyceum',
    'lycee',
    'polytechnic',
    'kolej',
    'ünivers',
    'okul',
]
 
 
def extract_education(input_text):
    organizations = []
 
    # first get all the organization names using nltk
    for sent in nltk.sent_tokenize(input_text):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk, 'label') and chunk.label() == 'ORGANIZATION':
                organizations.append(' '.join(c[0] for c in chunk.leaves()))
 
    # we search for each bigram and trigram for reserved words
    # (college, university etc...)
    education = set()
    for org in organizations:
        for word in RESERVED_WORDS:
            if org.lower().find(word) >= 0:
                education.add(org)
 
    return education

################################################################################################

print('Phone Number of candidate is',extract_phone_number(resume_text))
print('Email of candidate is',extract_emails(resume_text))
print('Education of candidate is',extract_education(resume_text))
print('Matching skills of candidate are',extract_skills(resume_text))


