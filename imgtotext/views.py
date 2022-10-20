from django.shortcuts import render
from PIL import Image
import numpy as np
import pytesseract
# Author Fatai Akeem Tolani

# you have to install tesseract module too from here - https://github.com/UB-Mannheim/tesseract/wiki
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Path to tesseract.exe
)
def ocr(request):
    
    if request.method =='POST':
        image = request.FILES['filename']
        image = Image.open(image)
        img = np.array(image.convert("L"))
            # with Image.open(request.FILES['filename']) as image:
            #     sharpenImage = image.filter(ImageFilter.SHARPEN)
        text = pytesseract.image_to_string(img)
        
        return render(request, 'base.html', {'text':text})


        
    return render(request, 'base.html')