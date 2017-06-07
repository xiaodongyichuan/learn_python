import numpy as np
import cv2
import imutils
import argparse
import math


rectangle = np.zeros((300,300),dtype ="uint8")
original=rectangle
next_time =cv2.bitwise_not(original)

mask =imutils.rotate(next_time,45,scale= math.sqrt(2)/2)
mask =cv2.bitwise_not(mask)
cv2.imshow("mask",mask)

for i in range (0,20):	
	generate = next_time
	generate =imutils.rotate(generate,45,scale= math.sqrt(2)/2)
	b=next_time[5,5]
	print("b={}".format(b))
	print("i={}".format(i)) 
	if i%2 ==1:
		next_time=cv2.bitwise_or(generate,mask)
	else:
	 	next_time=generate
	cv2.imshow("next_time",next_time)
	cv2.waitKey(0)	
		

cv2.imshow("next_time",next_time)
cv2.imshow("generate",generate)
cv2.waitKey(0)
