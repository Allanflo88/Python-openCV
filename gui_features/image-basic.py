import cv2 as cv
from matplotlib import pyplot as plt

# Read Image
img = cv.imread('resources/star-wars.jpg', cv.IMREAD_COLOR )

# Show Image
cv.imshow('star-wars',img)

# Indefinitely waits for a key input if = 0, otherwise wait for the time in miliseconds
# return pressed key
cv.waitKey(0)
cv.destroyAllWindows()

# Set name window 'image' to normal, default is WINDOW_AUTOSIZE
cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()

# Save image in PNG format
img_gray = cv.imread('resources/star-wars.jpg', cv.IMREAD_GRAYSCALE )
cv.imwrite('resources/star-wars-gray.png',img_gray)

# Show image with MatplotLib
# Color image loaded by OpenCV is in BGR mode
# But Matplotlib displays in RGB mode
# So color images will not be displayed correctly in Matplotlib if image is read with OpenCV.
img = cv.imread('resources/star-wars.jpg',cv.IMREAD_COLOR)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()