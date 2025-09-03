from typing import List

# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

# You may return the answer in any order.


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        out = []
        def backtrack(curr: list, start: int):
            if len(curr) == k:
                out.append(curr[:])
                return
            else:
                for val in range(start, n + 1):
                    curr.append(val)
                    backtrack(curr, val + 1)
                    curr.pop()

        v = []
        backtrack(v, 1)
        return out

n1 = 4
k1 = 2
expected = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

print(Solution().combine(n1, k1))
assert Solution().combine(n1, k1) == expected