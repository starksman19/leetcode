from typing import List, Optional


# ---------------------------
# 1. BFS
def bfs_warmup(start, graph: dict):
    pass


assert bfs_warmup(1, {1: [2, 3], 2: [4], 3: [], 4: []}) == [1, 2, 3, 4]


# ---------------------------
# 2. DFS
def dfs_warmup(start, graph: dict):
    pass


assert dfs_warmup(1, {1: [2, 3], 2: [4], 3: [], 4: []}) == [1, 2, 4, 3]


# ---------------------------
# 3. Binary Search
def binary_search_warmup(arr: List[int], target: int):
    pass


assert binary_search_warmup([1, 2, 3, 5, 8], 5) == 3
assert binary_search_warmup([1, 2, 3], 4) == -1


# ---------------------------
# 4. Sliding Window
def sliding_window_warmup(arr: List[int], k: int):
    pass


assert sliding_window_warmup([2, 1, 5, 1, 3, 2], 3) == 9


# ---------------------------
# 5. Two Pointers
def two_pointers_warmup(arr: List[int], target: int):
    pass


assert two_pointers_warmup([1, 2, 3, 4, 6], 6) == True
assert two_pointers_warmup([2, 3, 4], 8) == False


# ---------------------------
# 6. Stack
def stack_warmup(s: str):
    pass


assert stack_warmup("()[]{}") == True
assert stack_warmup("([)]") == False


# ---------------------------
# 7. Binary Tree Traversal
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal_warmup(root: Optional[TreeNode]):
    pass


root = TreeNode(1, TreeNode(2), TreeNode(3))
assert inorder_traversal_warmup(root) == [2, 1, 3]


# ---------------------------
# 8. Quickselect
def quickselect_warmup(arr: List[int], k: int):
    pass


assert quickselect_warmup([3, 2, 1, 5, 4], 2) == 2


# ---------------------------
# 9. Divide and Conquer
def divide_and_conquer_sum(arr: List[int], l: int, r: int):
    pass


assert divide_and_conquer_sum([1, 2, 3, 4], 0, 3) == 10


# ---------------------------
# 10. DP — LIS
def lis_warmup(nums: List[int]):
    pass


assert lis_warmup([10, 9, 2, 5, 3, 7, 101, 18]) == 4


# ---------------------------
# 11. DP — Knapsack 0/1
def knapsack_warmup(weights: List[int], values: List[int], W: int):
    pass


assert knapsack_warmup([1, 3, 4, 5], [1, 4, 5, 7], 7) == 9


# ---------------------------
# 12. DP — Coin Change
def coin_change_warmup(coins: List[int], amount: int):
    pass


assert coin_change_warmup([1, 2, 5], 11) == 3
