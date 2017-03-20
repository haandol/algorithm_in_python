# http://www.geeksforgeeks.org/greedy-algorithms-set-6-dijkstras-shortest-path-algorithm/


def solution(g, start):
    dist = [99999 for _ in range(len(g))]
    dist[start] = 0

    visited = []
    path = {}

    Q = list(g.keys())
    while Q:
        u = min(Q, key=lambda x: dist[x])
        Q.remove(u)
        if u in visited:
            continue

        for v, d in g[u].items():
            alter = dist[u] + d
            if alter < dist[v]:
                dist[v] = alter
                path[v] = u

        visited.append(u)

    return path



if '__main__' == __name__:
    g = {
        0: {1: 4, 7: 8},
        1: {0: 4, 2: 8, 7: 11},
        2: {1: 8, 3: 7, 5: 4, 8: 2},
        3: {2: 7, 4: 9, 5: 14},
        4: {3: 9, 5: 10},
        5: {2: 4, 3: 14, 4: 10, 6: 2},
        6: {5: 2, 7: 1, 8: 6},
        7: {0: 8, 1: 11, 6: 1, 8: 7},
        8: {2: 2, 6: 6, 7: 7},
    }
    start = 0
    path = solution(g, start)

    end = 8
    while end != start:
        print(f'{end} <- {path[end]}')
        end = path[end]
