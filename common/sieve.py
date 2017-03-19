def solution(n):
    prime = [True for _ in range(n+1)]
    prime[0] = False
    prime[1] = False
    prime[2] = True

    for i in range(2, n):
        for j in range(2, n):
            if i*j > n:
                break
            prime[i*j] = False

    return [i for i, el in enumerate(prime) if el]


if __name__ == '__main__':
    print(solution(47))
