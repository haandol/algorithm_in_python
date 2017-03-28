def combination(result, L, n, r, start, depth):
    if depth == r:
        print result[:r]
    else:
        for i in range(start, n):
            result[depth] = L[i]
            combination(result, L, n, r, i+1, depth+1)


def combination2(result, L, n, r, index, i):
    if index == r:
        print result
        return
    if i >= n:
        return

    result[index] = L[i]
    combination2(result, L, n, r, index+1, i+1)

    combination2(result, L, n, r, index, i+1)


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
