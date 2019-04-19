import PyPDF2
import docx
import os
import sys
a=[]
PDFfilename = sys.argv[0] #filename of your PDF/directory where your PDF is stored
OutputLocation = sys.argv[1]
pdfFileObj=open(PDFfilename,'rb')
pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
for i in range(0,pdfReader.numPages):
    pageobj=pdfReader.getPage(i)
    a.append(pageobj.extractText())
pdfFileObj.close()
doc = docx.Document()

for i in range(len(a)):
    doc.add_paragraph(a[i])
    doc.add_page_break()
doc.save(OutputLocation)
