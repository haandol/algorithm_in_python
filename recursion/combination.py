def combination(result, L, n, r, start, depth):
    if depth == r:
        print result[:r]
    else:
        for i in range(start, n):
            result[depth] = L[i]
            combination(result, L, n, r, i+1, depth+1)


def solution(L, r):
    n = len(L)
    result = [0] * n
    combination(result, L, n, r, 0, 0)


solution([1, 2, 3, 4, 5], 2)
