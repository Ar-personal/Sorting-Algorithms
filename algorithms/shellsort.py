from colours import *
import sortfunctions as sf
import math


def shellSort(data, drawData):
    n = len(data)
    h = 1
    while h < n/3:
        h = 3*h + 1
    while h >= 1:
        for i in range(h, n):
            j = i
            while j >= h and sf.less(data[j], data[j - h]) > 0:
                sf.exchange(data, j, j - h)
                j -= h
                drawData(data, [YELLOW if x == j or x == j - h else BLUE for x in range(len(data))])
        h = int(h / 3)
    drawData(data, [BLUE for x in range(len(data))])