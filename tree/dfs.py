# http://www.geeksforgeeks.org/depth-first-traversal-for-a-graph/

from __init__ import Graph


def recur(g, v, visited):
    visited.append(v)
    for u in g[v]:
        if u in visited:
            continue
        recur(g, u, visited)


def solution(g, start):
    visited = []
    recur(g, start, visited)
    return visited


if __name__ == '__main__':
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(2, 6)
    print(solution(g, 0))
