#Today,I realized thresholding throughout several methods: blur,mean,Gaussian,OTSU and Riddler-Calvard
#Normally,we use thresholding methons to focus on object or areas of particular interest in an image.

from __future__ import print_function
import numpy as np
import argparse 
import cv2
import mahotas
ap =argparse.ArgumentParser()
ap.add_argument("-i","--image",required =True,help="Path to the image")
args = vars(ap.parse_args())

image =cv2.imread(args["image"])
image =cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image,(5,5),0)
cv2.imshow("Image",image)

#simple thresholding
(T,thresh) =cv2.threshold(blurred,155,255,cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary",thresh)

(T,threshInv) =cv2.threshold(blurred,155,255,cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverse",threshInv)

cv2.imshow("Coins",cv2.bitwise_and(image,image,mask = thresh))
cv2.waitKey(0)

#adaptive thresholding
#mean weighted adaptive thresholding
thresh =cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,4)
cv2.imshow("Mean Thresh",thresh)
#Gaussian weighted mean thresholding
thresh =cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,15,3)
cv2.imshow("Gaussian Thresh",thresh)
cv2.waitKey(0)

#OTSU AND RIDDLER-CALVARD


ap =argparse.ArgumentParser()
ap.add_argument("-i","--image",required =True,help ="Path to the image")
args=vars(ap.parse_args())
image =cv2.imread(args["image"])
image =cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blurred =cv2.GaussianBlur(image,(5,5),0)
cv2.imshow("Image",image)

T = mahotas.thresholding.otsu(blurred)   #OTSU
print("Otsu's threshold: {}".format(T))
thresh =image.copy()
thresh[thresh > T] =255
thresh[thresh < 255]= 0
thresh =cv2.bitwise_not(thresh) 
cv2.imshow("Otsu",thresh)

T=mahotas.thresholding.rc(blurred)      #Riddler-Calvard
print("Riddler-Calvard: {}".format(T))
thresh = image.copy()
thresh[thresh > T]=255
thresh[thresh <255]=0
thresh =cv2.bitwise_not(thresh)
cv2.imshow("Riddler-Calvard",thresh)
cv2.waitKey(0)

from __future__ import print_function
import numpy as np
import argparse 
import cv2
import mahotas
ap =argparse.ArgumentParser()
ap.add_argument("-i","--image",required =True,help="Path to the image")
args = vars(ap.parse_args())

image =cv2.imread(args["image"])
image =cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image,(5,5),0)
cv2.imshow("Image",image)

#simple thresholding
(T,thresh) =cv2.threshold(blurred,155,255,cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary",thresh)

(T,threshInv) =cv2.threshold(blurred,155,255,cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverse",threshInv)

cv2.imshow("Coins",cv2.bitwise_and(image,image,mask = thresh))
cv2.waitKey(0)

#adaptive thresholding
#mean weighted adaptive thresholding
thresh =cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,4)
cv2.imshow("Mean Thresh",thresh)
#Gaussian weighted mean thresholding
thresh =cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,15,3)
cv2.imshow("Gaussian Thresh",thresh)
cv2.waitKey(0)

#OTSU AND RIDDLER-CALVARD


ap =argparse.ArgumentParser()
ap.add_argument("-i","--image",required =True,help ="Path to the image")
args=vars(ap.parse_args())
image =cv2.imread(args["image"])
image =cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blurred =cv2.GaussianBlur(image,(5,5),0)
cv2.imshow("Image",image)

T = mahotas.thresholding.otsu(blurred)   #OTSU
print("Otsu's threshold: {}".format(T))
thresh =image.copy()
thresh[thresh > T] =255
thresh[thresh < 255]= 0
thresh =cv2.bitwise_not(thresh) 
cv2.imshow("Otsu",thresh)

T=mahotas.thresholding.rc(blurred)      #Riddler-Calvard
print("Riddler-Calvard: {}".format(T))
thresh = image.copy()
thresh[thresh > T]=255
thresh[thresh <255]=0
thresh =cv2.bitwise_not(thresh)
cv2.imshow("Riddler-Calvard",thresh)
cv2.waitKey(0)
