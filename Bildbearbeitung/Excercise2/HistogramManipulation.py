import cv2
import numpy as np
import Utilities

# function to apply a look-up table onto an image
def applyLUT(img, LUT):
    result = img.copy()

    return result

# function to equalize a grayscale image
def equalizeHistogram(img):
    result = img.copy()

    result_L = 256
    result_N = result.size

    result_hist = cv2.calcHist([result],[0], None, [result_L], [0,result_L])
    result_integral = result_hist.cumsum()

    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            result[i,j] = ((result_L-1)/result_N)*result_integral[result[i,j]]

    print("Histogram equalized")
    return result

# function to stretch a grayscale image
def stretchHistogram(img):
    result = img.copy()

    result_min = np.min(result)
    result_max = np.max(result)
    result_L = 256

    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            result[i,j] = ((result[i,j] - result_min) / (result_max - result_min)) * (result_L - 1)

    print("Histogram stretched")
    return result

#function logHistogram
def logHistogram(img):
    result = img.copy()

    result_a = 255 / np.log(255)

    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            result[i,j] = result_a * np.log(result[i,j] + 1)

    return result

#function expHistogram
def expHistogram(img):
    result = img.copy()

    result_a = 255 / np.exp(255/255)

    #print(np.exp(256))
    #print(256 / np.exp(256))

    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            result[i,j] = result_a * np.exp(result[i,j]/255 - 1)

    return result

#function Inverse
def inverseHistogram(img):

    result = img.copy()

    result_max = 256 - 1

    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            result[i,j] = result_max - result[i,j]

    return result

#function Threshold
def tresholdHistogram(img):

    result = img.copy()

    result_threshold = 255 / 2 

    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            if result [i,j] < result_threshold:
                result [i,j] = 0
            else:
                result [i,j] = 255

    return result

#function closeGapsHistogram
def closeGapsHistogram(img):

    result = img.copy()

    return result

# function to create a vector containing the histogram
def calculateHistogram(img, nrBins):

    histogram = np.zeros([nrBins], dtype=np.int)

    return histogram



