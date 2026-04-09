# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        que = deque([root])
        ret = []
        while que:
            level = []
            start_que_len = len(que)
            for i in range(start_que_len):
                node = que.popleft()
                level.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            ret.append(level[:])
            level.clear()
        return ret


sol = Solution()

root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)
assert sol.levelOrder(root1) == [[3], [9, 20], [15, 7]]


root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)
assert sol.levelOrder(root2) == [[1], [2, 3], [4, 5]]


root3 = TreeNode(5)
root3.left = TreeNode(4)
root3.right = TreeNode(8)
root3.left.left = TreeNode(11)
root3.left.left.left = TreeNode(7)
root3.left.left.right = TreeNode(2)
root3.right.left = TreeNode(13)
root3.right.right = TreeNode(4)
root3.right.right.right = TreeNode(1)
assert sol.levelOrder(root3) == [[5], [4, 8], [11, 13, 4], [7, 2, 1]]


root4 = TreeNode(1)
root4.right = TreeNode(2)
root4.right.right = TreeNode(3)
root4.right.right.right = TreeNode(4)
assert sol.levelOrder(root4) == [[1], [2], [3], [4]]


root5 = TreeNode(1)
root5.left = TreeNode(2)
root5.left.left = TreeNode(3)
root5.left.left.left = TreeNode(4)
assert sol.levelOrder(root5) == [[1], [2], [3], [4]]


root6 = TreeNode(1)
assert sol.levelOrder(root6) == [[1]]


root7 = None
assert sol.levelOrder(root7) == []
