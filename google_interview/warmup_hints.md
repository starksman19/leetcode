# 🧠 Algorithm Warmup — Step-by-Step Hints

---

## 1. BFS (Breadth-First Search)

**Cel:** przejść graf poziomami

**Hinty:**
1. Użyj `deque` jako kolejki.
2. Wrzuć `start` do kolejki.
3. Stwórz `visited = set()`.
4. Dopóki kolejka nie jest pusta:
   - zdejmij element (`popleft`)
   - jeśli nie był odwiedzony:
     - dodaj do wyniku
     - oznacz jako visited
     - dodaj sąsiadów do kolejki
5. Uważaj na duplikaty!

---

## 2. DFS (Depth-First Search)

**Cel:** przejść graf w głąb

**Hinty:**
1. Użyj rekurencji.
2. Stwórz `visited`.
3. Funkcja `dfs(node)`:
   - jeśli odwiedzony → return
   - dodaj do visited i wyniku
   - rekurencyjnie odwiedź sąsiadów
4. Wywołaj `dfs(start)`

---

## 3. Binary Search

**Cel:** znaleźć element w posortowanej tablicy

**Hinty:**
1. `left = 0`, `right = len(arr) - 1`
2. Dopóki `left <= right`:
   - `mid = (left + right) // 2`
3. Jeśli trafiony → zwróć indeks
4. Jeśli za duży → szukaj w lewej połowie
5. Jeśli za mały → w prawej
6. Brak → `-1`

---

## 4. Sliding Window

**Cel:** maksymalna suma okna długości `k`

**Hinty:**
1. Policz sumę pierwszego okna
2. Iteruj:
   - dodaj nowy element
   - odejmij stary
3. Aktualizuj maksimum

---

## 5. Two Pointers

**Cel:** znaleźć parę o sumie `target`

**Hinty:**
1. `left = 0`, `right = n-1`
2. Dopóki `left < right`:
   - licz sumę
3. Jeśli OK → True
4. Za duża → `right--`
5. Za mała → `left++`

---

## 6. Stack (Balanced Parentheses)

**Cel:** sprawdzić poprawność nawiasów

**Hinty:**
1. Mapa: zamykający → otwierający
2. Iteruj:
   - otwierający → push
   - zamykający:
     - sprawdź stos
     - sprawdź dopasowanie
3. Na końcu stos musi być pusty

---

## 7. Inorder Traversal (Binary Tree)

**Cel:** LEWY → ROOT → PRAWY

**Hinty:**
1. Rekurencja:
   - jeśli None → return
   - lewo
   - root
   - prawo

---

## 8. Quickselect

**Cel:** k-ty największy element

**Hinty:**
1. Zamień na k-ty najmniejszy:
   - `k = len(arr) - k`
2. Partition:
   - pivot
   - mniejsze w lewo
3. Sprawdź pivot index:
   - == k → wynik
   - > k → lewo
   - < k → prawo

---

## 9. Divide & Conquer

**Cel:** suma przedziału

**Hinty:**
1. Base case: `l == r`
2. Podziel:
   - `mid`
3. Rekurencja:
   - lewa + prawa

---

## 10. LIS (Longest Increasing Subsequence)

**Cel:** najdłuższa rosnąca podsekwencja

**Hinty (O(n²)):**
1. `dp[i] = LIS kończące się na i`
2. Start: same 1
3. Dla każdego i:
   - sprawdź j < i
   - jeśli rośnie:
     - `dp[i] = max(dp[i], dp[j] + 1)`
4. Wynik = max(dp)

---

## 11. Knapsack (0/1)

**Cel:** maksymalna wartość przy ograniczonej wadze

**Hinty:**
1. `dp[w] = max value`
2. Iteruj po przedmiotach
3. Iteruj wagę **od tyłu**
4. Update:
   - `dp[w] = max(dp[w], value + dp[w-weight])`

---

## 12. Coin Change

**Cel:** minimalna liczba monet

**Hinty:**
1. `dp[0] = 0`, reszta = inf
2. Dla każdej monety:
   - iteruj kwoty
   - `dp[j] = min(dp[j], dp[j-coin] + 1)`
3. Jeśli inf → -1

---

## 13. Backtracking (Combination Sum)

**Cel:** wszystkie kombinacje sumujące się do target

**Hinty:**
1. `backtrack(path, sum, start)`
2. Jeśli sum == target:
   - zapisz wynik
3. Jeśli sum > target:
   - stop
4. Iteruj od start:
   - dodaj element
   - rekurencja (ten sam index!)
   - usuń element

---

## Bonus: RaceResults System

**Cel:** szybki dostęp + top3

**Hinty:**
1. `name -> score` (dict)
2. `score -> name` (dict)
3. max-heap:
   - używaj `(-score, name)`
4. Nie usuwaj starych wpisów z heap (lazy removal)
5. Przy top3:
   - zdejmuj z heap
   - sprawdzaj aktualność
   - zbierz 3
   - przywróć heap

---

## 💡 Tip

Te zadania pokrywają:
- grafy
- wyszukiwanie
- DP
- struktury danych
- backtracking

Jeśli umiesz je bez patrzenia → jesteś bardzo blisko poziomu interview-ready 🚀