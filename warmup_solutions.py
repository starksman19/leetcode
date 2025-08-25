from collections import deque
import random
from typing import List, Optional


# ---------------------------
# 1. BFS
def bfs_warmup(start, graph: dict):
    visited = set([start])
    q = deque([start])
    order = []
    while q:
        node = q.popleft()
        order.append(node)
        for nei in graph.get(node, []):
            if nei not in visited:
                visited.add(nei)
                q.append(nei)
    return order


assert bfs_warmup(1, {1: [2, 3], 2: [4], 3: [], 4: []}) == [1, 2, 3, 4]


# ---------------------------
# 2. DFS
def dfs_warmup(start, graph: dict):
    visited = set()
    order = []

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        order.append(node)
        for nei in graph.get(node, []):
            dfs(nei)

    dfs(start)
    assert order == [1, 2, 4, 3]
    return order


assert dfs_warmup(1, {1: [2, 3], 2: [4], 3: [], 4: []}) == [1, 2, 4, 3]


# ---------------------------
# 3. Binary Search
def binary_search_warmup(arr: List[int], target: int):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


assert binary_search_warmup([1, 2, 3, 5, 8], 5) == 3
assert binary_search_warmup([1, 2, 3], 4) == -1


# ---------------------------
# 4. Sliding Window
def sliding_window_warmup(arr: List[int], k: int):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum


assert sliding_window_warmup([2, 1, 5, 1, 3, 2], 3) == 9


# ---------------------------
# 5. Two Pointers
def two_pointers_warmup(arr: List[int], target: int):
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        s = arr[lo] + arr[hi]
        if s == target:
            return True
        elif s < target:
            lo += 1
        else:
            hi -= 1
    return False


assert two_pointers_warmup([1, 2, 3, 4, 6], 6) == True
assert two_pointers_warmup([2, 3, 4], 8) == False


# ---------------------------
# 6. Stack
def stack_warmup(s: str):
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return not stack


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
    res = []

    def inorder(node):
        if not node:
            return
        inorder(node.left)
        res.append(node.val)
        inorder(node.right)

    inorder(root)
    return res


root = TreeNode(1, TreeNode(2), TreeNode(3))
assert inorder_traversal_warmup(root) == [2, 1, 3]


# ---------------------------
# 8. Quickselect
def quickselect_warmup(arr: List[int], k: int):
    if not arr:
        return None
    pivot = random.choice(arr)
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]
    if k <= len(lows):
        return quickselect_warmup(lows, k)
    elif k <= len(lows) + len(pivots):
        return pivot
    else:
        return quickselect_warmup(highs, k - len(lows) - len(pivots))


assert quickselect_warmup([3, 2, 1, 5, 4], 2) == 2


# ---------------------------
# 9. Divide and Conquer
def divide_and_conquer_sum(arr: List[int], l: int, r: int):
    if l > r:
        return 0
    if l == r:
        return arr[l]
    mid = (l + r) // 2
    return divide_and_conquer_sum(arr, l, mid) + divide_and_conquer_sum(arr, mid + 1, r)


assert divide_and_conquer_sum([1, 2, 3, 4], 0, 3) == 10


# ---------------------------
# 10. DP — LIS
def lis_warmup(nums: List[int]):
    if not nums:
        return 0
    n = len(nums)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


assert lis_warmup([10, 9, 2, 5, 3, 7, 101, 18]) == 4


# ---------------------------
# 11. DP — Knapsack 0/1
def knapsack_warmup(weights: List[int], values: List[int], W: int):
    n = len(weights)
    dp = [0] * (W + 1)
    for i in range(n):
        for w in range(W, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[W]


assert knapsack_warmup([1, 3, 4, 5], [1, 4, 5, 7], 7) == 9


# ---------------------------
# 12. DP — Coin Change
def coin_change_warmup(coins: List[int], amount: int):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != float("inf") else -1


assert coin_change_warmup([1, 2, 5], 11) == 3
