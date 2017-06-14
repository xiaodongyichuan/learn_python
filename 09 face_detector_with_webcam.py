# A beautiful morning,It's funny and can learn lots of technology at morning.
# First thing is that,in Python ,you can't import filename start with a number.It's sooooo important for me,
    #because when I import a package named "09 facedetector",then "SyntaxError: invalid token",
    #and then I change the name to "09_facedetector",then also "SyntaxError: invalid token".I was confused about why?
    #then baidu it,found that YOU CAN NOT IMPORT A PACKAGE NAMED START WITH A NUMBER. And then, there is a solve about
    # "In python, how to importt filename start with a number". Links: https://stackoverflow.com/questions/9090079/in-python-how-to-import-filename-starts-with-a-number
    
# Second thing is that,it's teach you how to get the key from keyboard and control the program.
    #  use " 0xFF == ord("q") " to monitor if the "q" has been pressed.
    
# In progarm ," ap.add_argument("-v","--video",required =True,help ="Poth to the video") ",
    #If the --video isnot necessary,you can delete the "required =True" or change the part tobe "required =Flase"
  
  ############################################################################################
  
# Come back to today's subject.Today,I want to detect my face with webcam.
# Here we go.
# In today's project,we have to files named 09_cam.py and facedetector.py respectively.
# Usage1 (If you want to use video files): python 09_cam.py --face haarcascade_frontalface_default.xml --video [yourvideo]
# Usage2 (If you want to use webcam): python 09_cam.py --face haarcascade_frontalface_default.xml 


##############################################################################################
#09_cam.py
##############################################################################################
from facedetector import FaceDetector
import imutils
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-f","--face",required =True,help ="Path to where the face cascade resides")
ap.add_argument("-v","--video",required =False,help="Path to the image")
args = vars(ap.parse_args())

fd = FaceDetector(args["face"])

if not args.get("video",False):
	camera = cv2.VideoCapture(0)

else:
	camera = cv2.VideoCapture(args["video"])

while True:
	(grabbed,frame) = camera.read()

	if args.get("video") and not grabbed:
		break
	
	frame = imutils.resize(frame,width = 300)
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	##################################################
	faceRects = fd.detect(gray,scaleFactor = 1.1,minNeighbors = 5, minSize = (30,30))
	frameClone = frame.copy()
	
	for (fX,fY,fW,fH) in faceRects:
		cv2.rectangle(frameClone,(fX,fY),(fX+fW,fY+fH),(0,255,0),2)
	
	cv2.imshow("Face",frameClone)

	if cv2.waitKey(1) & 0xFF == ord("q"):   #great
		break

camera.release()
cv2.destroyAllWindows()




##############################################################################################
#facedetector.py
##############################################################################################

import cv2

class FaceDetector:
	def __init__(self,faceCascadePath):
		self.faceCascade = cv2.CascadeClassifier(faceCascadePath)

	def detect(self,image,scaleFactor = 1.1, minNeighbors = 5, minSize = (30,30)):
		rects = self.faceCascade.detectMultiScale(image,scaleFactor = scaleFactor, minNeighbors = minNeighbors, minSize = minSize, flags = cv2.CASCADE_SCALE_IMAGE)
		return rects

