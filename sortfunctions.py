def less(b, a):
    if a < b:
        return -1
    if a==b:
        return 0
    if a > b:
        return 1


def exchange(data, a, b):
    t = data[a]
    data[a] = data[b]
    data[b] = t