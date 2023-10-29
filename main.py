import cv2 as cv
import numpy as np
import pytesseract 
from langdetect import detect
from langdetect import DetectorFactory
DetectorFactory.seed = 0


img=cv.imread('whitetext.jpg')

# cv.waitKey(0)
# cv.destroyAllWindows()


# Creating the Different function for Different functionality


# Adding Different Functionalities 


# #For inverting the image Function:
# def invertImage(img):
#     img_invert=cv.bitwise_not(img)
#     return img_invert


# #For rescalling the Image
# def rescaleImage(img,scale):
#     width = int (img.shape[1] * scale/ 100 )
#     height = int (img.shape[0] * scale / 100)
#     dim = (width, height)
#     img_Re=cv.resize(img,dim,interpolation=cv.INTER_AREA)
#     return img_Re



# #For GrayScale of Image:

# def grayImage(img):
#     img_Gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#     return img_Gray

# # Was Not working for Binarization i.e. cv.Threshold
# def binImage(img):
#     imgGray= grayImage(img)
#     imgBinarize=cv.threshold(imgGray,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
#     return imgBinarize
# imgbin=binImage(img)
# cv.imshow("Binary Image",imgbin[1])
# # cv.waitKey(0)
# # cv.destroyAllWindows()

# #For Reducing Noise From Image :
# # Thickening of font 
# #we use erodion
# def erodeImg(img):
#     img=cv.bitwise_not(img)
#     kernel=np.ones((1,1),np.uint8)
#     img=cv.erode(img,kernel,iterations=1)
#     return img
# img=erodeImg(img)
# cv.imshow("Erroded image",img)

# # for thickening the font We will use Dilation
# def imgDilate(img):
#     img=cv.bitwise_not(img)
#     kernel=np.ones((1,1),np.uint8)
#     img=cv.dilate(img,kernel,iterations=1)
#     return img
# img=imgDilate(img)
# cv.imshow("Dilate image",img)

# # Writing a function for rotation/deskewing
# # Calculate skew angle of an image
# def getSkewAngle(cvImage) -> float:
#     # Prep image, copy, convert to gray scale, blur, and threshold
#     newImage = cvImage.copy()
#     gray = cv.cvtColor(newImage, cv.COLOR_BGR2GRAY)
#     blur = cv.GaussianBlur(gray, (9, 9), 0)
#     thresh = cv.threshold(blur, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]

#     # Apply dilate to merge text into meaningful lines/paragraphs.
#     # Use larger kernel on X axis to merge characters into single line, cancelling out any spaces.
#     # But use smaller kernel on Y axis to separate between different blocks of text
#     kernel = cv.getStructuringElement(cv.MORPH_RECT, (30, 5))
#     dilate = cv.dilate(thresh, kernel, iterations=5)

#     # Find all contours
#     contours, hierarchy = cv.findContours(dilate, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
#     contours = sorted(contours, key = cv.contourArea, reverse = True)

#     # Find largest contour and surround in min area box
#     largestContour = contours[0]
#     minAreaRect = cv.minAreaRect(largestContour)

#     # Determine the angle. Convert it to the value that was originally used to obtain skewed image
#     angle = minAreaRect[-1]
#     if angle < -45:
#         angle = 90 + angle
#     return -1.0 * angle
# # Rotate the image around its center
# def rotateImage(cvImage, angle: float):
#     newImage = cvImage.copy()
#     (h, w) = newImage.shape[:2]
#     center = (w // 2, h // 2)
#     M = cv.getRotationMatrix2D(center, angle, 1.0)
#     newImage = cv.warpAffine(newImage, M, (w, h), flags=cv.INTER_CUBIC, borderMode=cv.BORDER_REPLICATE)
#     return newImage

# # Deskew image
# def deskew(cvImage):
#     angle = getSkewAngle(cvImage)
#     return rotateImage(cvImage, -1.0 * angle)

# img1=deskew(img)
# cv.imshow("Deskew Image",img1)




# # Removing Borders
# def removeBorder(img):
#     contours,heiarchy=cv.findContours(img,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
#     cntSorted=sorted(contours,key=lambda x:cv.contourArea(x))
#     cnt=cntSorted[-1]
#     x,y,w,h=cv.boundingRect(cnt)
#     crop_img=img[y:y+h,x:x+w]
#     return crop_img
# # img=removeBorder(img)
# # cv.imshow("noBorder",img)
# cv.waitKey(0)
# cv.destroyAllWindows()

# #Add A missing a border
# def addMissBorder(img):
#     color=[255,255,255]
#     top,bottom,left,right=150*4
#     img=cv.copyMakeBorder(img,top,bottom,left,right,cv.BORDER_CONSTANT,value=color)
#     return img
# text_generated=pyt.image_to_string(img)
# print(text_generated)

