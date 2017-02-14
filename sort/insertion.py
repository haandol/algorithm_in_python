# https://interactivepython.org/runestone/static/pythonds/SortSearch/TheInsertionSort.html

def sort(L):
    n = len(L)
    for i in xrange(1, n):
        for j in xrange(i+1):
            if L[i] <= L[j]:
                break
        item = L.pop(i)
        L.insert(j, item)


if '__main__' == __name__:
    L = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    sort(L)
    assert L == sorted(L)
