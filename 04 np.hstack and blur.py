#This is a way for me to learn blur and np.hstack.
#np.hstack is so useful,and I love it sooooo much.
#In C language,I wrote a lot code can got it before.
#We make use of the np.hstack function to stack our output images together.
#This methodd "horizontally stacks" our three images into a row.
#This is useful since we don't want to create three separate windows using the cv2.imshow function.

import numpy as np 
import argparse
import cv2

ap =argparse.ArgumentParser()
ap.add_argument("-i","--image",required =True,help="Path to the Image")
args =vars(ap.parse_args())

image =cv2.imread(args["image"])
cv2.imshow("Original",image)

blurred = np.hstack([cv2.blur(image,(3,3)),cv2.blur(image,(5,5)),cv2.blur(image,(7,7))])
cv2.imshow("Areaged",blurred)
cv2.waitKey(0)
