# http://www.geeksforgeeks.org/greedy-algorithms-set-5-prims-minimum-spanning-tree-mst-2/


def min_key(weight, mst, n):
    safe_nodes = [v for v in range(n) if v not in mst]
    return min(safe_nodes, key=lambda v: weight[v])


def print_parent(mat, parent, start):
    n = len(mat)
    print('Edge Weight')
    for i in range(n):
        if i == start:
            continue

        print('{} - {}: {}'.format(parent[i], i, mat[i][parent[i]]))


def prim(mat, start):
    n = len(mat)
    weight = [99999] * n
    parent = [None] * n
    mst = []

    weight[start] = 0
    parent[start] = -1

    while len(mst) != n:
        u = min_key(weight, mst, n)
        mst.append(u)

        for v in range(n):
            if not mat[u][v]:
                continue

            if v not in mst and mat[u][v] < weight[v]:
                weight[v] = mat[u][v]
                parent[v] = u

    print_parent(mat, parent, start)


if '__main__' == __name__:
    '''Graph
            2     3
        (0)---(1)---(2)
         |   /   \   |
        6| 8/     \5 |7
         | /       \ |
        (3)---------(4)
               9
    '''
    mat = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0],
    ]
    prim(mat, 4)
