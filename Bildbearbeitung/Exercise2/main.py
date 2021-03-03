import cv2
import HistogramManipulation as HM
import Utilities

# Press the green button in the gutter to run the script.
# Task 1:
# implement a function that stretches a grayscale image
#
# Task 2
# implement a function that equalizes a grayscale image
#
# Small hint: use the functions in Utilities
# def plotHistogramVector(histogram) to im visualize the histogram vector

# Extra:
# 1. implement the following point operator functions on grayscale images:
#    logarithm, exponential function, inverse, threshold
# 2. implement a function to remove the gaps in the histogram of a
#    stretched/ equalized image
# make sure to prevent pixel overflows or negative pixel values

if __name__ == '__main__':
    # Aufgabe 1: Bild laden und in Graubild
    img = cv2.imread("./SampleData/redCar.jpg",1)
    imgBW = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # Aufgabe 2: Bild anzeigen
    cv2.imshow("Aufgabe 2 Bild anzeigen", imgBW)
    
    # Aufgabe 3: Histogramm anzeigen
    Utilities.showHistogram(imgBW)
    cv2.waitKey(0)

    # Aufgabe 4: stretchHistogram auf Bild anwenden
    stretchedImg = HM.stretchHistogram(imgBW)

    cv2.imshow("Image", stretchedImg)
    Utilities.showHistogram(stretchedImg)
    cv2.waitKey(0)

    # Aufgabe 5: Histogram und Bild speichern
    Utilities.saveHistogram(stretchedImg, "Histogram_Stretched_Image")
    cv2.imwrite("./Output/stretchedImage.jpg", stretchedImg)

    # Aufgabe 6: equalizeHistogram auf Bild anwenden
    equalizedImg = HM.equalizeHistogram(imgBW)

    cv2.imshow("Image", equalizedImg)
    Utilities.showHistogram(equalizedImg)
    cv2.waitKey(0)

    # Aufgabe 7: Histogram und Bild speichern
    Utilities.saveHistogram(equalizedImg, "Histogram_Equalized_Image")
    cv2.imwrite("./Output/equalizedImgage.jpg", equalizedImg)