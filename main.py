#Author: Antoni Devlin - 2018
import PyPDF2
import textract
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import subprocess
from pathlib import Path
from datetime import datetime

for file in 


pdfname = 'Measuring_Sustainability_WMI.pdf'
pdfFileObj = open(pdfname, 'rb')
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

punctuations = ['(',')',';',':','[',']',',','.','-','&','%']

stopwords = stopwords.words('english')
custom_stopwords = ['the', r'{[0-9]+:[0-9]+}', r'\d+']
stopwords.extend(custom_stopwords)

keywords = [word for word in tokens if not word in stopwords and not word in punctuations]

keywords_lower = [x.lower() for x in keywords]

frequency = Counter(keywords_lower)



def writetofile():
    time = datetime.now().strftime("%b %d %Y %H:%M:%S")
    filename = 'OUTPUT_' + pdfname +str(time) + '.txt'
    with open(filename ,'w') as f:
        rows = 0
        for k,v in frequency.most_common():
            f.write( "{} = {}\n".format(k,v) )
            rows += 1
    print('Successfully wrote ' + str(rows) + ' rows to ' + filename + ', based on an analysis of ' + pdfname + '.')
    #Open generated file
    subprocess.call(['open', '-a', 'TextEdit', 'pdf-output.txt'])

#Run program
writetofile()
