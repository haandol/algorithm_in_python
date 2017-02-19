# https://en.wikipedia.org/wiki/Dijkstra's_algorithm


def dijkstra(G, start):
    VISIT = []
    PATH = {}
    DIST = {k: 99999 for k in G}
    DIST[start] = 0
    Q = G.keys()
    while Q:
        u = min(Q, key=lambda x: DIST[x])
        Q.pop(Q.index(u))
        if u in VISIT:
            continue

        for v in G[u]:
            alt = DIST[u] + G[u][v]
            if alt < DIST[v]:
                DIST[v] = alt
                PATH[v] = u

        VISIT.append(u)

    return PATH


if '__main__' == __name__:
    G = {
        'a': {'b': 7, 'c': 9, 'f': 14},
        'b': {'a': 7, 'c': 10, 'd': 15},
        'c': {'a': 9, 'b': 10, 'd': 11, 'f': 2},
        'd': {'b': 15, 'c': 11, 'e': 6},
        'e': {'d': 6, 'f': 9},
        'f': {'a': 14, 'c': 2, 'e': 9},
    }

    start, end = 'a', 'e'
    P = dijkstra(G, start)

    node = P[end]
    VISIT = [node, end]
    while start not in VISIT:
        node = P[node]
        VISIT.insert(0, node)
    print VISIT
