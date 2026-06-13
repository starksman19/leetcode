# LeetCode: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Given the root of a binary tree, return its maximum depth.

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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], level: int):
            if node is None:
                return level
            return max(dfs(node.right, level + 1), dfs(node.left, level + 1))

        return dfs(root, 0)


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


root = build_tree([3, 9, 20, None, None, 15, 7])

print(Solution().maxDepth(root))
assert Solution().maxDepth(root) == 3

root = build_tree([1, None, 2])

print(Solution().maxDepth(root))
assert Solution().maxDepth(root) == 2
