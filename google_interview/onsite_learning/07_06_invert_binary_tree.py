# LeetCode: https://leetcode.com/problems/invert-binary-tree/
# Given the root of a binary tree, invert the tree and return its root.

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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        def dfs_invert(node: TreeNode):
            if not node:
                return
            dfs_invert(node.left)
            dfs_invert(node.right)
            node.left, node.right = node.right, node.left

        dfs_invert(root)
        return root


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


def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


root = build_tree([4, 2, 7, 1, 3, 6, 9])

print(tree_to_list(Solution().invertTree(root)))
assert tree_to_list(Solution().invertTree(build_tree([4, 2, 7, 1, 3, 6, 9]))) == [
    4,
    7,
    2,
    9,
    6,
    3,
    1,
]
