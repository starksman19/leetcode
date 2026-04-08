# Given the root of a Binary Search Tree (BST),
# return the minimum absolute difference between the values of any two different nodes in the tree.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.min_diff = float("inf")

        def inorder(node: TreeNode):
            if not node:
                return
            inorder(node.left)
            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val
            inorder(node.right)

        inorder(root)
        return self.min_diff


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)

root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

s = Solution()
print(s.getMinimumDifference(root))
assert s.getMinimumDifference(root) == 1
