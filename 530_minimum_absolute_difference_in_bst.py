from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference_bad(self, root: Optional[TreeNode]) -> int:
        values = []

        queue = deque([root])
        while queue:
            node = queue.popleft()
            values.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        values.sort() # LAZY and not optimal
        min_diff = float('inf')
        for i in range(1, len(values)):
            min_diff = min(min_diff, values[i] - values[i - 1])

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_value = float('inf')
        prev = None
        def dfs(node):
            nonlocal min_value
            nonlocal prev
            if node is None:
                return
            dfs(node.left)
            if prev is not None:
                min_value = min(min_value, abs(node.val - prev))
            prev = node.val
            dfs(node.right)

        dfs(root)
        return min_value


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)

root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

s = Solution()
print(s.getMinimumDifference(root))
assert s.getMinimumDifference(root) == 1
