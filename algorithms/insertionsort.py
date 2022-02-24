import time

from colours import *
import sortfunctions as sf


def insertionSort(data, drawData):
    n = len(data)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if j > 0 and sf.less(data[j], data[j-1]) > 0:
                sf.exchange(data, j, j-1)
                drawData(data, [YELLOW if x == j or x == j - 1 else BLUE for x in range(len(data))])
    drawData(data, [BLUE for x in range(len(data))])