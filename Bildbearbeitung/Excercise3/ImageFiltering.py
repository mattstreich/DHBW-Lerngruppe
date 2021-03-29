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
            tmp[i,j] = int(np.round(average/(kSize*kSize)))

    #Gefilternes Bild uebertragen
    img = tmp
    return 0

# create a gaussian kernel of arbitrary size
def createGaussianKernel(kSize, stdDeviation):
    normalize = int(kSize/2)
    kernel = np.empty([kSize,kSize])

    for i in range(kSize):
        for j in range(kSize):
            kernel[i,j] = (1/(2*np.pi*np.square(stdDeviation))) * np.exp(-0.5*((np.square(i-normalize)+np.square(j-normalize))/(np.square(stdDeviation))))
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

            sobel = [[int(img[i,j]),int(img[i,j+1]),int(img[i,j+2])]
            ,[int(img[i+1,j]),int(img[i+1,j+1]),int(img[i+1,j+2])],
            [int(img[i+2,j]),int(img[i+2,j+1]),int(img[i+2,j+2])]]

            sobel = np.array(sobel)

            sobel = sobel * kernel

            sumSobel = 0

            for u in range(3):
                for v in range(3):
                    sumSobel += sobel[u,v]
            
            sumSobel = ((sumSobel/9)+255)/2

            tmp[i,j] = int(np.round(sumSobel))

    #Gefilternes Bild uebertragen
    img = tmp
    return 0


# Extra: create an integral image of the given image
def createIntegralImage(img):
    tmp = np.zeros((img.shape[0],img.shape[1]))

    for i in range(tmp.shape[0]):
        for j in range(tmp.shape[1]):
            tmp[i,j] = int(img[i,j])

    img = cv2.copyMakeBorder(
        img,
        top=1,
        bottom=1,
        left=1,
        right=1,
        borderType=cv2.BORDER_CONSTANT
    )

    tmpIMG = np.zeros((img.shape[0],img.shape[1]))

    for i in range(tmpIMG.shape[0]):
        for j in range(tmpIMG.shape[1]):
            tmpIMG[i,j] = int(img[i,j])

    for i in range(tmp.shape[0]):
        for j in range(tmp.shape[1]):
            
            sum1= 0

            sum1= int(tmpIMG[i+1,j])+int(tmpIMG[i,j+1])+int(tmp[i,j])-int(tmpIMG[i,j])
            tmpIMG[i+1,j+1] = sum1
            tmp[i,j] = sum1

    return tmp

# Extra: apply the moving average filter by using an integral image
def applyMovingAverageFilterWithIntegralImage(img, kSize):
    tmp = img

    borderSize = int(kSize/2)

    img = cv2.copyMakeBorder(
        img,
        top=borderSize+1,
        bottom=borderSize+1,
        left=borderSize+1,
        right=borderSize+1,
        borderType=cv2.BORDER_REFLECT_101
    )

    integral = createIntegralImage(img)

    for i in range(tmp.shape[0]):
        for j in range(tmp.shape[1]):

            sumIntegral = (int(integral[i,j])
            +int(integral[i+kSize,j+kSize])
            -int(integral[i,j+kSize])
            -int(integral[i+kSize,j]))

            tmp[i,j] = int(sumIntegral/np.square(kSize))

    img = tmp 

    return 0

# Extra:
def applyMovingAverageFilterWithSeperatedKernels(img, kSize):
    #temporaeres Bild zum Speicher der Ergebnisse des Filters
    tmp = img
    tmp_x = img

    borderSize = int(kSize/2)

    #Bild erweitern, damit Groesse Eingang = Groese Ausgang
    img = cv2.copyMakeBorder(
        img,
        top=0,
        bottom=0,
        left=borderSize,
        right=borderSize,
        borderType=cv2.BORDER_REFLECT_101
    )

    for i in range(tmp.shape[0]):
        for j in range(tmp.shape[1]):

            average_x = 0

            for u in range(kSize):
                average_x += img[i,j+u]
              
            tmp_x[i,j] = int(np.round((average_x)/kSize))

    tmp_x = cv2.copyMakeBorder(
        tmp_x,
        top=borderSize,
        bottom=borderSize,
        left=0,
        right=0,
        borderType=cv2.BORDER_REFLECT_101
    )

    for i in range(tmp.shape[0]):
        for j in range(tmp.shape[1]):

            average_y = 0

            for u in range(kSize):
                average_y += tmp_x[i+u,j]
              
            tmp[i,j] = int(np.round((average_y)/kSize))
    #Gefilternes Bild uebertragen

    img = tmp

    return 0