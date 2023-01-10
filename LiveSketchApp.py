# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file"""

                #creating a live webcam sketch app using opencv

import cv2
import numpy as np
import matplotlib.pyplot as plt

#create a function to detect sketch image
def sketch(image):
    #convert colored image to grayscale
    img_gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    
    #blurring grayscale image using GaussianBlur method
    blur=cv2.GaussianBlur(img_gray, (5,5), 0)
    
    #detect edges using canny
    img_edge=cv2.Canny(blur,10,70)
    
    #to get sketching effect use inverse binary threshold 
    ret,mask= cv2.threshold(img_edge,80,255,cv2.THRESH_BINARY_INV)
    return mask

#capture live videocam feed using cv2.VideoCapture
cap=cv2.VideoCapture(0)

#using while loop to continuously get webcam feed
while True:
    ret, frame= cap.read()
    
    cv2.imshow('live sketch feed',sketch(frame))
    
    #specific key(q in this case) to exit the video feed with cv2.waitKey 
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
