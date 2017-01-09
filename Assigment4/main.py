
import sys
import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as mplot

class ImageAnalysis():
    def __init__(self, threshold):
        self.threshold = threshold
        self.images = self.getImages()
        self.avgPic = self.getAvgImage()
        self.diffPic = self.getDiffImage()

    def getImages(self):
        f_list = os.listdir('.')
        images = []
        for pic in f_list:
            if pic[-3:] == 'jpg':
                pic = Image.open(pic)
                images.append(np.float32(pic))
        return images

    def getAvgImage(self):
        avg = 0
        for pic in self.images:
            avg += pic
        return avg/len(self.images)

    def getDiffImage(self):
        diff = 0
        for i in range(1, len(self.images)):
            diff += abs(self.images[i] - self.images[i-1])
        return diff/(len(self.images)-1)

    def getAvgDiffImage(self):
        for row in range(len(self.avgPic)):
            for col in range(len(self.avgPic[0])):
                r = sum(self.diffPic[row][col])/(sum(self.avgPic[row][col]))
                if r > self.threshold:
                    self.avgPic[row][col] = [255,0,0]

    def plot(self):
        avg_img=np.clip(self.avgPic, 0, 255)
        avg_img=np.uint8(avg_img)
        mplot.imshow(avg_img)
        mplot.show()


def main():
    if len(sys.argv) != 2:
        print '2 arguments are expected  <main.py> <threshold>'
        sys.exit()
    try:
        threshold = float(sys.argv[1])
    except ValueError:
        print "Not a float"
        sys.exit()
    if 0 <= threshold <= 1:
        IA = ImageAnalysis(threshold)
        IA.getAvgDiffImage()
        IA.plot()
    else:
        print "threshold should be between 0 and 1"




if __name__ == '__main__':
    main()
