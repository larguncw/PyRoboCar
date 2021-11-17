import cv2
import numpy as np

def limbo(x):
    pass

# Load image
#image = cv2.imread('video1_372_078.png')  #filename

#Enter video location or 0 for livefeed
#capture = cv2.VideoCapture('older_videos/straight_lane_video1.avi') Example prerecorded video
#capture = cv2.VideoCapture(0) #Example livefeed
capture = cv2.VideoCapture('older_videos/straight_lane_video1.avi')
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if(capture.isOpened() == False):
    print("Error in opening video stream")

#Create a window
cv2.namedWindow('HSV mask')

# Create trackbars for color image
# H(ue) is from 0-179 for OpenCV
cv2.createTrackbar('H Min', 'HSV mask', 0, 179, limbo)
cv2.createTrackbar('S Min', 'HSV mask', 0, 255, limbo)
cv2.createTrackbar('V Min', 'HSV mask', 0, 255, limbo)

cv2.createTrackbar('H Max', 'HSV mask', 0, 179, limbo)
cv2.createTrackbar('V Max', 'HSV mask', 0, 255, limbo)
cv2.createTrackbar('S Max', 'HSV mask', 0, 255, limbo)

# Set default values for Max HSV trackbars
cv2.setTrackbarPos('H Max', 'HSV mask', 179)
cv2.setTrackbarPos('S Max', 'HSV mask', 255)
cv2.setTrackbarPos('V Max', 'HSV mask', 255)

# Initialize HSV min/max values
hMin = sMin = vMin = hMax = sMax = vMax = 0
phMin = psMin = pvMin = phMax = psMax = pvMax = 0

####--!! For a single image
# while(True):
#     # Get current position of all Trackbars
#     hMin = cv2.getTrackbarPos('H Min', 'HSV mask')
#     sMin = cv2.getTrackbarPos('S Min', 'HSV mask')
#     vMin = cv2.getTrackbarPos('V Min', 'HSV mask')
#
#     hMax = cv2.getTrackbarPos('H Max', 'HSV mask')
#     sMax = cv2.getTrackbarPos('S Max', 'HSV mask')
#     vMax = cv2.getTrackbarPos('V Max', 'HSV mask')
#
#     # Set min and max HSV values to display
#     lower = np.array([hMin, sMin, vMin])
#     upper = np.array([hMax, sMax, vMax])
#
#     # Convert to HSV format and color threshold
#     # hsv =  cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#     # mask = cv2.inRange(hsv, lower, upper)
#     # result = cv2.bitwise_and(image, image, mask=mask)
#     hsv = cv2.cvtColor(capture, cv2.COLOR_BGR2HSV)
#     mask = cv2.inRange(hsv, lower, upper)
#     result = cv2.bitwise_and(capture, capture, mask=mask)
#
#     # Print if there is a change in HSV value
#     if ((phMin != hMin) | (psMin != sMin) | (pvMin != vMin) | (phMax != hMax) | (psMax != sMax) | (pvMax != vMax)):
#         print("(hMin = %d , sMin = %d, vMin = %d), (hMax = %d , sMax = %d, vMax = %d)" % (
#         hMin, sMin, vMin, hMax, sMax, vMax))
#         phMin = hMin
#         psMin = sMin
#         pvMin = vMin
#         phMax = hMax
#         psMax = sMax
#         pvMax = vMax
#
#     # Display result image
#     cv2.imshow('image', result)
#     if cv2.waitKey(10) & 0xFF == ord('q'):
#        break
#while True:
while(capture.isOpened()):
    ret, frame = capture.read()
    if ret == True:
        #frame = cv2.flip(frame, 0)
        pass

    # Get current position of all Trackbars
    hMin = cv2.getTrackbarPos('H Min', 'HSV mask')
    sMin = cv2.getTrackbarPos('S Min', 'HSV mask')
    vMin = cv2.getTrackbarPos('V Min', 'HSV mask')

    hMax = cv2.getTrackbarPos('H Max', 'HSV mask')
    sMax = cv2.getTrackbarPos('S Max', 'HSV mask')
    vMax = cv2.getTrackbarPos('V Max', 'HSV mask')

    # Set min and max HSV values to display
    lower = np.array([hMin, sMin, vMin])
    upper = np.array([hMax, sMax, vMax])

    # Convert to HSV format and color threshold
    # hsv =  cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # mask = cv2.inRange(hsv, lower, upper)
    # result = cv2.bitwise_and(image, image, mask=mask)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Print if there is a change in HSV value
    if ((phMin != hMin) | (psMin != sMin) | (pvMin != vMin) | (phMax != hMax) | (psMax != sMax) | (pvMax != vMax)):
        print("(hMin = %d , sMin = %d, vMin = %d), (hMax = %d , sMax = %d, vMax = %d)" % (
        hMin, sMin, vMin, hMax, sMax, vMax))
        phMin = hMin
        psMin = sMin
        pvMin = vMin
        phMax = hMax
        psMax = sMax
        pvMax = vMax

    # Display result image
    cv2.imshow('image', result)
    if cv2.waitKey(50) & 0xFF == ord('q'): #insert int value into waitKey to make video play slower/faster. int value in milliseconds
        break
# For camera live feed
capture.release()

cv2.destroyAllWindows()