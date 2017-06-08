#This code is test for getting 3 colors histogram and 2D color historm. 

from __future__ import print_function 
from matplotlib import pyplot as plt
import numpy as np 
import cv2
import argparse

ap =argparse.ArgumentParser()
ap.add_argument("-i","--image",required =True,help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Orignal",image)
cv2.waitKey(0)


chans = cv2.split(image)
colors=("b","g","r")
plt.figure()
plt.title("'Flattened' Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")

for (chan ,color) in zip (chans,colors):
	hist =cv2.calcHist([chan],[0],None,[256],[0,256])
	plt.plot(hist,color = color)
	plt.xlim(0,256)

plt.show()
cv2.waitKey(0)
	
fig = plt.figure()

ax = fig.add_subplot(131)
hist = cv2.calcHist([chans[1],chans[0]],[0,1],None,[32,32],[0,256,0,256])
p = ax.imshow(hist,interpolation = "nearest")
ax.set_title("2D Color Histogram for G and B")
plt.colorbar(p)

ax =fig.add_subplot(132)
hist = cv2.calcHist([chans[1],chans[2]],[0,1],None,[32,32],[0,256,0,256])
p = ax.imshow(hist,interpolation = "nearest")
ax.set_title("2D Color Histogram for G and R")
plt.colorbar(p)

ax = fig.add_subplot(133)
hist = cv2.calcHist([chans[0],chans[2]],[0,1],None,[32,32],[0,256,0,256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D Color Histogram for B and R")
plt.colorbar(p)

plt.show()
cv2.waitKey(0)

print("2D histogram shap: {},with {} values".format(hist.shape,hist.flatten().shape[0]))
