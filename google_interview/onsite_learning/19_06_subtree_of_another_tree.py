# Given the roots of two binary trees root and subRoot, return true if subRoot is a subtree of root.

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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
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


root = build_tree([3, 4, 5, 1, 2])
sub_root = build_tree([4, 1, 2])

print(Solution().isSubtree(root, sub_root))
assert Solution().isSubtree(root, sub_root) == True

root = build_tree([3, 4, 5, 1, 2, None, None, None, None, 0])
sub_root = build_tree([4, 1, 2])

print(Solution().isSubtree(root, sub_root))
assert Solution().isSubtree(root, sub_root) == False
