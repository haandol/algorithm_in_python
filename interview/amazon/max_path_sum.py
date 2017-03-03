class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, A):
        max_sum = float('-inf')

        def update_max(root):
            nonlocal max_sum

            if not root:
                return 0

            l = max(0, update_max(root.left))
            r = max(0, update_max(root.right))
            max_sum = max(max_sum, l + r + root.val)
            return root.val + max(l, r)

        update_max(A)

        return max_sum


if '__main__' == __name__:
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.right = Node(4)
    root.left.left = Node(-1)
    root.left.left.left = Node(3)
    root.left.left.right = Node(5)
    solution = Solution()
    print(solution.maxPathSum(root))

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    solution = Solution()
    print(solution.maxPathSum(root))

    root = Node(-100)
    root.left = Node(-200)
    root.right = Node(-300)
    solution = Solution()
    print(solution.maxPathSum(root))
