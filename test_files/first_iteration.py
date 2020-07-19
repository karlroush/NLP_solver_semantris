# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pyautogui
import time
import random
import numpy as np

def signal_handler(signum, frame):
    raise Exception("Timed out!")
    
def write_text(word):
    pyautogui.click(1289, 877)
    pyautogui.write(word)
    pyautogui.press('enter') 

def getCoords():
    print("move mouse")
    time.sleep(2)
    # screenWidth, screenHeight = pyautogui.size()
    # print(screenWidth)
    # print(screenHeight)
    currentMouseX, currentMouseY = pyautogui.position()
    print("Current [x,y]=", [currentMouseX,currentMouseY])

def gameStart():
    print("Open other window")
    time.sleep(1.5)
    
    pyautogui.click(1237, 759)
    time.sleep(2.5)
    
def tryWords(word):
    pyautogui.click(1289, 877)
    # time.sleep(random.uniform(0.05, 0.2))
    pyautogui.write(word)
    pyautogui.press('enter')
    # time.sleep(random.uniform(0.05, 0.2))
    
#%%
getCoords()

#%%
words= [['person', 'job', 'paper','sports'],
        ['blue', 'black', 'green', 'white'],
        ['outside','inside','up','down'],
        ['day','night','clock','time'],
        ['animal','zoo', 'bug', 'pet'],
        ['space','map','water', 'earth'],
        ['food', 'music', 'drink', 'TV'],
        ['thing','spark','clean','junk']
        ]
word_list= np.array(words, dtype=object)

pyautogui.moveTo(1289, 877)
currentMouseX, currentMouseY = pyautogui.position()
print("Current [x,y]=", [currentMouseX,currentMouseY])

row=0 
while (1200< currentMouseX <1300) or (800<currentMouseY<900):
    item= random.randint(0, len(word_list[row])-1)
    word= word_list[row][item]
    tryWords(word)
    row+=1
    if row == np.shape(words)[0] -1:
        row=0 

# =============================================================================
# start_time= time.time()# 
# duration= 0
# while duration <120:
#     tryWords(words)
#     duration= time.time()- start_time
# =============================================================================