import cv2
import numpy
img= cv2.imread('bookpage.jpg')

retval,threshhold=cv2.threshold(img,12,255,cv2.THRESH_BINARY)

grayscaled=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval,threshhold2=cv2.threshold(grayscaled,12,255,cv2.THRESH_BINARY)

gaus= cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,115,1)
                            
                            
cv2.imshow('orignal',img)
cv2.imshow('threshhold',threshhold)
cv2.imshow('threshhold2',threshhold2)
cv2.imshow('gaus',gaus)
cv2.waitKey(0)
cv2.destroyAllWindows()
