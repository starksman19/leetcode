from collections import deque
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
    que = deque([start])
    ret = []
    while que:
        curr = que.popleft()
        ret.append(curr)
        for val in graph[curr]:
            que.append(val)
    return ret


ret_1 = bfs_warmup(1, {1: [2, 3], 2: [4], 3: [], 4: []})
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
    ret = []
    visited = set()

    def dfs(next_val: int):
        if next_val not in visited:
            visited.add(next_val)
            ret.append(next_val)
            for val in graph[next_val]:
                dfs(val)

    dfs(start)
    return ret


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
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
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
    left, right = 0, k
    ret = 0
    while right < len(arr):
        ret = max(ret, sum(arr[left:right]))
        left += 1
        right += 1
    return ret


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
        suma = arr[left] + arr[right]
        if suma == target:
            return True
        elif suma > target:
            right -= 1
        else:
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
    map_p = {"}": "{", "]": "[", ")": "("}
    ret = []
    for parant in s:
        if parant in map_p.values():
            ret.append(parant)
        else:
            if len(ret) == 0:
                return False
            else:
                val = ret.pop()
                if map_p[parant] != val:
                    return False
    if ret:
        return False
    return True


assert stack_warmup("()[]{}") == True
assert stack_warmup("([)]") == False
assert stack_warmup("([)") == False
assert stack_warmup("([)]]") == False
assert stack_warmup("([)][") == False


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
    ret = []

    def dfs(node: TreeNode):
        if not node:
            return
        dfs(node.left)
        ret.append(node.val)
        dfs(node.right)

    dfs(root)
    return ret


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
        - wartość k-tego największego elementu
    Oczekiwanie:
        - średnio O(n), losowy pivot
    """
    k = len(arr) - k

    def partition(left, right):
        pointer, pivot = left, arr[right]
        for i in range(left, right):
            if arr[i] < pivot:
                arr[i], arr[pointer] = arr[pointer], arr[i]
                pointer += 1
        arr[pointer], arr[right] = arr[right], arr[pointer]
        if pointer == k:
            return arr[k]
        elif pointer > k:
            return partition(left, pointer - 1)
        else:
            return partition(pointer + 1, right)

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

    def div(array, left, right):
        if left == right:
            return array[right]
        mid = (left + right) // 2
        left = div(array, left, mid)
        right = div(array, mid + 1, right)
        return left + right

    return div(arr, l, r)


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
    dp = [1 for _ in range(len(nums))]
    for i in range(len(dp)):
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
    # ile wejdzie przy założeniu takiej wagi -> 0,1,2,3,4,5.. W w
    assert len(weights) == len(values)

    dp = [0 for i in range(W + 1)]
    dp[0] = 0
    for i in range(0, len(weights)):
        for w in range(W, weights[i] - 1, -1):
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])
    return dp[-1]


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
    dp = [float("inf") for _ in range(amount + 1)]
    dp[0] = 0
    for coin in coins:
        for x in range(coin, len(dp)):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[-1] if dp[-1] != float("inf") else -1


assert coin_change_warmup([1, 2, 5], 11) == 3


# ---------------------------
# 13. Backtracking - combinationSum


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """
    # Given an array of distinct integers candidates and a target integer target,
    # return a list of all unique combinations of candidates where the chosen numbers sum to target.
    # You may return the combinations in any order.
    #
    # The same number may be chosen from candidates an unlimited number of times.
    # Two combinations are unique if the frequency of at least one of the chosen numbers is different.
    """
    ret = []

    def backtrack(curr_value: int, curr_values: list[int], start: int):
        if curr_value == target:
            ret.append(curr_values[:])
            return
        elif curr_value > target:
            return
        else:
            for i in range(start, len(candidates)):
                curr_values.append(candidates[i])
                backtrack(curr_value + candidates[i], curr_values, i)
                curr_values.pop()

    backtrack(0, [], 0)
    return ret


candidates1 = [2, 3, 5]
target1 = 8
candidates2 = [2]
target2 = 1
assert combination_sum(candidates1, target1) == [
    [2, 2, 2, 2],
    [2, 3, 3],
    [3, 5],
]
assert combination_sum(candidates2, target2) == []
