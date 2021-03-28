import cv2
import ImageFiltering as IF
import numpy as np
from datetime import datetime
from matplotlib import pyplot as plt
import Utilities


if __name__ == '__main__':
    # load image and apply filters
    # choose some sort of border handling that keeps the size of the processed image

    #landen des Bildes und umwandeln in schwarz/weiss
    img = cv2.imread("./SampleData/redCar.jpg",1)
    imgBW = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    #Schwarz/Weiss Bild zeigen und speichern
    cv2.imshow("Schwarz/Weiss", imgBW)
    cv2.imwrite("./Output/BlackWhiteImage.jpg", imgBW)

    Utilities.showHistogram(imgBW)
    cv2.waitKey(0)
    Utilities.saveHistogram(imgBW, "Histogram_BW_Image")

    #Moving Average Bild Erstellen
    imgMovingAverage = imgBW.copy()
    IF.applyMovingAverageFilter(imgMovingAverage, 5)

    #Moving Average Bild zeigen und speichern
    cv2.imshow("Moving Average", imgMovingAverage)
    cv2.imwrite("./Output/MovingAverageImage.jpg", imgMovingAverage)

    Utilities.showHistogram(imgMovingAverage)
    cv2.waitKey(0)
    Utilities.saveHistogram(imgMovingAverage, "Histogram_MovingAverage_Image")

    #Gauss Bild Erstellen
    imgGauss = imgBW.copy()
    IF.applyGaussFilter(imgGauss, 5, 1)

    #Gauss Bild zeigen und speichern
    cv2.imshow("Gauss", imgMovingAverage)
    cv2.imwrite("./Output/GaussImage.jpg", imgGauss)

    Utilities.showHistogram(imgGauss)
    cv2.waitKey(0)
    Utilities.saveHistogram(imgGauss, "Histogram_Gauss_Image")

    #Sobel Kernel erstellen
    xKernel = IF.createSobelXKernel()
    yKernel = IF.createSobelYKernel()

    #Sobel Bilder Erstellung
    imgXSobel = imgBW.copy()
    imgYSobel = imgBW.copy()
    IF.applyKernelInSpatialDomain(imgXSobel, xKernel)
    IF.applyKernelInSpatialDomain(imgYSobel, yKernel)

    #Sobel Bilder zeigen und speichern
    cv2.imshow("XSobel", imgXSobel)
    cv2.imwrite("./Output/XSobelImage.jpg", imgXSobel)

    Utilities.showHistogram(imgXSobel)
    cv2.waitKey(0)
    Utilities.saveHistogram(imgXSobel, "Histogram_XSobel_Image")

    cv2.imshow("YSobel", imgYSobel)
    cv2.imwrite("./Output/YSobelImage.jpg", imgYSobel)

    Utilities.showHistogram(imgYSobel)
    cv2.waitKey(0)
    Utilities.saveHistogram(imgYSobel, "Histogram_YSobel_Image")

    #Median Bild Erstellung
    imgMedian = imgBW.copy()
    IF.applyMedianFilter(imgMedian, 5)

    #Median Bild zeigen und speichern
    cv2.imshow("Median", imgMedian)
    cv2.imwrite("./Output/MedianImage.jpg", imgMedian)

    Utilities.showHistogram(imgMedian)
    cv2.waitKey(0)
    Utilities.saveHistogram(imgMedian, "Histogram_Median_Image")

    #Moving Average Seperate Kernel Bild Erstellung
    imgMASeperatedKernel = imgBW.copy()
    IF.applyMovingAverageFilterWithSeperatedKernels(imgMASeperatedKernel, 5)

    #Moving Average Seperate Kernel zeigen und speichern
    cv2.imshow("Moving Average Seperated Kernel", imgMASeperatedKernel)
    cv2.imwrite("./Output/MovingAverageSeperatedKernelImage.jpg", imgMASeperatedKernel)
    
    Utilities.showHistogram(imgMASeperatedKernel)
    cv2.waitKey(0)
    Utilities.saveHistogram(imgMASeperatedKernel, "Histogram_Sep_Kernel_Image")

    #Moving Average Integral Bild Erstellung
    imgMAIntegral = imgBW.copy()
    IF.applyMovingAverageFilterWithIntegralImage(imgMAIntegral, 5)

    #Moving Average Seperate Kernel zeigen und speichern
    cv2.imshow("Moving Average Integral", imgMAIntegral)
    cv2.imwrite("./Output/MovingAverageIntegralImage.jpg", imgMAIntegral)

    Utilities.showHistogram(imgMAIntegral)
    cv2.waitKey(0)
    Utilities.saveHistogram(imgMAIntegral, "Histogram_Integral_Image")

    #Zeitmessen 
    x_min = 3
    x_max = 9

    x = np.arange(x_min,x_max,2)
    
    y_MA_Filter = np.zeros(x.shape)
    y_MA_Seperate = np.zeros(x.shape)
    y_MA_Intergral = np.zeros(x.shape)

    imgTime = imgBW.copy()

    for i in range(x.shape[0]):
        kSize = x[i]

        before = datetime.now()
        IF.applyMovingAverageFilter(imgTime, kSize)
        after = datetime.now()
        td = after - before
        y_MA_Filter[i] = td.total_seconds()

        before = datetime.now()
        IF.applyMovingAverageFilterWithSeperatedKernels(imgTime, kSize)
        after = datetime.now()
        td = after - before
        y_MA_Seperate[i] = td.total_seconds()

        before = datetime.now()
        IF.applyMovingAverageFilterWithIntegralImage(imgTime, kSize)
        after = datetime.now()
        td = after - before
        y_MA_Intergral[i] = td.total_seconds()

    fig = plt.figure()

    ax = fig.add_subplot()

    fig.suptitle('Zeitmessung bei verschiedenen Implementionen von Moving Average', fontsize=14, fontweight='bold')

    ax.set_xlabel("Kernel Größe")
    ax.set_ylabel("Dauer in Sekunden")

    filter_plot = ax.plot(x,y_MA_Filter, label='Filter')
    seperate_plot = ax.plot(x,y_MA_Seperate, label='Seperate Kernel')
    intergral_plot = ax.plot(x,y_MA_Intergral, label='Integral')

    ax.legend()

    plt.show()

    fig.savefig('./Output/Zeitmessen.jpg')

    cv2.waitKey(0)