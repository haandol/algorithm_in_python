# http://www.geeksforgeeks.org/bfs-vs-dfs-binary-tree/


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def traverse(head):
    values = []

    Q = [head]
    while Q:
        node = Q.pop(0)
        values.append(node.value)
        if node.left:
            Q.append(node.left)
        if node.right:
            Q.append(node.right)

    return values


if '__main__' == __name__:
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.left = Node(4)
    head.left.right = Node(5)

    values = traverse(head)
    assert [1, 2, 3, 4, 5] == values
