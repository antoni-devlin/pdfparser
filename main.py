import PyPDF2
import textract
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import subprocess

filename = 'Measuring_Sustainability_WMI.pdf'

pdfFileObj = open(filename, 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

num_pages = pdfReader.numPages
count = 0
text = ""

while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count += 1
    text += pageObj.extractText()

if text != "":
    text = text
else:
    text = textract.process(fileurl, method='tesseract', language='eng')

tokens = word_tokenize(text)

punctuations = ['(',')',';',':','[',']',',','.','-']

stopwords = stopwords.words('english')
custom_stopwords = ['the']
stopwords.extend(custom_stopwords)

keywords = [word for word in tokens if not word in stopwords and not word in punctuations]

keywords_lower = [x.lower() for x in keywords]

frequency = Counter(keywords_lower)

with open('pdf-output.txt' ,'w') as f:
    rows = 0
    for k,v in frequency.most_common():
        f.write( "{} = {}\n".format(k,v) )
        rows += 1
    print('Successfully wrote ' + str(rows) + ' rows to pdf-output.txt, based on an analysis of ' + filename + '.')

#Open generated file
subprocess.call(['open', '-a', 'TextEdit', 'pdf-output.txt'])
