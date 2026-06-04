# LeetCode: https://leetcode.com/problems/same-tree/
# Given the roots of two binary trees, return true when the trees have the same structure and values.

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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
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


p = build_tree([1, 2, 3])
q = build_tree([1, 2, 3])

print(Solution().isSameTree(p, q))
assert Solution().isSameTree(p, q) == True

p = build_tree([1, 2])
q = build_tree([1, None, 2])

print(Solution().isSameTree(p, q))
assert Solution().isSameTree(p, q) == False
