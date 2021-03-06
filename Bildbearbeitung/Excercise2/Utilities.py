import cv2
from matplotlib import pyplot as plt


def showHistogram(img):
    color = ('b', 'g', 'r')
    if len(img.shape) == 2:
        color = ('b')
    plt.close()
    for i, col in enumerate(color):
        histr = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(histr, color=col)
        plt.xlim([0, 256])
    plt.show()

def plotHistogramVector(histogram):
    plt.plot(histogram, color='b')
    plt.xlim([0, len(histogram)])
    plt.show()

def grabWebcam():
    cap = cv2.VideoCapture(0)
    while True:
        ret, im = cap.read()
        cv2.imshow('video test', im)
        key = cv2.waitKey(10)
        if key == 27:
            break
        # if key == ord(' '):
        # cv2.imwrite('vid_result.jpg',im)

def saveHistogram(img,filename):
    color = ('b', 'g', 'r')
    if len(img.shape) == 2:
        color = ('b')
    plt.close()
    for i, col in enumerate(color):
        histr = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(histr, color=col)
        plt.xlim([0, 256])
    plt.savefig('./Output/' + filename + '.jpg')