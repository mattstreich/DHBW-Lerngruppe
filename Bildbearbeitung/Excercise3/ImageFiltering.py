import numpy as np
import cv2



# apply median filter
def applyMedianFilter(img, kSize):
    #temporaeres Bild zum Speicher der Ergebnisse des Filters
    tmp = img

    borderSize = int(kSize/2)

    #Bild erweitern, damit Groesse Eingang = Groese Ausgang
    img = cv2.copyMakeBorder(
        img,
        top=borderSize,
        bottom=borderSize,
        left=borderSize,
        right=borderSize,
        borderType=cv2.BORDER_REFLECT_101
    )

    #Position des Medians
    median_pos = int(kSize / 2)

    for i in range(tmp.shape[0]):
        for j in range(tmp.shape[1]):
            
            median = []
            #Filter fuellen

            for u in range(kSize):
                for v in range(kSize):
                    median.append(img[i+u,j+v])

            #calculieren des medians
            median.sort()
            #median uertragen
            tmp[i,j] = median[median_pos]

    #Gefilternes Bild uebertragen
    img = tmp

    return 0

# create a moving average kernel of arbitrary size
def applyMovingAverageFilter(img, kSize):

    #temporaeres Bild zum Speicher der Ergebnisse des Filters
    tmp = img
 
    borderSize = int(kSize/2)

    #Bild erweitern, damit Groesse Eingang = Groese Ausgang
    img = cv2.copyMakeBorder(
        img,
        top=borderSize,
        bottom=borderSize,
        left=borderSize,
        right=borderSize,
        borderType=cv2.BORDER_REFLECT_101
    )

    for i in range(tmp.shape[0]):
        for j in range(tmp.shape[1]):
            
            average = 0 

            for u in range(kSize):
                for v in range(kSize):
                    average += img[i+u,j+v]


            #median uertragen
            tmp[i,j] = int(average/(kSize*kSize))

    #Gefilternes Bild uebertragen
    img = tmp
    return 0

# create a gaussian kernel of arbitrary size
def createGaussianKernel(kSize, stdDeviation):

    kernel = np.empty([kSize,kSize])

    for i in range(kSize):
        for j in range(kSize):
            kernel[i,j] = ( 1/(np.sqrt(2 * np.pi)) ) * np.exp(-((np.square(i)+np.square(j))/(2*stdDeviation)))

    return kernel

def applyGaussFilter(img, kSize, stdDeviation):
    #temporaeres Bild zum Speicher der Ergebnisse des Filters
    tmp = img

    borderSize = int(kSize/2)

    #Bild erweitern, damit Groesse Eingang = Groese Ausgang
    img = cv2.copyMakeBorder(
        img,
        top=borderSize,
        bottom=borderSize,
        left=borderSize,
        right=borderSize,
        borderType=cv2.BORDER_REFLECT_101
    )

    gausskernel = createGaussianKernel(kSize,stdDeviation)

    for i in range(tmp.shape[0]):
        for j in range(tmp.shape[1]):

            gauss = 0

            for u in range(kSize):
                for v in range(kSize):
                    gauss += img[i+u,j+v] * gausskernel[u,v]

            tmp[i,j] = int(np.round(gauss))

    #Gefilternes Bild uebertragen
    img = tmp

    return 0

# create a kernel of size 3x3
def createSobelXKernel():

    kernel = [[1,0,-1],[2,0,-2],[1,0,-1]]
    kernel = np.array(kernel)

    return kernel

# create a kernel of size 3x3
def createSobelYKernel():

    kernel = [[1,2,1],[0,0,0],[-1,-2,-1]]
    kernel = np.array(kernel)

    return kernel

def applyKernelInSpatialDomain(img, kernel):
    #temporaeres Bild zum Speicher der Ergebnisse des Filters
    tmp = img


    #Bild erweitern, damit Groesse Eingang = Groese Ausgang
    img = cv2.copyMakeBorder(
        img,
        top=1,
        bottom=1,
        left=1,
        right=1,
        borderType=cv2.BORDER_REFLECT_101
    )

    for i in range(tmp.shape[0]):
        for j in range(tmp.shape[1]):

            sobel = 0

            for u in range(3):
                for v in range(3):
                    sobel += img[i+u,j+v] * kernel[2-u,2-v]

            tmp[i,j] = int(np.round(sobel))

    #Gefilternes Bild uebertragen
    img = tmp
    return 0


# Extra: create an integral image of the given image
def createIntegralImage(img):
    tmp = img

    tmp = np.cumsum(tmp)

    img=tmp

    return 0

# Extra: apply the moving average filter by using an integral image
def applyMovingAverageFilterWithIntegralImage(img, kSize):
    tmp = img

    borderSize = int(kSize/2)

    img = cv2.copyMakeBorder(
        img,
        top=borderSize,
        bottom=borderSize,
        left=borderSize,
        right=borderSize,
        borderType=cv2.BORDER_REFLECT_101
    )

    integral, integralsq = cv2.integral2(img)

    createIntegralImage(integral)

    total_pixel = np.square(kSize*2+1)

    for i in range(tmp.shape[0]):
        for j in range(tmp.shape[1]):
            s1 = (int(integral[i+kSize,j+kSize])
            +int(integral[i-kSize,j-kSize])
            -int(integral[i+kSize,j-kSize])
            -int(integral[i-kSize,j+kSize]))

            s2 = (int(integralsq[i+kSize,j+kSize])
            +int(integralsq[i-kSize,j-kSize])
            -int(integralsq[i+kSize,j-kSize])
            -int(integralsq[i-kSize,j+kSize]))

            std = (s2 - (np.square(s1))/total_pixel)/total_pixel
            
            if(std < 0): 
                std = 0

            std = np.sqrt(std)

            tmp[i,j] = int(std)

    img = tmp 

    return 0

# Extra:
def applyMovingAverageFilterWithSeperatedKernels(img, kSize):
    #temporaeres Bild zum Speicher der Ergebnisse des Filters
    tmp = img

    borderSize = int(kSize/2)

    #Bild erweitern, damit Groesse Eingang = Groese Ausgang
    img = cv2.copyMakeBorder(
        img,
        top=borderSize,
        bottom=borderSize,
        left=borderSize,
        right=borderSize,
        borderType=cv2.BORDER_REFLECT_101
    )

    for i in range(tmp.shape[0]):
        for j in range(tmp.shape[1]):

            average_x = 0
            average_y = 0

            for u in range(kSize):
                average_x += img[i,j+u]

            for u in range(kSize):
                average_y += img[i+u,j]

            tmp[i,j] = int((average_x + average_y)/(2*kSize))

    #Gefilternes Bild uebertragen

    img = tmp
    return 0