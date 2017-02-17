# http://www.geeksforgeeks.org/bfs-vs-dfs-binary-tree/


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def traverse_in_order(values, node):
    if not node:
        return

    if node.left:
        traverse_in_order(values, node.left)
    values.append(node.value)
    if node.right:
        traverse_in_order(values, node.right)


if '__main__' == __name__:
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.left = Node(4)
    head.left.right = Node(5)

    values = []
    traverse_in_order(values, head)
    assert [4, 2, 5, 1, 3] == values
