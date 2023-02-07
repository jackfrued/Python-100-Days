import re

import PyPDF2

with open('Python_Tricks_encrypted.pdf', 'rb') as pdf_file_stream:
    reader = PyPDF2.PdfFileReader(pdf_file_stream)
    with open('dictionary.txt', 'r') as txt_file_stream:
        file_iter = iter(lambda: txt_file_stream.readline(), '')
        for word in file_iter:
            word = re.sub(r'\s', '', word)
            if reader.decrypt(word):
                print(word)
                break

