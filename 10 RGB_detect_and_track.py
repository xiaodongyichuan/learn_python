# Before we start today's project,let's learn something perpare for it.

# Firstly, it's the function named " cv2.inRange（src, lowerb, upperb[, dst]） → dst "
    # Official formal explanation： Checks if array elements lie between the elements of two other arrays.
                     # dst(I) = lowerb(I)<= src(I)<= upperb(I) 
    # Used this function you will get a binary image. If you want get a binary image ,there sevel methods
    # you can take it: compare(), inRange(), threshold(), adaptiveThreshold(), Canny().
    
# Secondly, the function is named " cv2.findContours(image, mode, method[, hierarchy[, offset]]) → contours, hierarchy "
    # This function for finding contours in a binary image. 
    # If want learn more,this link will help you. http://docs.opencv.org/2.4/modules/imgproc/doc/structural_analysis_and_shape_descriptors.html?highlight=cv2.findcontour#cv2.findContours
    
###############################################################################

# Today's project is tell you how to use RGB to detect and track things.

# Code belows here :
# Usage: python 10 object_tracking_in_video.py
###############################################################################

#named: 10 object_tracking_in_video.py

import numpy as np
import argparse
import time
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required =False, help = "Path to the video (optional)")
args = vars(ap.parse_args())

Lower = np.array([50,60,90], dtype = "uint8")  #bgr
Upper = np.array([110,150,200], dtype = "uint8")



if not args.get("video",False):
	camera = cv2.VideoCapture(0)

else:
	camera = cv2.VideoCapture(args["video"])


while True:
	(grabbed,frame) =camera.read()
	
	if not grabbed:
		break
	
	blue = cv2.inRange(frame,Lower,Upper)  
	#this function is a thresholded image,
	#with pixels faliing within the upper and lower range set to white 
	#and pixels that do not fall into this range set as black

	blue = cv2.GaussianBlur(blue,(3,3),0)
	
	(_,cnts,_) = cv2.findContours(blue.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	
	if len(cnts) > 0:
		cnt = sorted(cnts, key = cv2.contourArea, reverse = True)[0]

		rect = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt)))
		cv2.drawContours(frame,[rect], -1, (0, 255, 0), 2)

	cv2.imshow("Tracking", frame)
	cv2.imshow("Binary", blue)

	time.sleep(0.025)

	if cv2.waitKey(1) & 0xFF == ord("q"):
		break

camera.release()
cv2.destroyAllWindows()
