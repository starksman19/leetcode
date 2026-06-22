# LeetCode: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# Design an algorithm to serialize a binary tree to a string and deserialize the string back to the original tree.

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(
        self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        ret = []
        que = deque([root])
        while que:
            node = que.popleft()
            if node:
                que.append(node.left)
                que.append(node.right)
                ret.append(str(node.val))
            else:
                ret.append(str(None))
        while ret and ret[-1] == "None":
            ret.pop()
        return ",".join(ret)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        vals = data.split(",")
        que_rest = deque(vals[1:])
        new_root = TreeNode(val=int(vals[0]))
        que_to_visit = deque([new_root])
        while que_rest:
            node = que_to_visit.popleft()
            left = que_rest.popleft()

            if left != "None":
                left_node = TreeNode(val=int(left))
                node.left = left_node
                que_to_visit.append(left_node)
            if que_rest:
                right = que_rest.popleft()
                if right != "None":
                    right_node = TreeNode(val=int(right))
                    node.right = right_node
                    que_to_visit.append(right_node)
        return new_root


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


codec = Codec()
root = build_tree([1, 2, 3, None, None, 4, 5])

print(codec.serialize(root))
assert tree_to_list(codec.deserialize(codec.serialize(root))) == [1, 2, 3, None, None, 4, 5]

root = build_tree([])

print(codec.serialize(root))
assert tree_to_list(codec.deserialize(codec.serialize(root))) == []
