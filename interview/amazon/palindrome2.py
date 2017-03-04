class Solution:
    def minCut(self, s):
        n = len(s)
        if n < 2:
            return 0

        IS_PAL = [[False]*n for _ in range(n)]
        DP = [0] * n

        for i in range(n):
            IS_PAL[i][i] = True
            DP[i] = i

        for i in range(1, n):
            for j in range(i, -1, -1):
                if s[i] == s[j] and (i-j < 2 or IS_PAL[i-1][j+1]):
                    if j == 0:
                        DP[i] = 0
                    else:
                        IS_PAL[i][j] = True
                        DP[i] = min(1+DP[j-1], DP[i])

        return DP[n-1]


if '__main__' == __name__:
    solution = Solution()

    A = 'bbab'
    print(solution.minCut(A))

    A = 'babb'
    print(solution.minCut(A))

    A = 'aab'
    print(solution.minCut(A))

    A = 'ab'
    print(solution.minCut(A))

    A = 'abbacccedde'
    print(solution.minCut(A))
