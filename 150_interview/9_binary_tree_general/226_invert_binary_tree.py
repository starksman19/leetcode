from collections import deque
from typing import Optional

# Given the root of a binary tree, invert the tree, and return its root.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree_bfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        new_root = TreeNode(root.val)
        que = deque([root])
        new_que = deque([new_root])
        while que:
            old_node = que.popleft()
            new_node = new_que.popleft()

            if old_node.left:
                new_right = TreeNode(old_node.left.val)
                new_node.right = new_right
                que.append(old_node.left)
                new_que.append(new_right)
            if old_node.right:
                new_left = TreeNode(old_node.right.val)
                new_node.left = new_left
                que.append(old_node.right)
                new_que.append(new_left)
        return new_root

    def invertTree_dfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        new_root = TreeNode(root.val)

        def dfs(root_old: TreeNode, root_new: TreeNode):
            if root_old is None:
                return

            if root_old.left:
                new_node = TreeNode(root_old.left.val)
                root_new.right = new_node
                dfs(root_old.left, new_node)
            if root_old.right:
                new_node = TreeNode(root_old.right.val)
                root_new.left = new_node
                dfs(root_old.right, new_node)

        dfs(root, new_root)
        return new_root


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print(Solution().invertTree_dfs(root))
print(Solution().invertTree_bfs(root))


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)

root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

print(Solution().invertTree_dfs(root))
print(Solution().invertTree_bfs(root))
