"""
读取PDF文件

Version: 0.1
Author: 骆昊
Date: 2018-03-26
"""

from PyPDF2 import PdfFileReader

with open('./res/Python课程大纲.pdf', 'rb') as f:
    reader = PdfFileReader(f, strict=False)
    print(reader.numPages)
    if reader.isEncrypted:
        reader.decrypt('')
    current_page = reader.getPage(5)
    print(current_page)
    print(current_page.extractText())
