# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 11:29:03 2020

@author: PC User
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
import time
from statistics import mean
import pytesseract


def get_selected_words(screen):
    """
    Return a list of words highlighted on the screen
    based on the light blue theme color of the game
    Reference docs:
    https://docs.opencv.org/3.3.0/d4/dc6/tutorial_py_template_matching.html
    :param screen: screen image instance returned by pyautogui
    :return: (list) highlighted words on the screen
    """
    selected_words = []

    screen_img_gray = cv2.cvtColor(screen, cv2.COLOR_RGB2GRAY)
    template = cv2.imread('arcade_template.png',0)
    w, h = template.shape[::-1]
    
    # apply opencv template matching
    res_img = cv2.matchTemplate(
        screen_img_gray, template, cv2.TM_CCOEFF_NORMED)

    # find the screen image section where the template is matching
    # with the given threshold range
    threshold = 0.75
    loc = np.where(res_img >= threshold)
    print(loc[0])
    
    for pt in zip(*loc[::-1]):
        # crop rectangle section around the selected template
        # a rectangle right next to the template
        cropped_image = screen_img_gray[pt[1]:pt[1] + h + 5, pt[0] + w:pt[0] + w + 205]

        # append the image text to selected word list using tesseract
        selected_words.append(pytesseract.image_to_string(cropped_image))

    return selected_words

screen= cv2.imread('test.png')
get_selected_words(screen)
word= pytesseract.image_to_string('word.png')
print(word)
#%%
img_rgb = cv2.imread('test.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('arcade_template.png',0)
# w, h = template.shape[::-1]

# times= {'cv2.TM_CCOEFF_NORMED': [],
#         'cv2.TM_CCORR_NORMED': [],
#         'cv2.TM_SQDIFF': [],
#         }


res = cv2.matchTemplate(img_gray,template,cv2.TM_SQDIFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

# top_left = min_loc
# bottom_right = (top_left[0] + w, top_left[1] + h)
top_left = (min_loc[0]+ w, min_loc[1])
bottom_right = (top_left[0] + w+ 205, top_left[1] + h)
cv2.rectangle(img_rgb,top_left, bottom_right, 255, 2)
cv2.imwrite('res.png',img_rgb)

# =============================================================================
# for key in times:
#     start_time = time.time()
#     img = img_gray
#     method = eval(key)
#     # Apply template Matching
#     res = cv2.matchTemplate(img,template,method)
#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#     # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
#     if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
#         top_left = min_loc
#     else:
#         top_left = max_loc
#         
# 
#     bottom_right = (top_left[0] + w, top_left[1] + h)
#     cv2.rectangle(img,top_left, bottom_right, 255, 2)
#     plt.subplot(121),plt.imshow(res,cmap = 'gray')
#     # plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
#     # plt.subplot(122),plt.imshow(img,cmap = 'gray')
#     # plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
#     # plt.suptitle(key)
#     plt.show()
# =============================================================================
    
# =============================================================================
# i=0
# while i < 500:
#     for key in times:
#         start_time = time.time()
#         img = img2.copy()
#         method = eval(key)
#         # Apply template Matching
#         res = cv2.matchTemplate(img,template,method)
#         min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#         # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
#         if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
#             top_left = min_loc
#         else:
#             top_left = max_loc
#             
#         # print(key)    
#         # print("--- %s seconds ---" % (time.time() - start_time))
#         times[key].append(time.time() - start_time) 
#     i+=1
# 
# for key in times:
#     print(key, mean(times[key]))
# =============================================================================
# =============================================================================
#     bottom_right = (top_left[0] + w, top_left[1] + h)
#     cv2.rectangle(img,top_left, bottom_right, 255, 2)
#     plt.subplot(121),plt.imshow(res,cmap = 'gray')
#     plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
#     plt.subplot(122),plt.imshow(img,cmap = 'gray')
#     plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
#     plt.suptitle(key)
#     plt.show()
# =============================================================================
