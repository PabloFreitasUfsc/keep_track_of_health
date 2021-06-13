#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Pablo Freitas
# Created Date: Son June 13 12:42:00 PDT 2021
# =============================================================================
"""The Module Has Been Build for having a scrutured place of all information inside the blood. """

__author__ = "Pablo Freitas"
__copyright__ = "Copyright 2021, Keep Track of Health"
__credits__ = ["Pablo Freitas", "Diego Freitas"]
__license__ = "None"
__version__ = "1.0.0"
__maintainer__ = "Pablo Freitas"
__email__ = "pablofreitas.fn@gmail.com"
__status__ = "Prototype"

# =============================================================================
# Imports
# =============================================================================

from pathlib import Path
import pdfminer


# Load your PDF"

sample_file_path = Path(__file__).absolute().parent.joinpath("samples")
exam_test = Path(sample_file_path).joinpath("exames_test.pdf")

# #opening method will be rb
# pdf_obj = open(exam_test, "rb")

# #create reader variable that will read the pdffileobj
# pdf_reader = PyPDF2.PdfFileReader(pdf_obj)
# x = 0

# #create a variable that will select the selected number of pages
# page_obj=pdf_reader.getPage(1)

# #(x+1) because python indentation starts with 0.
# #create text variable which will store all text datafrom pdf file
# text=page_obj.extractText()

# print(text)

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO


def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = "utf-8"
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    fp = open(path, "rb")
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()

    for page in PDFPage.get_pages(
        fp,
        pagenos,
        maxpages=maxpages,
        password=password,
        caching=caching,
        check_extractable=True,
    ):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text


text = convert_pdf_to_txt(str(exam_test))


# print(text.__len__())

split_text = []
# n  = 244
# for index in range(0, len(text), n):
#     split_text.append(text[index : index + n])
step_size = 0
aux_start_line = 0
n_lines = 0
for index in range(0, len(text)):
    if text[index] == "\n":
        n_lines = n_lines + 1
        step_size = text.index(text[index])
        split_text.append(text[aux_start_line:index])
        # print(index)
        aux_start_line = aux_start_line + step_size

for element in split_text:
    print(element)
    # break
