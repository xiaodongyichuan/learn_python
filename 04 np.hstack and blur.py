#This is a way for me to learn blur and np.hstack.
#np.hstack is so useful,and I love it sooooo much.
#In C language,I wrote a lot code can got it before.
#We make use of the np.hstack function to stack our output images together.
#This methodd "horizontally stacks" our three images into a row.
#This is useful since we don't want to create three separate windows using the cv2.imshow function.


#AVERAGING
#We are going to define a k*k sliding window on top of our image, where k is always an odd number.
#This window is going to slide from left-to-right and from top-to-bottom.The pixel at the center of this matrix is then set to be the avergae of all other pixels surrounding it.
#(ve have to use an odd number,otherwise there would not be a true "center")

import numpy as np 
import argparse
import cv2

ap =argparse.ArgumentParser()
ap.add_argument("-i","--image",required =True,help="Path to the Image")
args =vars(ap.parse_args())

image =cv2.imread(args["image"])
cv2.imshow("Original",image)

blurred = np.hstack([cv2.blur(image,(3,3)),cv2.blur(image,(5,5)),cv2.blur(image,(7,7))])
cv2.imshow("Averaged",blurred)
cv2.waitKey(0)


#GAUSSIAN
#Gaussian blurring is similar to vaverage blurring,but instead of using a simple mean,
#we are now using a weighted mean,where neighborhood pixels that are closer to the central
#pixel contribute more "weight" to the average.


blurred = np.hstack([cv2.GaussianBlur(image,(3,3),0),cv2.GaussianBlur(image,(5,5),0),cv2.GaussianBlur(image,(7,7),0)])
cv2.imshow("Gaussian",blurred)
cv2.waitKey(0)

#Here you can see that we are making use of the cv2.
#GaussianBlur function on Lines 36-38. The first argument
#to the function is the image we want to blur. Then, similar to cv2.blur, we provide a tuple representing our kernel
#size. Again, we start with a small kernel size of 3 × 3 and
#start to increase it.
#The last parameter is our s, the standard deviation in the
#x-axis direction. By setting this value to 0, we are instructing OpenCV to automatically compute them based on our
#kernel size.


#MEDIAN
#Traditionally, the median blur method has been most effective when removing salt-and-pepper noise.
#This type of noise is exactly what it on your dining room table,and sprinkling salt and pepper on top of it.
#using the median blur method,you could remove the salt and pepper from your image.
#Median blurring is more effective at removing salt-and-pepper style noise from an image 
#because each central pixel is always replaced with a pixel intensity that exists in the image.


blurred = np.hstack([cv2.medianBlur(image,3),cv2.medianBlur(image,5),cv2.medianBlur(image,7)])
cv2.imshow("Median",blurred)
cv2.waitKey(0)


#BILATERAL
#In order to reduce noise while still maintaining edges,we cean use bilateral blurring.
#Bilateral blurring accomplishes this by introducing two Gaussian distributions.
#   The first Gaussian function only considers spatial neighbors,that is, pixels that
   #appear close together in the (x,y) coordinate space of the image.
#   The second Gaussian then models the pixel intensity of the neighborhood, ensuring that
   #only pixels with similar intensity are included in the actual computation of the blur.
#Overall, this method is able to preserve edges of an image, while still reducing noise.
#The largest downside to this method is that it is considerably solwer than its averaging,Gaussian,and median blurring counterparts.

blurred = np.hstack([cv2.bilateralFilter(image,5,21,21),cv2.bilateralFilter(image,7,31,31),cv2.bilateralFilter(image,7,41,41)])
cv2.imshow("Bilateral",blurred)
cv2.waitKey(0)

#This is the end of image's blur, and I love the Bilateral so much, I think I will use it on my picture next time.
