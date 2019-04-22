import win32com.client  # https://github.com/mhammond/pywin32
import sys
in_file = sys.argv[0]
out_file = sys.argv[1]
excel = win32com.client.Dispatch('Excel.Application')
excel.Visible = False
doc = excel.WorkBooks.Open(in_file, ReadOnly=True)

#This code let me select multiple Sheets into a single PDF, however we went for 1 sheet per PDF file.
# sheets_to_convert = [1, 2, 3]
# doc.WorkSheets(sheets_to_convert).Select()
# doc.ActiveSheets.ExportAsFixedFormat(0, out_file)

for x in range(100):
    try:
        sheet = doc.Worksheets[x]
        sheet.PageSetup.PrintGridLines = 1

        # 57 is PDF format even though it isn't listed as such in Microsofts documentation.
        sheet.SaveAs('{}_{}'.format(out_file, x), FileFormat=57)
    except:
        break

doc.Close(SaveChanges=False)
excel.Quit()