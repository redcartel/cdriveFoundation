from random import randint

values = [randint(1,1000000) for _ in range(10000)]

def selection_sort(vals):
    sorted_list = []
    while len(vals):
        index = 0
        _min = vals[0]
        for i in range(len(vals)):
            if _min == None or vals[i] < _min:
                _min = vals[i]
                index = i
        sorted_list.append(vals.pop(index))
        print(sorted_list, vals)
    vals[:] = sorted_list

def bubble_sort(vals):
    for stop in range(len(vals),1,-1):
        for i in range(0, stop-1):
            if vals[i] > vals[i+1]:
                vals[i], vals[i+1] = vals[i+1], vals[i]
                print(vals, i, i+1)

def binary_search(vals, value):
    length = len(vals)
    start = 0
    stop = length
    while stop - start > 1:
        index = (stop - start) // 2 + start
        print(vals[start], vals[stop])
        if vals[index] == value:
            return index
        elif vals[index] < value:
            start = index
        else:
            stop = index
    print(vals[start], vals[stop])
    if vals[start] == value:
        return start
    if vals[stop] == value:
        return stop
    return None
