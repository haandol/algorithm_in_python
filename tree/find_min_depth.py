# http://www.geeksforgeeks.org/find-minimum-depth-of-a-binary-tree/

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def solution(root):
    if not root:
        return 0

    if not root.left:
        return solution(root.right) + 1
    if not root.right:
        return solution(root.left) + 1

    return min(solution(root.left), solution(root.right)) + 1


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    root.left.left = Node(4)
    root.left.right = Node(5)

    root.right.left = Node(6)
    root.right.left.left = Node(7)

    print(solution(root))
