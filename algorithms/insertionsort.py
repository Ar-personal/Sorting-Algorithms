import time

from colours import *
import sortfunctions as sf


def insertionSort(data, drawData, timeTick):
    n = len(data)
    for i in range(1, n):
        for k in range(i, 0, -1):
            j = k
            if j > 0 and j > sf.less(data[j], data[j-1]):
                sf.exchange(data, j, j-1)
                drawData(data, [YELLOW if x == j or x == j - 1 else BLUE for x in range(len(data))])
                time.sleep(timeTick)
    drawData(data, [BLUE for x in range(len(data))])