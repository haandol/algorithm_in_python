# https://www.interviewbit.com/problems/min-sum-path-in-matrix/


def solution(L):
    n = len(L)
    m = len(L[0])
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                L[i][j] += L[i][j-1]
            elif j == 0:
                L[i][j] += L[i-1][j]
            else:
                L[i][j] += min(L[i][j-1], L[i-1][j])

    return L[i][j]


if '__main__' == __name__:
    L = [
        [1, 3, 2],
        [4, 3, 1],
        [5, 6, 1]
    ]
    print(solution(L))
