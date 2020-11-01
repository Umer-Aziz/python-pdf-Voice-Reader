# pip install pyttsx3
import pyttsx3
# pip install PyPDF2
import PyPDF2
# opening the specific pdf file.and rb mean read binary.
b = open("essay.pdf", "rb")
#Read The pdf file.
pdf = PyPDF2.PdfFileReader(b)
#check the num of pages in pdf file.
numofpages = pdf.numPages
print(numofpages)
voice = pyttsx3.init()
#read all the pages from 0 to last page.
for num in range(0, numofpages):
    #Reading start from 0 page.
    page = pdf.getPage(0)
    #extract only text from pdf.
    text = page.extractText()
    #output of text
    voice.say(text)
    voice.runAndWait()