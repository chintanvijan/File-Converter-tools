import PyPDF2
import xlsxwriter
import sys
PDFfilename = sys.argv[0] #filename of your PDF/directory where your PDF is stored

pfr = PyPDF2.PdfFileReader(open(PDFfilename, "rb")) #PdfFileReader object

pg4 = pfr.getPage(0) #extract pg 127
txt=pg4.extractText()
li = txt.split('\n')
print(li)
#writer = PyPDF2.PdfFileWriter() #create PdfFileWriter object
#add pages
#writer.addPage(pg4)
#print(writer)
workbook = xlsxwriter.Workbook(sys.argv[1]) 
  
# The workbook object is then used to add new  
# worksheet via the add_worksheet() method. 
worksheet = workbook.add_worksheet() 
  
# Use the worksheet object to write 
# data via the write() method.
for i in range(len(li)): 
	worksheet.write('A'+str(i),li[i])  
  
# Finally, close the Excel file 
# via the close() method. 
workbook.close() 