from collections import deque
from typing import List, Optional
import heapq


# ---------------------------
# 1. BFS
def bfs_warmup(start, graph: dict):
    """
    PROBLEM:
    Masz graf nieskierowany lub skierowany reprezentowany jako lista sąsiedztwa.
    Twoim zadaniem jest przejść graf metodą BFS (Breadth-First Search),
    czyli przeszukiwania wszerz.

    BFS odwiedza wierzchołki poziomami:
    - najpierw startowy
    - potem wszystkich jego sąsiadów
    - potem sąsiadów sąsiadów itd.

    Wejście:
        - start: wierzchołek początkowy
        - graph: dict {node: [neighbors]}

    Wyjście:
        - lista odwiedzonych wierzchołków w kolejności BFS
    """
    que = deque([start])
    res = []
    while que:
        node = que.popleft()
        res.append(node)
        for val in graph[node]:
            que.append(val)
    return res


assert bfs_warmup(1, {1: [2, 3], 2: [4], 3: [], 4: []}) == [1, 2, 3, 4]


# ---------------------------
# 2. DFS
def dfs_warmup(start, graph: dict):
    """
    PROBLEM:
    Przejdź graf metodą DFS (Depth-First Search), czyli "w głąb".

    DFS działa tak:
    - idziesz jak najgłębiej jedną ścieżką
    - dopiero potem się cofasz

    Wejście:
        - start: wierzchołek początkowy
        - graph: dict {node: [neighbors]}

    Wyjście:
        - lista odwiedzonych wierzchołków w kolejności DFS
    """
    ret = []

    def dfs(node):
        if node is None:  # not needed in this case, wont enter here if neghnour list is empty
            return
        ret.append(node)
        for val in graph[node]:
            dfs(val)

    dfs(start)
    return ret


assert dfs_warmup(1, {1: [2, 3], 2: [4], 3: [], 4: []}) == [1, 2, 4, 3]


# ---------------------------
# 3. Binary Search
def binary_search_warmup(arr: List[int], target: int):
    """
    PROBLEM:
    Masz posortowaną tablicę liczb i chcesz znaleźć indeks elementu.

    Binary Search:
    - porównujesz środek
    - odrzucasz połowę tablicy
    - powtarzasz

    Wejście:
        - arr: posortowana lista
        - target: liczba do znalezienia

    Wyjście:
        - indeks elementu
        - -1 jeśli nie istnieje

    Złożoność:
        - O(log n)
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
    PROBLEM:
    Znajdź maksymalną sumę podtablicy długości k.

    Naiwne rozwiązanie:
        - licz sumę za każdym razem → O(n*k)

    Lepsze:
        - przesuwaj "okno"
        - odejmij lewy element, dodaj prawy

    Wejście:
        - arr: lista liczb
        - k: długość okna

    Wyjście:
        - maksymalna suma

    Złożoność:
        - O(n)

    """
    ret = float("-inf")
    left, right = 0, k
    for i in range(len(arr)):
        ret = max(ret, sum(arr[left + i : right + i]))
    return ret


assert sliding_window_warmup([2, 1, 5, 1, 3, 2], 3) == 9


