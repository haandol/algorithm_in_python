def solution(coins, change):
    DP = list(range(change+1))

    for i in range(change+1):
        for coin in coins:
            DP[i] = min(DP[i-coin] + 1, DP[i])

    return DP[change]


if '__main__' == __name__:
    coins = [1, 5, 10, 21, 25]
    print(solution(coins, 63))
