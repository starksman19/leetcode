# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def bfs(root: TreeNode):
            que = deque([root])
            ret = []
            while que:
                node = que.popleft()
                if not node:
                    ret.append(None)
                    continue
                que.append(node.left)
                que.append(node.right)
                ret.append(node.val)
            return ret
        return bfs(p) == bfs(q)