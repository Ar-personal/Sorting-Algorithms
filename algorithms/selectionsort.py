from colours import *
import sortfunctions as sf


def selectionSort(data, drawData):
    n = len(data)
    for i in range(0, n):
        min = i
        j = i + 1
        while j < n:
            if sf.less(data[j], data[min]):
                sf.exchange(data, i, min)
                drawData(data, [YELLOW if x == j or x == j + 1 else BLUE for x in range(len(data))])
    drawData(data, [BLUE for x in range(len(data))])