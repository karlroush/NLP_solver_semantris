# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 16:41:52 2020

@author: compute
"""
import cv2

img_rgb = cv2.imread('test.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('arcade_template.png',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray,template,cv2.TM_SQDIFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

# top_left = min_loc
# bottom_right = (top_left[0] + w, top_left[1] + h)
top_left = (min_loc[0]+ w, min_loc[1])
bottom_right = (top_left[0] + w+ 205, top_left[1] + h)

crop_img = img_gray[top_left[1]:top_left[1]+h+5, top_left[0]:top_left[0]+150]
cv2.imwrite('crop.png',crop_img)

cv2.rectangle(img_rgb,top_left, bottom_right, 255, 2)
cv2.imwrite('res.png',img_rgb)