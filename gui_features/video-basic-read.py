import cv2 as cv

# Receive as argument the camera index
# If passed a String as argument, it will load a video
cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break

# Get frame width, pass second argument as an Int to resize 
print("Frame width: {}".format(cap.get(cv.CAP_PROP_FRAME_WIDTH)))

# Get frame length, pass second argument as an Int to resize 
print("Frame width: {}".format(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()