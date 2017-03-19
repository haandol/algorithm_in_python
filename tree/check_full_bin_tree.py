# http://www.geeksforgeeks.org/check-whether-binary-tree-full-binary-tree-not/


from __init__ import Node


def solution(root):
    if not root:
        return True

    if root.left and not root.right:
        return False

    if root.right and not root.left:
        return False

    return solution(root.left) and solution(root.right)



if __name__ == '__main__':
    root = Node(1)
    print(solution(root))

    root = Node(1)
    root.left = Node(2)
    print(solution(root))

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    print(solution(root))

    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)

    root.left.right = Node(40)
    root.left.left = Node(50)
    root.right.left = Node(60)
    root.right.right = Node(70)

    root.left.left.left = Node(80)
    root.left.left.right = Node(90)
    root.left.right.left = Node(80)
    root.left.right.right = Node(90)
    root.right.left.left = Node(80)
    root.right.left.right = Node(90)
    root.right.right.left = Node(80)
    root.right.right.right = Node(90)
    print(solution(root))
