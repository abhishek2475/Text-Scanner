import cv2 as cv
import numpy as np
import imutils
from matplotlib import pyplot as plt
import pytesseract

class nplate:
    def __init__(self) -> None:
        pass

    def extractNplate(img):
        # img=cv.imread("vehicle1.jpg")
        img_gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        img_Filter=cv.bilateralFilter(img_gray,11,17,1)
        img_canny=cv.Canny(img_Filter,30,200)

        img_keypoints=cv.findContours(img_canny.copy(),cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
        contour=imutils.grab_contours(img_keypoints)
        contour=sorted(contour,key=cv.contourArea,reverse=True)[:10]
        location=None
        for cnd in contour:
            approx=cv.approxPolyDP(cnd,8,True)
            if len(approx)==4:
                location=approx
                break

        # print(location)


        mask=np.zeros(img_gray.shape,np.uint8)
        image_mask=cv.drawContours(mask,[location],0,255,-1)

        image_mask=cv.bitwise_and(img,img,mask=mask)
        # image_mask=cv.cvtColor(image_mask,cv.COLOR_BGR2RGB)
        # image_mask=


        (x,y)=np.where(mask==255)
        (x1,y1)=((np.min(x)),(np.min(y)))
        (x2,y2)=((np.max(x)),(np.max(y)))
        only_NumberPlate=img[x1:x2+1,y1:y2+1]
        # cv.imshow("hello",cv.cvtColor(only_NumberPlate,cv.COLOR_BGR2RGB))
        # # cv.imshow("New",image_mask)
        # cv.waitKey(0)
        # cv.destroyAllWindows()

        a=pytesseract.image_to_string(cv.cvtColor(image_mask,cv.COLOR_BGR2RGB))
        return a
    
    
# img=cv.imread("vehicle1.jpg")
# a=nplate.extractNplate(img)
# print(a)