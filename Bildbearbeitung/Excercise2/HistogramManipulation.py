import cv2
import numpy as np
import Utilities
import random

# function to apply a look-up table onto an image
def applyLUT(img, LUT):
    result = img.copy()

    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            result[i,j] = LUT[result[i,j]]

    return result

# function to equalize a grayscale image
def equalizeHistogram(img):
    result = img.copy()

    result_L = 256
    result_N = result.size

    result_hist = cv2.calcHist([result],[0], None, [result_L], [0,result_L])
    result_integral = result_hist.cumsum()

    result_LUT = np.arange(256)
    
    for i in range(result_LUT.size):
        result_LUT[i] = ((result_L-1)/result_N)*result_integral[result_LUT[i]]

    return applyLUT(result, result_LUT)

# function to stretch a grayscale image
def stretchHistogram(img):
    result = img.copy()

    result_min = np.min(result)
    result_max = np.max(result)
    result_L = 256

    result_LUT = np.arange(256)
    
    for i in range(result_LUT.size):
        result_LUT[i] = ((result_LUT[i] - result_min) / (result_max - result_min)) * (result_L - 1)

    return applyLUT(result, result_LUT)

#function logHistogram
def logHistogram(img):
    result = img.copy()

    result_a = 255 / np.log(255)

    result_LUT = np.arange(256)
    
    for i in range(result_LUT.size):
        result_LUT[i] = result_a * np.log(result_LUT[i] + 1)

    return applyLUT(result, result_LUT)

#function expHistogram
def expHistogram(img):
    result = img.copy()

    result_a = 255 / np.exp(255/255)

    #print(np.exp(255))
    #print(255 / np.exp(255))

    result_LUT = np.arange(256)
    
    for i in range(result_LUT.size):
        result_LUT[i] = result_a * np.exp(result_LUT[i]/255 - 1)

    return applyLUT(result, result_LUT)

#function Inverse
def inverseHistogram(img):

    result = img.copy()

    result_max = 256 - 1

    result_LUT = np.arange(256)
    
    for i in range(result_LUT.size):
        result_LUT[i] = result_max - result_LUT[i]

    return applyLUT(result, result_LUT)

#function Threshold
def tresholdHistogram(img):

    result = img.copy()

    result_threshold = 255 / 2 

    result_LUT = np.arange(256)
    
    for i in range(result_LUT.size):
        if result_LUT[i] < result_threshold:
            result_LUT[i] = 0
        else:
            result_LUT[i] = 255

    return applyLUT(result, result_LUT)

#function closeGapsHistogram
def closeGapsHistogram(img):

    result = img.copy()
    
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            if result[i,j] >= 4 and result[i,j] <=251:
                result[i,j] = result[i,j] + random.random()*10 - 5

    return result

# function to create a vector containing the histogram
def calculateHistogram(img, nrBins):

    histogram = np.zeros([nrBins], dtype=np.int)

    return histogram



