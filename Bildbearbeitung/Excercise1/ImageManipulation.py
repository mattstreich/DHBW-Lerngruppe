import cv2
import numpy as np

# Example for basic pixel based image manipulation:
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_core/py_basic_ops/py_basic_ops.html

# Task 1:
# Implement some kind of noticeable image manipulation in this function
# e.g. channel manipulation, filter you already know, drawings on the image etc.
def myFirstImageManipulation(img):

    #show initial picture
    cv2.imshow('Original Picture', img)

    #creating a image to transform and flipping the image
    transImg = cv2.flip(img, 0)
    
    #convert the image into a black and white image with to channels
    transImg = cv2.cvtColor(transImg,cv2.COLOR_BGR2GRAY)
    #converts the image back to 3 channels (will keep the bw look)
    transImg = cv2.cvtColor(transImg,cv2.COLOR_GRAY2BGR)
    #creating an red image in the size of the original image
    red_img  = np.full(transImg.shape, (0,0,255), np.uint8)
    #add the red image to the bw image
    transImg = cv2.add(transImg,red_img)
    
    #show transformed picture
    cv2.imshow("Transformed Picture", transImg)
    cv2.waitKey(0)

    #save the transformed picture
    cv2.imwrite("./Trans.jpg", transImg)
    return 0



# Extra:    Print the basic image properties to the console:
#           width, height, number of channels, number of pixels, pixel type,
#           the color of the first pixel of the image,
#           Color of the first pixel in the second row
#           Color of the first pixel in the second column
#           This function should work for color and for grayscale images
def printImageDetails(pic):

    picMetaData = [1,1,1]
    
    for i in range(0,len(np.array(pic.shape)-1)):
       picMetaData[i]=pic.shape[i]

    #for maintainability and overview first the output values are stored in variable
    height = picMetaData[0]
    width = picMetaData[1]
    channels = picMetaData[2]

    nPixels = pic.size
    pixelType = pic.dtype

    color1pixel = pic[0,0]
    color1pixel2row = pic[1,0]
    color1pixel2col = pic[0,1]
    

    print('Image Height       : ',height)
    print('Image Width        : ',width)
    print('Number of Channels : ',channels)
    print('Number of Pixels   : ',nPixels)
    print('Type of Pixel      : ',pixelType)
    print('Color of the Pixel : ',color1pixel)
    print('Color 1st Pixel 2R : ',color1pixel2row)
    print('Color 1st Pixel 2C : ',color1pixel2col)
    print('---------------------')

    return 0

