from collections import deque
import heapq
import random
from typing import List, Optional


# ---------------------------
# 1. BFS
def bfs_warmup(start, graph: dict):
    """
    Wejście:
        - start: wierzchołek startowy
        - graph: dict -> lista sąsiadów {node: [neighbors]}
    Wyjście:
        - lista odwiedzonych wierzchołków w kolejności BFS
    Oczekiwanie:
        - przechodzimy graf poziomami
    """
    queue = deque([start])
    out = []
    while queue:
        it = queue.popleft()
        for node in graph[it]:
            queue.append(node)
        out.append(it)
    return out


assert bfs_warmup(1, {1: [2, 3], 2: [4], 3: [], 4: []}) == [1, 2, 3, 4]


# ---------------------------
# 2. DFS
def dfs_warmup(start, graph: dict):
    """
    Wejście:
        - start: wierzchołek startowy
        - graph: dict -> lista sąsiadów {node: [neighbors]}
    Wyjście:
        - lista odwiedzonych wierzchołków w kolejności DFS
    Oczekiwanie:
        - przechodzimy graf w głąb
    """
    out = [start]
    visited = set()

    def dfs(n):
        nonlocal graph
        if graph.get(n, None) is None:
            return
        for node in graph[n]:
            if node not in visited:
                visited.add(node)
                out.append(node)
                dfs(node)

    dfs(start)
    return out


assert dfs_warmup(1, {1: [2, 3], 2: [4], 3: [], 4: []}) == [1, 2, 4, 3]


