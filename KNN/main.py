'''
    Spirit Animal: generousIbex
    Date:          19/10/16
    Challenge #:   5
    Sources:
            - Dr. Jones Lecture
            - http://www.cs.olemiss.edu/~jones/doku.php?id=csci343_nearest_neighbors
'''


import os, os.path, time
import matplotlib.pyplot as mplot
from PIL import Image
import numpy as np
import math
import sys


def getKNeighbors(k, reconstruc):
    dist = lambda a,b:  math.sqrt(math.pow(a[0]-b[0],2)+math.pow(a[1]-b[1],2))
    green = [0, 255, 0, 255]
    reference = np.float32(Image.open('data.png'))
    rc = np.float32(reconstruc)

    '''
        Get all points from the reference image that are green and
        append the coordinates into the rf_coor (reference coordinates) list
    '''
    rf_coor = []
    for row in range(len(reference)):
        for col, pixel in enumerate(reference[row]):
            if not(pixel == green).all():
                rf_coor.append([row, col])

    '''
        This is where the magic happens.
        1.- Iterate through all the points in the reference image
            and find the ones that are green
        2.- If the pixel is green, then do as follow:
            - Find the dist from the pixel coordinates to all the points in
              our rf_coor list. Store the value and list coor in a tuple.
            - Sort the tuple by the distance value
            - Use a list slicing to only keep the k values of the list
        3.- Get the average of all the pixels in k_neighbors array by
            calling back the reference image to get the actual pixel values.
            Numpy average will do it for you.
        4.- Set the new value in the corresponding coordinates
    '''

    for row in range(len(rc)):
        for col, pixel in enumerate(rc[row]):
            if (pixel == green).all():
                k_neighbors = sorted([(dist([row, col], coor), rf_coor[x]) for x, \
                                       coor in enumerate(rf_coor)])[:k]
                rc[row][col] = np.average([reference[p[0]][p[1]] for i, p \
                                 in k_neighbors], axis=0)

    k_img=np.clip(rc, 0, 255)
    k_img=np.uint8(k_img)
    mplot.imshow(k_img)
    mplot.show(block=True)
    mplot.imsave('{}-neigboors.png'.format(k), k_img)


def main():
    if  len(sys.argv) != 3:
        print 'Should have two parameters: <k_neighbors> <file_name>'
        exit()
    try:
        k = int(sys.argv[1])
        if k < 1:
            print 'K value should be more than one'
            sys.exit()
    except ValueError:
        print "Not a int Value"
        sys.exit()

    try:
        reconstruc = Image.open(sys.argv[2])
    except FileNotFoundError:
        print "File does not exists"
        sys.exit()
    getKNeighbors(k, reconstruc)

if __name__ == '__main__':
    import timeit
    print 'Execution time:'
    print('\t' + str(timeit.timeit("main()", setup="from __main__ import main", number=1)))
