def combination(result, L, n, r, start, picked):
    if picked == r:
        print result[:r]
    else:
        for i in range(start, n):
            result[picked] = L[i]
            combination(result, L, n, r, i+1, picked+1)


def combination2(result, L, n, r, picked, index):
    if picked == r:
        print result
        return
    if index >= n:
        return

    result[picked] = L[index]
    combination2(result, L, n, r, picked+1, index+1)

    combination2(result, L, n, r, picked, index+1)


def solution(L, r):
    n = len(L)
    result = [0] * r
    combination(result, L, n, r, 0, 0)


def solution2(L, r):
    n = len(L)
    result = [0] * r
    combination2(result, L, n, r, 0, 0)


solution([1, 2, 3, 4, 5], 2)
print
solution2([1, 2, 3, 4, 5], 2)
