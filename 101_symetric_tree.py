# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def bfs(nod, left_pass=True) -> List[int]:
            ret = []
            que = deque([nod])
            while que:
                node = que.popleft()
                if node:
                    ret.append(node.val)
                    if left_pass:
                        que.append(node.left)
                        que.append(node.right)
                    else:
                        que.append(node.right)
                        que.append(node.left)
                else:
                    ret.append(None)
            return ret
        return bfs(root.right) == bfs(root.left, False)




root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)

root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print(Solution().isSymmetric(root))
assert Solution().isSymmetric(root) == True