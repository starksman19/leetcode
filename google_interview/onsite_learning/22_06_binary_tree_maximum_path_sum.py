# LeetCode: https://leetcode.com/problems/binary-tree-maximum-path-sum/
# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them.
# A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
#
# The path sum of a path is the sum of the node's values in the path.
#
# Given the root of a binary tree, return the maximum path sum of any non-empty path.

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(
        self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ret = float("-inf")

        def dfs_max(node: TreeNode) -> int:
            nonlocal ret
            if not node:
                return 0
            left = dfs_max(node.left)
            right = dfs_max(node.right)
            ret = max(ret, node.val + max(left, 0) + max(right, 0))

            return node.val + max(max(left, right), 0)

        dfs_max(root)

        return ret


def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    index = 1
    while queue and index < len(values):
        node = queue.popleft()
        if index < len(values) and values[index] is not None:
            node.left = TreeNode(values[index])
            queue.append(node.left)
        index += 1
        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            queue.append(node.right)
        index += 1
    return root


root = build_tree([1, 2, 3])

print(Solution().maxPathSum(root))
assert Solution().maxPathSum(root) == 6

root = build_tree([-10, 9, 20, None, None, 15, 7])

print(Solution().maxPathSum(root))
assert Solution().maxPathSum(root) == 42
