# https://www.interviewbit.com/problems/longest-increasing-subsequence/


class Solution:
    def lis(self, A):
        n = len(A)
        DP = [1] * n
        for i in xrange(1, n):
            for j in xrange(i):
                if A[j] < A[i]:
                    DP[i] = max(DP[i], DP[j] + 1)

        return max(DP)


if '__main__' == __name__:
    A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    solution = Solution()
    print solution.lis(A)
