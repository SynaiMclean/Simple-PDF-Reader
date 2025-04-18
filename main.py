import PyPDF2
import pyttsx3
from tkinter.filedialog import *

#Have user open the PDF file
book = askopenfilename()

#Allow our reader to read that specific file.
pdfreader = PyPDF2.PdfReader(book)

#Using len() to get the number of pages
pages = len(pdfreader.pages)

#Loop the process of extract text and have the reader go over ever page
for num in range(0, pages):
    page = pdfreader.pages[num]
    text = page.extract_text()
    #Create our reader and setting rate to read text
    player = pyttsx3.init()
    rate = player.setProperty('rate', 170)
    player.say(text)
    player.runAndWait()