# ---------------------------
# 5. Two Pointers
def two_pointers_warmup(arr: List[int], target: int):
    """
    PROBLEM:
    Sprawdź, czy istnieją dwie liczby w posortowanej tablicy,
    których suma daje target.

    Podejście:
        - jeden wskaźnik na początku
        - drugi na końcu
        - przesuwaj w zależności od sumy

    Wejście:
        - arr: posortowana lista
        - target: suma

    Wyjście:
        - True / False

    Złożoność:
        - O(n)
    """
    left, right = 0, len(arr) - 1

    while left < right:
        val = arr[left] + arr[right]
        if val == target:
            return True
        if val > target:
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
    PROBLEM:
    Sprawdź, czy nawiasy są poprawnie zbalansowane.

    Reguły:
        - każdy otwierający musi mieć zamykający
        - kolejność musi się zgadzać

    Przykłady:
        ()[]{} → OK
        ([)] → NIE

    Wejście:
        - string z nawiasami

    Wyjście:
        - True / False
    """
    a_map = {"}": "{", "]": "[", ")": "("}
    stack = []
    for item in s:
        if item in a_map.values():
            stack.append(item)
        elif not stack or a_map[item] != stack.pop():
            return False

    return True if not stack else False


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
    PROBLEM:
    Wykonaj przejście drzewa binarnego w kolejności inorder:

        LEWY → KORZEŃ → PRAWY

    Wejście:
        - root drzewa

    Wyjście:
        - lista wartości
    """
    ret = []

    def inorder(node: TreeNode):
        if not node:
            return
        inorder(node.left)
        ret.append(node.val)
        inorder(node.right)

    inorder(root)
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
    PROBLEM:
    Znajdź k-ty największy element w tablicy.

    Nie sortujemy całej tablicy!
    Używamy podejścia podobnego do quicksorta (partition).

    Wejście:
        - arr
        - k (1-indexed)

    Wyjście:
        - wartość k-tego największego elementu

    Średnia złożoność:
        - O(n)
    """
    k = len(arr) - k

    def partition(left, right):
        pointer, pivot = left, arr[right]
        for i in range(left, right):
            if arr[i] < pivot:
                arr[pointer], arr[i] = arr[i], arr[pointer]
                pointer += 1
        arr[right], arr[pointer] = arr[pointer], arr[right]
        if pointer == k:
            return arr[pointer]
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
    PROBLEM:
    Oblicz sumę elementów w przedziale [l, r].

    Podejście:
        - podziel na pół
        - policz rekurencyjnie
        - zsumuj wyniki

    Wejście:
        - arr
        - indeksy l, r

    Wyjście:
        - suma

    """

    def div_and_conq(left, right):
        if left == right:
            return arr[left]
        mid = (left + right) // 2
        return div_and_conq(left, mid) + div_and_conq(mid + 1, right)

    return div_and_conq(l, r)


assert divide_and_conquer_sum([1, 2, 3, 4], 0, 3) == 10
assert divide_and_conquer_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 3) == 10
assert divide_and_conquer_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 4, 8) == 35


