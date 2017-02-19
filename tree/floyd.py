# http://www.geeksforgeeks.org/dynamic-programming-set-16-floyd-warshall-algorithm/

from copy import deepcopy
from tabulate import tabulate


def floyd(mat):
    n = len(mat)

    dist = deepcopy(mat)

    for k in range(n):
        for u in range(n):
            for v in range(n):
                dist[u][v] = min(dist[u][v], dist[u][k] + dist[k][v])

    return dist



if '__main__' == __name__:
    mat = [
        [0, 5, 9999, 10],
        [9999, 0, 3, 9999],
        [9999, 9999, 0, 1],
        [9999, 9999, 9999, 0],
    ]
    print(tabulate(floyd(mat)))
