# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 17:01:41 2020

@author: compute
"""
import pytesseract 
from PIL import Image, ImageGrab
import pyautogui
import time 
import requests
import cv2
from gensim.models import KeyedVectors, Word2Vec

def getCoords():
    print("move mouse to location")
    time.sleep(2)
    currentMouseX, currentMouseY = pyautogui.position()
    print('Mouse [x,y]=', [currentMouseX, currentMouseY])
    
def get_game():
    image =  pyautogui.screenshot(region=(1200,97,1450-969,872-97))
    image.save('./images/raw_capture.png')
    
def isolate_word(raw_image):
    # FIND THE TARGET WORD
    img_rgb = cv2.imread(raw_image)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('./images/arcade_template.png',0)
    w, h = template.shape[::-1]
    
    res = cv2.matchTemplate(img_gray,template,cv2.TM_SQDIFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    
    # top_left = min_loc
    # bottom_right = (top_left[0] + w, top_left[1] + h)
    top_left = (min_loc[0]+ w, min_loc[1])
    bottom_right = (top_left[0] + w+ 205, top_left[1] + h)
    
    crop_img = img_gray[top_left[1]:top_left[1]+h+5, top_left[0]:top_left[0]+200]
    cv2.imwrite('./images/crop.png',crop_img)
    # cv2.rectangle(img_rgb,top_left, bottom_right, 255, 2)
    # cv2.imwrite('match.png',img_rgb)

def image_to_text(image):
    # CONVERTS AN IMAGE TO TEXT
    img = Image.open(image) 
    pytesseract.pytesseract.tesseract_cmd ='C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'

    # start_time = time.time()
    result = pytesseract.image_to_string(img).lower()
    # print("--- %s seconds ---" % (time.time() - start_time))
    return result

def similiar_words(target_word,model_google):
    # GETS SIMILIAR WORDS
    try:
        url = 'https://www.dictionaryapi.com/api/v3/references/thesaurus/json/'
        url= url +target_word +'?key='+'api_key_here'
        # print(url)
        response = requests.post(url)
        r_data= response.json()
        related_words=[]
        for item in r_data[0]['meta']['syns']:
            related_words.append(item)
        return related_words[0]
    except:
        print('not in thesaurus. using NLP look up...')
        try:
            candidate_words=[]
            for item in model_google.most_similar(target_word, topn=10):
                candidate_words.append(item[0].lower().replace('_', ' '))
            related_words= candidate_words
            return related_words  
        except:
            pass

def pick_word(similar_word_list,target_word):
    # PICK THE WORD TO ENTER
    # it shares prefix (4 character) with original word
    # it has more than 10 characters
    accepted_words=[]
    for word in similar_word_list:
        if word[:4] == target_word[:4] or len(word) > 15:
            continue
        else:
            accepted_words.append(word)
    return accepted_words

def enter_word(word):
    pyautogui.click(1292, 872)
    pyautogui.write(word)
    pyautogui.press('enter')

def problem_words(target_word):
    if target_word== 'snow':
        return [True, 'white']
    elif target_word== 'sports':
        return [True, 'ball']
    elif target_word== 'lemonade':
        return [True, 'drink']
    elif target_word== 'electricity':
        return[True, 'spark']
    elif target_word== 'egg':
        return[True, 'chicken']
    else:
        return [False, None]
    
def main_process():
    pyautogui.moveTo(1292, 872)
    currentMouseX, currentMouseY = pyautogui.position()
    if (1200< currentMouseX < 1350) or (750 < currentMouseY< 950):
        # print('screenshotting...')
        while True:
            i=0
            get_game()
            raw_image= './images/raw_capture.png'
        
            # print('isolating word...')
            isolate_word(raw_image)
        
            # print('reading word from image...')
            target_word= image_to_text('./images/crop.png')
            print('Target word=', target_word)
            if target_word== ('' or ' '):
                time.sleep(0.05)
                pass
            try:
                # print('finding similiar words...')
                similar_word_list= similiar_words(target_word, model_google)
                similar_word_list= pick_word(similar_word_list, target_word)
                # print('Similiar words=', similar_word_list)
            
                word= similar_word_list[0]
                print('entering word=', word)
                enter_word(word)
                get_game()
                check_image= './images/raw_capture.png'
                isolate_word(check_image)
                new_word= image_to_text('./images/crop.png')
                        
                while new_word== target_word:
                    word= similar_word_list[i+1]
                    enter_word(word)
                    get_game()
                    check_image= './images/raw_capture.png'
                    isolate_word(check_image)
                    new_word= image_to_text('./images/crop.png')
                    i+=1
            except:
                time.sleep(0.05)
                pass
        
        currentMouseX, currentMouseY = pyautogui.position()
        # time.sleep(0.75)
    else:
        quit
def just_google():
    pyautogui.moveTo(1292, 872)
    currentMouseX, currentMouseY = pyautogui.position()
    old_word=''
    
    if (1200< currentMouseX < 1350) or (750 < currentMouseY< 950):
        # print('screenshotting...')
        while True:
            i=0
            get_game()
            raw_image= './images/raw_capture.png'
        
            # print('isolating word...')
            isolate_word(raw_image)
        
            # print('reading word from image...')
            target_word= image_to_text('./images/crop.png')
            print('Target word=', target_word)
            if target_word== ('' or ' '):
                time.sleep(0.5)
                pass
        
            # print('finding similiar words...')
            candidate_words= []
            try:
                for item in model_google.most_similar(target_word, topn=10):
                    candidate_words.append(item[0].lower().replace('_', ' '))
                candidate_words= pick_word(candidate_words,target_word)
                # print('Similiar words=', candidate_words)
                
                word= candidate_words[0]
                print('entering word=', word)
                enter_word(word)
                get_game()
                check_image= './images/raw_capture.png'
                isolate_word(check_image)
                new_word= image_to_text('./images/crop.png')
                    
                while new_word== target_word:
                    word= candidate_words[i+1]
                    enter_word(word)
                    get_game()
                    check_image= './images/raw_capture.png'
                    isolate_word(check_image)
                    new_word= image_to_text('./images/crop.png')
                    i+=1
            except:
                time.sleep(0.05)
                pass
        currentMouseX, currentMouseY = pyautogui.position()
        # time.sleep(1.5)
    else:
        quit

def run_google():
    try:
        just_google()
    except:
        time.sleep(0.05)

        just_google()
    
def run_composite():
    try:
        main_process()
    except:
        time.sleep(0.05)
        main_process()
        
#%%
start_time = time.time()

print('loading NLP model...')
model_google = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
print("--- Loaded model in %s seconds ---" % (time.time() - start_time))

#%%
# run_google() #just using NLP model
run_composite() #with thesaurus and NLP
print("--- %s seconds ---" % (time.time() - start_time))