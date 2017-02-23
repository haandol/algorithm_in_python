# https://www.interviewbit.com/problems/ways-to-decode/

import string


table = {
    str(code): letter
    for code, letter in enumerate(string.ascii_uppercase, 1)
}


class Solution:
    def numDecodings(self, A):
        DP = [0 for x in xrange(len(A))]
        if A[0] in table:
            DP[0] = 1

        for i in xrange(1, len(A)):
            if A[i] in table:
                DP[i] += DP[i-1]

            if A[i-1:i+1] in table:
                if i == 1:
                    DP[i] += 1
                else:
                    DP[i] += DP[i-2]

        return DP[len(A)-1]


if '__main__' == __name__:
    A = "1222"
    solution = Solution()
    assert 5 == solution.numDecodings(A)

    A = "1235"
    solution = Solution()
    print solution.numDecodings(A)

    A = "875361268549483279131"
    solution = Solution()
    print solution.numDecodings(A)
