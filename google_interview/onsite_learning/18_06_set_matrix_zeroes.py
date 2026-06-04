# Given an m x n matrix, if an element is 0, set its entire row and column to 0 in-place.

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        pass


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

Solution().setZeroes(matrix)
print(matrix)
assert matrix == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]

Solution().setZeroes(matrix)
print(matrix)
assert matrix == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