# ---------------------------
# 10. LIS
def lis_warmup(nums: List[int]):
    """
    PROBLEM:
    Znajdź długość najdłuższej rosnącej podsekwencji (LIS).

    Podsekwencja ≠ podciąg (można pomijać elementy)

    Przykład:
        [10,9,2,5,3,7,101,18] → LIS = 4 (np. 2,3,7,101)

    Podejścia:
        - DP O(n^2)
        - lub O(n log n)

    Wyjście:
        - długość LIS
    """
    n = len(nums)
    dp = [1] * n

    for i in range(1, len(nums)):
        for j in range(0, i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp[-1]


assert lis_warmup([10, 9, 2, 5, 3, 7, 101, 18]) == 4


# ---------------------------
# 11. Knapsack
def knapsack_warmup(weights: List[int], values: List[int], W: int):
    """
    PROBLEM:
    Klasyczny plecak 0/1.

    Masz:
        - wagi
        - wartości
        - maksymalną pojemność

    Każdy przedmiot można wziąć maksymalnie raz.

    Cel:
        - maksymalizować wartość

    Wejście:
        - weights
        - values
        - W

    Wyjście:
        - maksymalna wartość
    """
    dp = [float("-inf")] * (W + 1)
    dp[0] = 0
    for i in range(len(weights)):
        for w in range(W, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[-1]


assert knapsack_warmup([1, 3, 4, 5], [1, 4, 5, 7], 7) == 9


# ---------------------------
# 12. Coin Change
def coin_change_warmup(coins: List[int], amount: int):
    """
    PROBLEM:
    Znajdź minimalną liczbę monet potrzebną do uzyskania danej kwoty.

    Możesz używać monet wielokrotnie.

    Jeśli się nie da → zwróć -1.

    Wejście:
        - coins
        - amount

    Wyjście:
        - minimalna liczba monet

    """
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for i in range(len(coins)):
        for j in range(coins[i], len(dp)):
            dp[j] = min(dp[j], 1 + dp[j - coins[i]])
    return dp[-1] if dp[-1] != float("inf") else -1


assert coin_change_warmup([1, 2, 5], 11) == 3
assert coin_change_warmup([2, 6, 8, 10], 17) == -1


# ---------------------------
# 13. Backtracking
def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """
    PROBLEM:
    Znajdź wszystkie kombinacje liczb, które sumują się do target.

    Zasady:
        - możesz używać elementów wielokrotnie
        - kolejność nie ma znaczenia
        - wynik: lista kombinacji

    Przykład:
        [2,3,5], target=8 →
        [2,2,2,2], [2,3,3], [3,5]

    Podejście:
        - backtracking (DFS)
    """
    ret = []

    def backtrack(curr_sum: int, curr_array: List[int], start_index: int):
        if curr_sum == target:
            ret.append(curr_array[:])
            return
        elif curr_sum > target:
            return
        for i in range(start_index, len(candidates)):
            curr_array.append(candidates[i])
            curr_sum += candidates[i]
            backtrack(curr_sum, curr_array, i)
            curr_array.pop()
            curr_sum -= candidates[i]

    backtrack(0, [], 0)
    return ret


assert combination_sum([2, 3, 5], 8) == [
    [2, 2, 2, 2],
    [2, 3, 3],
    [3, 5],
]
assert combination_sum([2], 1) == []


# ---------------------------
# 14. Heap / Priority Queue (Top K Elements)
def top_k_elements_warmup(nums: List[int], k: int):
    """
    PROBLEM:
    Masz nieposortowaną listę liczb i chcesz znaleźć k największych elementów.

    NIE sortujemy całej tablicy (to byłoby O(n log n)).

    Zamiast tego używamy struktury:
        - heap (kolejka priorytetowa) z modułu heapq

    Podejście:
        - utrzymujemy min-heap o rozmiarze k
        - każdy nowy element dodajemy do heap
        - jeśli heap przekroczy rozmiar k → usuwamy najmniejszy

    Dzięki temu w heap zostają tylko k największe elementy.

    Wejście:
        - nums: lista liczb
        - k: liczba elementów do zwrócenia

    Wyjście:
        - lista k największych elementów (kolejność dowolna)

    Złożoność:
        - O(n log k)
    """
    top_k = []
    for num in nums:
        if len(top_k) < k:
            heapq.heappush(top_k, num)
        else:
            heapq.heappushpop(top_k, num)
    return top_k


assert top_k_elements_warmup([3, 2, 1, 5, 6, 4], 2) == [5, 6] or top_k_elements_warmup(
    [3, 2, 1, 5, 6, 4], 2
) == [6, 5]


class RaceResults:
    def __init__(self):
        """
        PROBLEM:
        Projektujemy strukturę danych do przechowywania wyników zawodników.

        Chcemy obsługiwać bardzo szybkie operacje:
            - dodawanie / aktualizacja wyniku zawodnika
            - pobranie wyniku po imieniu
            - pobranie zawodnika po wyniku
            - pobranie aktualnego TOP 3 zawodników

        Wymagania wydajnościowe:
            - wyszukiwanie po imieniu → O(1)
            - wyszukiwanie po wyniku → O(1)
            - szybkie pobieranie najlepszych wyników

        Używane struktury:
            - dict:
                name_to_score
                score_to_name

            - heapq:
                max-heap do przechowywania najlepszych wyników

        Dodatkowo:
            - przechowujemy cache TOP3
            - heap może zawierać stare wpisy
            - podczas odczytu ignorujemy nieaktualne rekordy

        Idea:
            Python posiada tylko min-heap,
            dlatego używamy ujemnych wartości,
            aby symulować max-heap.

        Przykład:
            insert("Anna", 98.5)
            insert("Tom", 88.0)

            get_top3()
            -> [("Anna", 98.5), ("Tom", 88.0)]
        """
        self.top_3 = []
        self.heapq = []
        self.score_by_name = {}
        self.name_by_score = {}

    def insert(self, name: str, score: float):
        """
        PROBLEM:
        Dodaje nowy wynik zawodnika lub aktualizuje istniejący.

        Jeśli zawodnik już istnieje:
            - stary wynik zostaje zastąpiony nowym

        Operacje:
            - aktualizacja dict
            - dodanie wpisu do max-heap
            - odświeżenie cache TOP3

        Wejście:
            - name: imię zawodnika
            - score: wynik zawodnika

        Złożoność:
            - O(log n)
        """
        if name in self.score_by_name:
            old_score = self.score_by_name[name]
            del self.name_by_score[old_score]

        self.score_by_name[name] = score
        self.name_by_score[score] = name

        heapq.heappush(self.heapq, (-score, name))
        self._update_top3()

    def _update_top3(self):
        """
        PROBLEM:
        Aktualizuje cache najlepszych 3 zawodników.

        Podejście:
            - pobieramy elementy z max-heap
            - ignorujemy stare / nieaktualne wpisy
            - zapisujemy tylko aktualne TOP3
            - przywracamy elementy do heap

        Dzięki temu:
            - get_top3() działa bardzo szybko

        Złożoność:
            - O(log n)
        """
        temp = []
        used = []

        while self.heapq and len(temp) < 3:
            value, name = heapq.heappop(self.heapq)
            value = -value

            if self.score_by_name[name] == value:
                temp.append((name, value))
                used.append((-value, name))

        for item in used:
            heapq.heappush(self.heapq, item)
        self.top_3 = temp

    def get_top3(self):
        """
        PROBLEM:
        Zwraca aktualnych 3 najlepszych zawodników.

        Wyjście:
            - lista:
                [(name, score), ...]

        Złożoność:
            - O(1)
        """
        return self.top_3

    def get_score_by_name(self, name: str):
        """
        PROBLEM:
        Zwraca wynik zawodnika na podstawie imienia.

        Podejście:
            - bezpośredni dostęp przez dict

        Wejście:
            - name: imię zawodnika

        Wyjście:
            - score lub None

        Złożoność:
            - O(1)
        """
        return self.score_by_name.get(name)

    def get_name_by_score(self, score: float):
        """
        PROBLEM:
        Zwraca zawodnika na podstawie wyniku.

        Podejście:
            - bezpośredni dostęp przez dict

        Wejście:
            - score: wynik

        Wyjście:
            - name lub None

        Złożoność:
            - O(1)
        """
        return self.name_by_score.get(score)


rr = RaceResults()

rr.insert("Anna", 98.5)
assert rr.get_score_by_name("Anna") == 98.5

rr.insert("Tom", 88.0)
rr.insert("Kate", 91.2)

top3 = rr.get_top3()
assert ("Anna", 98.5) in top3
assert ("Tom", 88.0) in top3
assert ("Kate", 91.2) in top3

assert rr.get_name_by_score(91.2) == "Kate"

# aktualizacja wyniku
rr.insert("Tom", 99.9)

assert rr.get_score_by_name("Tom") == 99.9
assert rr.get_name_by_score(99.9) == "Tom"

top3 = rr.get_top3()
assert top3[0] == ("Tom", 99.9)

# więcej zawodników
rr.insert("Mike", 77.0)
rr.insert("Eva", 95.4)

top3 = rr.get_top3()

assert ("Tom", 99.9) in top3
assert ("Anna", 98.5) in top3
assert ("Eva", 95.4) in top3

# sprawdzenie nadpisania starego wyniku
rr.insert("Anna", 50.0)

assert rr.get_score_by_name("Anna") == 50.0

top3 = rr.get_top3()

assert ("Anna", 98.5) not in top3
assert ("Tom", 99.9) in top3

# pojedynczy zawodnik
single = RaceResults()

single.insert("Solo", 100.0)

assert single.get_top3() == [("Solo", 100.0)]

# brak zawodnika
assert single.get_score_by_name("Ghost") is None

# brak wyniku
assert single.get_name_by_score(999.0) is None
