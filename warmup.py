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
    """
    pass

# ---------------------------
# 2. DFS
def dfs_warmup(start, graph: dict):
    """
    Wejście:
        - start: wierzchołek startowy
        - graph: dict -> lista sąsiadów {node: [neighbors]}
    Wyjście:
        - lista odwiedzonych wierzchołków w kolejności DFS
    """
    pass

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
    """
    pass

# ---------------------------
# 4. Sliding Window
def sliding_window_warmup(arr: List[int], k: int):
    """
    Wejście:
        - arr: lista liczb
        - k: długość okna
    Wyjście:
        - maksimum sumy wartości w dowolnym oknie długości k
    """
    pass

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
    """
    pass

# ---------------------------
# 6. Stack
def stack_warmup(s: str):
    """
    Wejście:
        - s: string zawierający nawiasy (), {}, []
    Wyjście:
        - True jeśli wszystkie nawiasy są poprawnie zbalansowane
        - False w przeciwnym razie
    """
    pass

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
        - lista wartości w kolejności in-order
    """
    pass

# ---------------------------
# 8. Quickselect
def quickselect_warmup(arr: List[int], k: int):
    """
    Wejście:
        - arr: lista liczb
        - k: pozycja (1-indeksowana) najmniejszego elementu
    Wyjście:
        - wartość k-tego najmniejszego elementu
    """
    pass

# ---------------------------
# 9. Divide and Conquer
def divide_and_conquer_sum(arr: List[int], l: int, r: int):
    """
    Wejście:
        - arr: lista liczb
        - l, r: indeksy zakresu (0-based)
    Wyjście:
        - suma elementów arr[l:r+1]
    """
    pass

# ---------------------------
# 10. Dynamic Programming — LIS
def lis_warmup(nums: List[int]):
    """
    Wejście:
        - nums: lista liczb
    Wyjście:
        - długość najdłuższej rosnącej podsekwencji
    """
    pass

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
    """
    pass

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
    """
    pass
