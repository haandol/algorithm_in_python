# http://www.geeksforgeeks.org/find-maximum-path-sum-in-a-binary-tree/


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def run(root, s):
    if not root:
        return 0

    max_child = max(run(root.left, s), run(root.right, s))
    return s + max(root.value, root.value + max_child)


def solution(root):
    left = run(root.left, 0)
    right = run(root.right, 0)
    return max(
        [root.value, root.value + left + right, root.value + max(left, right)]
    )


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(2)
    root.right = Node(10)

    root.left.left = Node(20)
    root.left.right = Node(1)

    root.right.right = Node(-25)
    root.right.right.left = Node(3)
    root.right.right.right = Node(4)

    print(solution(root))
