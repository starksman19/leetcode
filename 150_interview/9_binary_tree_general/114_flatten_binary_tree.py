# Given the root of a binary tree, flatten the tree into a "linked list":
#
# The "linked list" should use the same TreeNode class where the right child pointer points
# to the next node in the list and the left child pointer is always null.
# The "linked list" should be in the same order as a pre-order traversal of the binary tree.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        current = root
        while current:
            if current.left:
                right_side = current.right
                go_to_right = current.left
                # Go to max right of left side
                prev = go_to_right
                while go_to_right:
                    prev = go_to_right
                    go_to_right = go_to_right.right
                # Append right tree to max right of left
                prev.right = right_side

                current.right = current.left
                current.left = None
            current = current.right

    def flatten2(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        traverse_list = deque()

        def preorder_traverse(node: TreeNode, traverse_list: deque[TreeNode]):
            if not node:
                return
            traverse_list.append(node)
            preorder_traverse(node.left, traverse_list)
            preorder_traverse(node.right, traverse_list)

        preorder_traverse(root, traverse_list)
        next_root = traverse_list.popleft()
        while traverse_list:
            next_node = traverse_list.popleft()
            next_root.right = next_node
            next_root.left = None
            next_root = next_node

        return root


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)

root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

root.right.right = TreeNode(6)


Solution().flatten(root)

assert root.val == 1
assert root.left is None

assert root.right.val == 2
assert root.right.left is None

assert root.right.right.val == 3
assert root.right.right.left is None

assert root.right.right.right.val == 4
assert root.right.right.right.left is None

assert root.right.right.right.right.val == 5
assert root.right.right.right.right.left is None

assert root.right.right.right.right.right.val == 6
assert root.right.right.right.right.right.left is None

assert root.right.right.right.right.right.right is None

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)

Solution().flatten(root)

assert root.val == 1
assert root.left is None

assert root.right.val == 2
assert root.right.left is None

assert root.right.right.val == 3
assert root.right.right.left is None
assert root.right.right.right is None

root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)

Solution().flatten(root)

assert root.val == 1
assert root.left is None

assert root.right.val == 2
assert root.right.left is None

assert root.right.right.val == 3
assert root.right.right.left is None
assert root.right.right.right is None

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)

root.left.left = TreeNode(3)
root.right.left = TreeNode(6)

Solution().flatten(root)

assert root.val == 1
assert root.left is None

assert root.right.val == 2
assert root.right.left is None

assert root.right.right.val == 3
assert root.right.right.left is None

assert root.right.right.right.val == 5
assert root.right.right.right.left is None

assert root.right.right.right.right.val == 6
assert root.right.right.right.right.left is None
assert root.right.right.right.right.right is None
