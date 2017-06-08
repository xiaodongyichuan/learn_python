#This project is playing for R,G,B 
#My first thing to do is show the R,G,B channels thought cv2.split
#And then I change the channel sequence and chack the change.


import argparse
import cv2
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

(B,G,R) = cv2.split(image)

cv2.imshow("Red",R)
cv2.imshow("Green",G)
cv2.imshow("Blue",B)

merged =cv2.merge([B,G,R])
cv2.imshow("B,G,R",merged)

merged =cv2.merge([G,B,R])
cv2.imshow("G,B,R",merged)


merged =cv2.merge([R,B,G])
cv2.imshow("R,B,G",merged)


merged =cv2.merge([B,R,G])
cv2.imshow("B,R,G",merged)


merged =cv2.merge([G,R,B])
cv2.imshow("G,R,B",merged)

merged =cv2.merge([B,G,B])
cv2.imshow("R,G,B",merged)

merged =cv2.merge([B,G,B])
cv2.imshow("B,G,B",merged)

merged =cv2.merge([G,B,G])
cv2.imshow("G,B,G",merged)

cv2.waitKey(0)
