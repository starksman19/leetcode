# LeetCode: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Given the root of a binary search tree and an integer k, return the kth smallest value in the tree.

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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ret = []

        def dfs(node: Optional[TreeNode]):
            if not node:
                return
            dfs(node.left)
            ret.append(node.val)
            dfs(node.right)

        dfs(root)
        return ret[k - 1]


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


root = build_tree([3, 1, 4, None, 2])
k = 1

print(Solution().kthSmallest(root, k))
assert Solution().kthSmallest(root, k) == 1

root = build_tree([5, 3, 6, 2, 4, None, None, 1])
k = 3

print(Solution().kthSmallest(root, k))
assert Solution().kthSmallest(root, k) == 3
