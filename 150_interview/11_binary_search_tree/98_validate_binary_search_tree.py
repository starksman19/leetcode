# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
#
# A valid BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys strictly less than the node's key.
# The right subtree of a node contains only nodes with keys strictly greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST2(self, root: Optional[TreeNode]) -> bool:
        nodes = []

        def dfs(node: TreeNode):
            if node is None:
                return
            dfs(node.left)
            nodes.append(node.val)
            dfs(node.right)

        prev = float("-inf")
        dfs(root)
        for val in nodes:
            if val > prev:
                prev = val
                continue
            else:
                return False
        return True

    prev = float("-inf")

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: TreeNode):
            if node is None:
                return True
            if not dfs(node.left):
                return False
            if node.val <= self.prev:
                return False
            self.prev = node.val
            return dfs(node.right)

        return dfs(root)


# root = TreeNode(2)
# root.left = TreeNode(1)
# root.right = TreeNode(3)
#
# print(Solution().isValidBST(root))
# assert Solution().isValidBST(root) == True

root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)

root.right.left = TreeNode(3)
root.right.right = TreeNode(6)

print(Solution().isValidBST(root))
assert Solution().isValidBST(root) == False
