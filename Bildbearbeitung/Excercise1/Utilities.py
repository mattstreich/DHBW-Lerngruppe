import cv2
from matplotlib import pyplot as plt


def showHistogram(img):
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        histr = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(histr, color=col)
        plt.xlim([0, 256])
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