# ---------------------------
# 3. Binary Search
def binary_search_warmup(arr: List[int], target: int):
    """
    Wejście:
        - arr: posortowana lista liczb
        - target: szukana liczba
    Wyjście:
        - indeks elementu jeśli znaleziony
        - -1 jeśli nie istnieje
    Oczekiwanie:
        - logarytmiczny czas wyszukiwania
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


assert binary_search_warmup([1, 2, 3, 5, 8], 5) == 3
assert binary_search_warmup([1, 2, 3], 4) == -1


# ---------------------------
# 4. Sliding Window
def sliding_window_warmup(arr: List[int], k: int):
    """
    Wejście:
        - arr: lista liczb
        - k: długość okna
    Wyjście:
        - maksimum sumy wartości w dowolnym oknie długości k
    Oczekiwanie:
        - przesuwamy okno po tablicy
    """
    left, right = 0, k - 1
    out = 0
    while right <= len(arr) - 1:
        out = max(out, sum(arr[left : right + 1]))
        left += 1
        right += 1
    return out


assert sliding_window_warmup([2, 1, 5, 1, 3, 2], 3) == 9


# ---------------------------
# 5. Two Pointers
def two_pointers_warmup(arr: List[int], target: int):
    """
    Wejście:
        - arr: posortowana lista liczb
        - target: suma docelowa
    Wyjście:
        - True jeśli istnieje para sumująca się do target
        - False w przeciwnym razie
    Oczekiwanie:
        - dwa wskaźniki przesuwające się ku sobie
    """
    left, right = 0, len(arr) - 1
    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            return True
        elif s > target:
            right -= 1
        elif s < target:
            left += 1
    return False


assert two_pointers_warmup([1, 2, 3, 4, 6], 6) == True
assert two_pointers_warmup([2, 3, 4], 8) == False


# ---------------------------
# 6. Stack
def stack_warmup(s: str):
    """
    Wejście:
        - s: string zawierający nawiasy (), {}, []
    Wyjście:
        - True jeśli wszystkie nawiasy są poprawnie zbalansowane
        - False w przeciwnym razie
    Oczekiwanie:
        - stos do śledzenia otwarć nawiasów
    """
    char_map = {
        "}": "{",
        "]": "[",
        ")": "(",
    }
    que = []
    for char in s:
        if char in char_map.values():
            que.append(char)
        elif not que:
            return False
        elif que[-1] == char_map[char]:
            que.pop()

    return not que


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
    """
    Wejście:
        - root: korzeń drzewa binarnego
    Wyjście:
        - lista wartości w kolejności in-order (lewy->korzeń->prawy)
    Oczekiwanie:
        - przechodzimy całe drzewo rekurencyjnie
    """
    out = []

    def dfs(node: TreeNode):
        if node is None:
            return

        dfs(node.left)
        out.append(node.val)
        dfs(node.right)

    dfs(root)
    return out


root = TreeNode(
    1,
    TreeNode(2, TreeNode(4), None),
    TreeNode(3, TreeNode(5, TreeNode(7), None), TreeNode(6)),
)
assert inorder_traversal_warmup(root) == [4, 2, 1, 7, 5, 3, 6]


# ---------------------------
# 8. Quickselect
def quickselect_warmup(arr: List[int], k: int):
    """
    Wejście:
        - arr: lista liczb
        - k: pozycja (1-indexed) najmniejszego elementu
    Wyjście:
        - wartość k-tego najmniejszego elementu
    Oczekiwanie:
        - średnio O(n), losowy pivot
    """
    k = len(arr) - k

    def partition(left: int, right: int):
        pivot, pointer = arr[right], left
        for i in range(left, right):
            if arr[i] <= pivot:
                arr[i], arr[pointer] = arr[pointer], arr[i]
                pointer += 1
        arr[right], arr[pointer] = arr[pointer], arr[right]
        if pointer == k:
            return arr[k]
        elif pointer < k:
            return partition(pointer + 1, right)
        else:
            return partition(left, pointer - 1)

    return partition(0, len(arr) - 1)


nums = [3, 2, 1, 5, 6, 4]
k = 2
assert quickselect_warmup(nums, k) == 5


# ---------------------------
# 9. Divide and Conquer
def divide_and_conquer_sum(arr: List[int], l: int, r: int):
    """
    Wejście:
        - arr: lista liczb
        - l, r: indeksy zakresu
    Wyjście:
        - suma elementów arr[l:r+1]
    Oczekiwanie:
        - dzielimy problem na pół i sumujemy wyniki
    """
    if not arr:
        return 0
    if l == r:
        return arr[l]

    mid = (l + r) // 2
    left = divide_and_conquer_sum(arr, l, mid)
    right = divide_and_conquer_sum(arr, mid + 1, r)
    return left + right


assert divide_and_conquer_sum([1, 2, 3, 4], 0, 3) == 10


# ---------------------------
# 10. Dynamic Programming — LIS
def lis_warmup(nums: List[int]):
    """
    Wejście:
        - nums: lista liczb
    Wyjście:
        - długość najdłuższej rosnącej podsekwencji

        - używamy DP, O(n^2) lub O(n log n)
    """
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


assert lis_warmup([10, 9, 2, 5, 3, 7, 101, 18]) == 4


# ---------------------------
# 11. Dynamic Programming — Knapsack 0/1
def knapsack_warmup(weights: List[int], values: List[int], W: int):
    """
    Wejście:
        - weights: lista wag przedmiotów
        - values: lista wartości przedmiotów
        - W: maksymalna pojemność plecaka
    Wyjście:
        - maksymalna wartość, którą można włożyć do plecaka
    Oczekiwanie:
        - klasyczny plecak 0/1 z DP
    """
    dp = [[0] * (W + 1) for _ in range((len(values) + 1))]
    for i in range(1, len(values) + 1):
        for j in range(1, W + 1):
            if weights[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(
                    dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1]
                )
    return max([max(i) for i in dp])


assert knapsack_warmup([1, 3, 4, 5], [1, 4, 5, 7], 7) == 9


# ---------------------------
# 12. Dynamic Programming — Coin Change
def coin_change_warmup(coins: List[int], amount: int):
    """
    Wejście:
        - coins: lista nominałów monet
        - amount: kwota do uzyskania
    Wyjście:
        - minimalna liczba monet potrzebna do uzyskania amount
        - -1 jeśli nie da się uzyskać amount
    Oczekiwanie:
        - klasyczny DP minimalizacji liczby monet
    """
    if amount == 0:
        return 0

    dp = [float("inf") for _ in range(amount + 1)]
    dp[0] = 0
    for val in range(1, len(dp)):
        for coin in coins:
            if val - coin >= 0:
                dp[val] = min(dp[val], dp[val - coin] + 1)

    return dp[-1] if dp[-1] != float("inf") else -1


assert coin_change_warmup([1, 2, 5], 11) == 3
