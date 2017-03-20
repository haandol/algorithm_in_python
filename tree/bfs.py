# http://www.geeksforgeeks.org/breadth-first-traversal-for-a-graph/

from __init__ import Graph


def solution(g, start):
    result = []

    visited = []
    Q = [start]
    while Q:
        node = Q.pop(0)
        if node in visited:
            continue

        result.append(node)
        Q.extend(g[node])
        visited.append(node)

    return result


if __name__ == '__main__':
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(2, 6)
    print(solution(g, 0))
