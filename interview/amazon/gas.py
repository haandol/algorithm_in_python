# https://www.interviewbit.com/problems/gas-station/


class Solution:
    def canCompleteCircuit(self, gas, cost):
        n = len(gas)
        gas = gas*2
        cost = cost*2

        for start in xrange(n):
            fuel = 0
            for i in xrange(start, n+1):
                fuel += gas[i]
                if fuel < cost[i]:
                    break
            else:
                return True
        return False


if '__main__' == __name__:
    gas = [1, 2]
    cost = [2, 1]
    solution = Solution()
    print solution.canCompleteCircuit(gas, cost)
