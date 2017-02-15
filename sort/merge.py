# https://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html


def _merge(left, right):
    n = len(left)
    m = len(right)
    i = 0
    j = 0
    L = []

    while i < n and j < m:
        if left[i] <= right[j]:
            L.append(left[i])
            i += 1
        else:
            L.append(right[j])
            j += 1

    if i == n:
        for k in xrange(j, m):
            L.append(right[k])
    elif j == m:
        for k in xrange(i, n):
            L.append(left[k])
    return L


def _merge2(left, right):
    '''more simple and intuitive but inefficient'''
    L = []
    while left and right:
        if left[0] <= right[0]:
            L.append(left.pop(0))
        else:
            L.append(right.pop(0))

    if left:
        L.extend(left)
    elif right:
        L.extend(right)

    return L


def sort(L):
    if len(L) < 2:
        return L

    n = len(L)
    m = n / 2
    left = L[:m]
    right = L[m:]

    return _merge2(sort(left), sort(right))


if '__main__' == __name__:
    L = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    L2 = sort(L)
    assert L2 == sorted(L)
