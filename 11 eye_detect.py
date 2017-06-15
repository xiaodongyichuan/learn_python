# Today, we will talk about the tracting face again, and will add the function in eyes detecting.

# This project will contain two files,named "11 eyetracking.py" and "eyestracker.py" respectively.
#The cord belows:

###################################################################################################

# 11 eyetracking.py

from eyestracker import EyeTracker
import imutils
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--face", required = True, help = "Path to where the face cascade resides")
ap.add_argument("-e", "--eye", required = True, help = "Path to where the eye cascade resides")
ap.add_argument("-v", "--video", required = False, help = "Path to the (optional) video file")
args = vars(ap.parse_args())

et = EyeTracker(args["face"], args["eye"])

if not args.get("video", False):
	camera = cv2.VideoCapture(0)

else:
	camera = cv2.VideoCapture(args["video"])

while True:
	(grabbed,frame) = camera.read()

	if args.get("video") and not grabbed:
		break

	frame = imutils.resize(frame, width = 300)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	rects = et.track(gray)
	
	for rect in rects:
		cv2.rectangle(frame, (rect[0], rect[1]), (rect[2], rect[3]), (0, 255, 0), 2)
	
	cv2.imshow("Tracking", frame)
	
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break

camera.release()
cv2.destroyAllWindows()



#############################################################################################

# eyestracker.py

import cv2

class EyeTracker:
	def __init__(self, faceCascadePath, eyeCascadePath):
		self.faceCascade = cv2.CascadeClassifier(faceCascadePath)
		self.eyeCascade = cv2.CascadeClassifier(eyeCascadePath)
	
	def track(self,image):
		faceRects = self.faceCascade.detectMultiScale(image, scaleFactor = 1.1, minNeighbors = 5, minSize = (30,30), flags = cv2.CASCADE_SCALE_IMAGE)
		rects = []
		
		for (fX, fY, fW, fH) in faceRects:
			faceROI = image[fY:fY + fH, fX:fX + fW]
			rects.append((fX, fY, fX + fW, fY + fH))
			
			eyeRects = self.eyeCascade.detectMultiScale(faceROI, scaleFactor = 1.1, minNeighbors = 10, minSize = (20, 20), flags = cv2.CASCADE_SCALE_IMAGE)

			for (eX, eY, eW, eH) in eyeRects:
				rects.append((fX + eX, fY + eY, fX + eX + eW, fY + eY + eH))

		return rects
    
