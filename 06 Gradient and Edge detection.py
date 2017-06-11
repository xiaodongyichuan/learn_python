#Today,I learned what was gradient and how to detect the edge of an image.
#Gradient can be seen as derivative in some times.
#Edge detection embodies mathematical methods to find points in an image where the brightness of pixel intensities changes distinctly.
#I will show several methods (like: Laplacian,Sobel,Canny)in here.Let's go ahead and expore some code:

import numpy as np
import argparse
import cv2

ap =argparse.ArgumentParser()
ap.add_argument("-i","--image",required =True,help="Path to the image")
args =vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Original",image)


#Laplacian 
lap = cv2.Laplacian(image,cv2.CV_64F)   #If we don't use a floating point data type,then take the absolute value of the gradient image and convert it back to an 8-bit unsigned ineger,otherwise we'll be missing edges in our image.
lap = np.uint8(np.absolute(lap))
cv2.imshow("Laplacian",lap)
cv2.waitKey(0)

#Sobel 
sobelX =cv2.Sobel(image,cv2.CV_64F,1,0)
sobelY =cv2.Sobel(image,cv2.CV_64F,0,1)

sobelX =np.uint8(np.absolute(sobelX))
sobelY =np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX,sobelY)

cv2.imshow("Sobel X",sobelX)
cv2.imshow("Sobel Y",sobelY)
cv2.imshow("Sobel Combined",sobelCombined)

cv2.waitKey(0)

#Canny edge detector
image =cv2.GaussianBlur(image,(5,5),0)
cv2.imshow("Blurred",image)

canny =cv2.Canny(image,50,150)
cv2.imshow("Canny",canny)
cv2.waitKey(0)
