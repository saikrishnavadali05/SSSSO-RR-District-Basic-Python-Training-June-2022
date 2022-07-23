"""
Write a program to load, open and save an image. 
(hint : use opencv-python or PIL modules. Research about them on google and youtube)
"""
import cv2

img = cv2.imread("D:/image/flamingo.jpg")

print(img)
print(type(img)) # <class 'numpy.ndarray'>


# Displaying the image----------
cv2.imshow('image',img)
cv2.waitKey(0) # wait until a  key it is pressed.
cv2.destroyAllWindows()

# Saving the image-------------
# Reading image as a grey scale.
grey_img = cv2.imread("D:/image/flamingo.jpg",cv2.IMREAD_GRAYSCALE)

# save image
status = cv2.imwrite("D:/image/flamingo_grey.jpg",grey_img)

print("Image written to a file-System",status)