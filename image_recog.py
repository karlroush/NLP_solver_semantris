# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 16:18:45 2020

@author: compute
"""


import pytesseract 
from PIL import Image
import time 
import requests

img = Image.open('word.png') 
pytesseract.pytesseract.tesseract_cmd ='C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'

start_time = time.time()
result = pytesseract.image_to_string(img).lower()

print(result)
print("--- %s seconds ---" % (time.time() - start_time))

url = 'https://www.dictionaryapi.com/api/v3/references/thesaurus/json/'
url= url+result+'?key=55e878d5-1948-47b2-8d77-4b5a9cfad218'
print(url)
response = requests.post(url)
r_data= response.json()

related_words= r_data[0]['meta']['syns'][0]
