import pyttsx3
import PyPDF2

# Insert the name of your PDF file
# `PdfFileReader` reads the object that holds the path of the PDF file
# `rb` means read binary
pdfreader = PyPDF2.PdfReader(open('resume.pdf', 'rb'))
speaker = pyttsx3.init()

for page_num in range(len(pdfreader.pages)):
    text = pdfreader.getPage(page_num).extractText()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)

# Name the MP3 file whatever you like
speaker.save_to_file(clean_text, 'read.mp3')
speaker.runAndWait()

speaker.stop()