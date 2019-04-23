
from PIL import Image 
import os 
import sys
  
img_path = sys.argv[0]
   
pdf_path = sys.argv[1]
   
image = Image.open(img_path) 
  
image.save(pdf_path,"PDF") 