from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        que = deque([root])
        ret = [root.val]

        while que:
            level = []
            for node in que:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            if level:
                ret.append(level[-1].val)
            que = deque(level)
        return ret


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.right = TreeNode(5)
root.right.right = TreeNode(4)

s = Solution()
print(s.rightSideView(root))
