# Given an m x n matrix, return all elements in spiral order.

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        pass


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(Solution().spiralOrder(matrix))
assert Solution().spiralOrder(matrix) == [1, 2, 3, 6, 9, 8, 7, 4, 5]

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

print(Solution().spiralOrder(matrix))
assert Solution().spiralOrder(matrix) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
