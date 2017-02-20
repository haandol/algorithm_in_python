# https://www.interviewbit.com/problems/gas-station/


class Solution:
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1

        n = len(gas)
        fuel = 0
        start = 0
        for i in xrange(n):
            fuel += gas[i] - cost[i]
            if fuel < 0:
                fuel = 0
                start = i + 1

        return start


if '__main__' == __name__:
    gas = [959, 329, 987, 951, 942, 410, 282, 376, 581, 507, 546, 299, 564, 114, 474, 163, 953, 481, 337, 395, 679, 21, 335, 846, 878, 961, 663, 413, 610, 937, 32, 831, 239, 899, 659, 718, 738, 7, 209]
    cost = [862, 783, 134, 441, 177, 416, 329, 43, 997, 920, 289, 117, 573, 672, 574, 797, 512, 887, 571, 657, 420, 686, 411, 817, 185, 326, 891, 122, 496, 905, 910, 810, 226, 462, 759, 637, 517, 237, 884]
    solution = Solution()
    print solution.canCompleteCircuit(gas, cost)

    gas = [1, 2]
    cost = [2, 1]
    solution = Solution()
    print solution.canCompleteCircuit(gas, cost)
