# https://interactivepython.org/runestone/static/pythonds/SortSearch/TheQuickSort.html


def sort(L):
    '''you can extract partition method for efficiency'''
    n = len(L)
    if n < 2:
        return L

    pivotmark = n - 1
    pivot = L[pivotmark]
    leftmark = 0
    rightmark = pivotmark - 1
    while leftmark <= rightmark:
        if L[rightmark] < pivot < L[leftmark]:
            L[leftmark], L[rightmark] = L[rightmark], L[leftmark]
            leftmark += 1
            rightmark -= 1
        elif pivot < L[rightmark]:
            rightmark -= 1
        elif L[leftmark] <= pivot:
            leftmark += 1

    L[leftmark], L[pivotmark] = L[pivotmark], L[leftmark]

    left = sort(L[:leftmark])
    right = sort(L[leftmark:])

    return left + right


def sort2(L):
    '''simple and intuitive but inefficient'''
    if len(L) < 2:
        return L

    pivot = L[0]

    left = [el for el in L if el < pivot]
    mid = [el for el in L if el == pivot]
    right = [el for el in L if el > pivot]

    return sort(left) + mid + sort(right)


if '__main__' == __name__:
    L = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    L2 = sort(L)
    assert L2 == sorted(L)