class All:
    def __init__(self) -> None:
        pass

    def invertImage(img):
        img_invert=cv.bitwise_not(img)
        return img_invert


#For rescalling the Image
    def rescaleImage(img,scale):
        width = int (img.shape[1] * scale/ 100 )
        height = int (img.shape[0] * scale / 100)
        dim = (width, height)
        img_Re=cv.resize(img,dim,interpolation=cv.INTER_AREA)
        return img_Re



    #For GrayScale of Image:

    def grayImage(img):
        img_Gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        return img_Gray

    # Was Not working for Binarization i.e. cv.Threshold
    def binImage(img):
        imgGray= All.grayImage(img)
        imgBinarize=cv.threshold(imgGray,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
        return imgBinarize
    # imgbin=binImage(img)
    # cv.imshow("Binary Image",imgbin[1])
    # cv.waitKey(0)
    # cv.destroyAllWindows()

    #For Reducing Noise From Image :
    # Thickening of font 
    #we use erodion
    def erodeImg(img):
        img=cv.bitwise_not(img)
        kernel=np.ones((1,1),np.uint8)
        img=cv.erode(img,kernel,iterations=1)
        return img
    # img=erodeImg(img)
    # cv.imshow("Erroded image",img)

    # for thickening the font We will use Dilation
    def imgDilate(img):
        img=cv.bitwise_not(img)
        kernel=np.ones((1,1),np.uint8)
        img=cv.dilate(img,kernel,iterations=1)
        return img
    # img=imgDilate(img)
    # cv.imshow("Dilate image",img)

    # Writing a function for rotation/deskewing
    # Calculate skew angle of an image
    def getSkewAngle(cvImage) -> float:
        # Prep image, copy, convert to gray scale, blur, and threshold
        newImage = cvImage.copy()
        gray = cv.cvtColor(newImage, cv.COLOR_BGR2GRAY)
        blur = cv.GaussianBlur(gray, (9, 9), 0)
        thresh = cv.threshold(blur, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]

        # Apply dilate to merge text into meaningful lines/paragraphs.
        # Use larger kernel on X axis to merge characters into single line, cancelling out any spaces.
        # But use smaller kernel on Y axis to separate between different blocks of text
        kernel = cv.getStructuringElement(cv.MORPH_RECT, (30, 5))
        dilate = cv.dilate(thresh, kernel, iterations=5)

        # Find all contours
        contours, hierarchy = cv.findContours(dilate, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key = cv.contourArea, reverse = True)

        # Find largest contour and surround in min area box
        largestContour = contours[0]
        minAreaRect = cv.minAreaRect(largestContour)

        # Determine the angle. Convert it to the value that was originally used to obtain skewed image
        angle = minAreaRect[-1]
        if angle < -45:
            angle = 90 + angle
        return -1.0 * angle
    # Rotate the image around its center
    def rotateImage(cvImage, angle: float):
        newImage = cvImage.copy()
        (h, w) = newImage.shape[:2]
        center = (w // 2, h // 2)
        M = cv.getRotationMatrix2D(center, angle, 1.0)
        newImage = cv.warpAffine(newImage, M, (w, h), flags=cv.INTER_CUBIC, borderMode=cv.BORDER_REPLICATE)
        return newImage

    # Deskew image
    def deskew(cvImage):
        angle = All.getSkewAngle(cvImage)
        return All.rotateImage(cvImage, -1.0 * angle)

    # img1=deskew(img)
    # cv.imshow("Deskew Image",img1)




    # Removing Borders
    def removeBorder(img):
        img=All.grayImage(img)
        contours,heiarchy=cv.findContours(img,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
        cntSorted=sorted(contours,key=lambda x:cv.contourArea(x))
        cnt=cntSorted[-1]
        x,y,w,h=cv.boundingRect(cnt)
        crop_img=img[y:y+h,x:x+w]
        return crop_img
    # img=removeBorder(img)
    # cv.imshow("noBorder",img)
    # cv.waitKey(0)
    # cv.destroyAllWindows()

    #Add A missing a border
    def addMissBorder(img):
        color=[255,255,255]
        top=bottom=left=right=150*4
        img=cv.copyMakeBorder(img,top,bottom,left,right,cv.BORDER_CONSTANT,value=color)
        return img
    
    def preprocess(img):
        # img=All.binImage(img)
        img=All.erodeImg(img)
        img=All.imgDilate(img)
        # img=All.removeBorder(img)
        # img=All.addMissBorder(img)
        return img
    
    
    def textExtract(img):
        img=All.preprocess(img)
        text_generated=pytesseract.image_to_string(img)
        return text_generated

img1=All.preprocess(img)
# cv.imshow("First Image",img1)
# cv.waitKey(0)
# cv.destroyAllWindows()
a=All.textExtract(img1)
print(a)
if a is None:
    print('No Text Found')
else:
    b=detect(a)
    print(b)