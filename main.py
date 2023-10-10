import cv2 as cv
img=cv.imread('aero3.jpg')
cv.imshow("First Image",img)
cv.waitKey(0)
cv.destroyAllWindows()