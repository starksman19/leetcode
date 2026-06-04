# LeetCode: https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Given the root of a non-empty binary tree, return the maximum path sum.
# A path may start and end at any nodes and must follow parent-child connections.

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
        pass


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
