import cv2 as cv


img=cv.imread('aero3.jpg')
cv.imshow("First Image",img)
cv.waitKey(0)
cv.destroyAllWindows()


# Creating the Different function for Different functionality


# Adding Different Functionalities 


#For inverting the image Function:
def invertImage(img):
    img_invert=cv.bitwise_not(img)
    return img_invert
#Testing the Image
# img_in=invertImage(img)
# cv.imshow("Inverted Image",img_in)
# cv.waitKey(0)
# cv.destroyAllWindows()

#For rescalling the Image
def rescaleImage(img,scale):
    width = int (img.shape[1] * scale/ 100 )
    height = int (img.shape[0] * scale / 100)
    dim = (width, height)
    img_Re=cv.resize(img,dim,interpolation=cv.INTER_AREA)
    return img_Re

#For Testing The Function
# img_resi=rescaleImage(img,75)
# cv.imshow("Rescaled Image",img_resi)
# cv.waitKey(0)
# cv.destroyAllWindows()

#For GrayScale of Image:

def grayImage(img):
    img_Gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    return img_Gray
#For testing the Functionality:

# imgBin=grayImage(img);
# cv.imshow("Gray Image",imgBin)
# cv.waitKey(0)
# cv.destroyAllWindows()
# Was Not working for Binarization i.e. cv.Threshold
def binImage(img):
    imgGray= grayImage(img)
    imgBinarize=cv.threshold(imgGray,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    return imgBinarize
imgBinarize=binImage(img)
cv.imshow("Binary Image",imgBinarize[1])
cv.waitKey(0)
cv.destroyAllWindows()