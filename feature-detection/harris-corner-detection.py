import numpy as np
import cv2 as cv

filename = '../resources/chessboard.jpg'
img = cv.imread(filename)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Find Harris corners
gray = np.float32(gray)
dst = cv.cornerHarris(gray, 2, 3, 0.04)

# Result is dilated for marking the corners, not important
dst = cv.dilate(dst, None)
ret, dst = cv.threshold(dst, 0.01*dst.max(), 255, 0)
dst = np.uint8(dst)

# Find centroids
ret, labels, stats, centroids = cv.connectedComponentsWithStats(dst)

# Define the criteria to stop and refine the corners
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners = cv.cornerSubPix(gray,
                          np.float32(centroids),
                          (5, 5),
                          (-1, -1),
                          criteria)

# Now draw them
res = np.hstack((centroids, corners))
res = np.int0(res)
img[res[:, 1], res[:, 0]] = [0, 0, 255]
img[res[:, 3], res[:, 2]] = [0, 255, 0]
cv.imwrite('corners.png', img)
cv.imshow('corners.png', img)
if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()
