# https://interactivepython.org/runestone/static/pythonds/SortSearch/TheBinarySearch.html#analysis-of-binary-search


def binsearch(L, target, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if L[mid] == target:
        return mid
    elif L[mid] < target:
        return binsearch(L, target, mid+1, end)
    elif target < L[mid]:
        return binsearch(L, target, start, mid-1)


def search(L, target):
    n = len(L)
    return binsearch(L, target, 0, n)


if '__main__' == __name__:
    L = [0, 1, 3, 5, 6, 7, 10, 13, 39]
    print search(L, 0)
    print search(L, 2)
    print search(L, 5)
    print search(L, 39)
