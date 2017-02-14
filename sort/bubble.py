# https://interactivepython.org/runestone/static/pythonds/SortSearch/TheBubbleSort.html

def sort(L):
    n = len(L)
    for i in range(n-1, -1, -1):
        for j in range(i):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]


L = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
sort(L)
assert L == sorted(L)
