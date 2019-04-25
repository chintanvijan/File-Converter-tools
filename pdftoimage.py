import sys
from pdf2image import convert_from_path
pages = convert_from_path(sys.argv[0], 500)
for page in pages:
    page.save('out.jpg', 'JPEG')