# LeetCode: https://leetcode.com/problems/subtree-of-another-tree/
# Given the roots of two binary trees root and subRoot, return true if there is a subtree
# of root with the same structure and node values of subRoot and false otherwise.
#
# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants.
# The tree tree could also be considered as a subtree of itself.

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
    def isSubtree_bfs(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        q_root = deque([root])
        subroot_val = subRoot.val

        while q_root:
            node = q_root.popleft()
            if node.val == subroot_val:
                q_search = deque([node])
                q_subroot = deque([subRoot])
                same = True

                while q_search and q_subroot:
                    search = q_search.popleft()
                    q = q_subroot.popleft()

                    if search is None and q is None:
                        continue

                    if search is None or q is None:
                        same = False
                        break

                    if search.val != q.val:
                        same = False
                        break

                    q_search.append(search.left)
                    q_search.append(search.right)
                    q_subroot.append(q.left)
                    q_subroot.append(q.right)

                if not same or q_search or q_subroot:
                    if node.left:
                        q_root.append(node.left)
                    if node.right:
                        q_root.append(node.right)
                    continue

                return True

            else:
                if node.left:
                    q_root.append(node.left)
                if node.right:
                    q_root.append(node.right)

        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.dfs(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def dfs(self, new_root: TreeNode, subr: TreeNode) -> bool:
        if not new_root and not subr:
            return True
        if not new_root or not subr:
            return False
        if new_root.val != subr.val:
            return False
        return self.dfs(new_root.left, subr.left) and self.dfs(new_root.right, subr.right)


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


root = build_tree([1, 1])
sub_root = build_tree([1])

print(Solution().isSubtree(root, sub_root))
assert Solution().isSubtree(root, sub_root) == True

root = build_tree([3, 4, 5, 1, 2])
sub_root = build_tree([4, 1, 2])

print(Solution().isSubtree(root, sub_root))
assert Solution().isSubtree(root, sub_root) == True

root = build_tree([3, 4, 5, 1, 2, None, None, None, None, 0])
sub_root = build_tree([4, 1, 2])

print(Solution().isSubtree(root, sub_root))
assert Solution().isSubtree(root, sub_root) == False
