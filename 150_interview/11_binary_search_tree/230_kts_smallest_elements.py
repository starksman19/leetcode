# Given the root of a binary search tree, and an integer k,
# return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        l = []

        def inorder(node: TreeNode):
            if node is None:
                return
            inorder(node.left)
            l.append(node.val)
            inorder(node.right)

        inorder(root)
        return l[k - 1]


root = TreeNode(
    val=5,
    right=TreeNode(val=6),
    left=TreeNode(3, right=TreeNode(4), left=TreeNode(2, left=TreeNode(1))),
)

print(Solution().kthSmallest(root, 3))
assert Solution().kthSmallest(root, 3) == 3
