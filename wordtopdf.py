import sys
import os
import comtypes.client

wdFormatPDF = 17

in_file = sys.argv[0]
out_file = sys.argv[1]

word = comtypes.client.CreateObject('Word.Application')
doc = word.Documents.Open(in_file)
doc.SaveAs(out_file, FileFormat=wdFormatPDF)
doc.Close()
word.Quit()