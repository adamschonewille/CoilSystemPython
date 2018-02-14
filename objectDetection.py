import cv2
import filterlib

#========================================
# ALWAYS usd greyscale image as input
# e.g. grey() -> canny() -> biggestSquareContour()
#========================================
def biggestSquareContour(image,sampleNum,epsilon):
    # image = filterlib.grey(image)
    image, contours, hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(contours, key = cv2.contourArea, reverse = True)[:sampleNum]
    screenCnt = []
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, epsilon / 1000.0 * peri, True)
        if len(approx) == 4:
            screenCnt = approx
            break
    return screenCnt