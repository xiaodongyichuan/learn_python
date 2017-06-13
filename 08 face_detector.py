#Today, I have two parts of *.py files to show for this face_detector.
#One is named detect_faces.py and another named facedetector.py
#usage: python detect_faces.py --face haarcascade_frontalface_default.xml --image test.jpg
#Notes: You should download the haarcascade_frontalface_default.xml file online and put into the same folder where the two py files is.

#In this paragraph, we use the built-in Haar classifiers in Opencv. It's too old but it also can be used for beginner.


################################################
#detect_faces.py
################################################


from __future__ import print_function
from facedetector import FaceDetector
import argparse
import cv2

ap =argparse.ArgumentParser()
ap.add_argument("-f","--face",required = True,help ="Path to where the face cascade resides")
ap.add_argument("-i","--image",required = True,help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


fd = FaceDetector(args["face"])
faceRects = fd.detect(gray,scaleFactor = 1.04,minNeighbors = 6,minSize = (8,8))
print("I found {} face(s)".format(len(faceRects)))

for (x,y,w,h) in faceRects:
	cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("Faces",image)
cv2.imwrite('result.jpg',image)
cv2.waitKey(0)



################################################
#facedetector
################################################

import cv2

class FaceDetector:
	def __init__(self,faceCascadePath):
		self.faceCascade = cv2.CascadeClassifier(faceCascadePath)

	def detect(self,image,scaleFactor = 1.1, minNeighbors = 5, minSize = (30,30)):
		rects = self.faceCascade.detectMultiScale(image,scaleFactor = scaleFactor, minNeighbors = minNeighbors, minSize = minSize, flags = cv2.CASCADE_SCALE_IMAGE)
		return rects

