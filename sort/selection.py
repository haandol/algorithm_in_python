# https://interactivepython.org/runestone/static/pythonds/SortSearch/TheSelectionSort.html


def sort(L):
    n = len(L)
    for slot_pos in xrange(n-1, -1, -1):
        max_pos = slot_pos
        for j in xrange(slot_pos):
            if L[max_pos] < L[j]:
                max_pos = j

        L[max_pos], L[slot_pos] = L[slot_pos], L[max_pos]


if '__main__' == __name__:
    L = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
    sort(L)
    print L
    assert L == sorted(L)
