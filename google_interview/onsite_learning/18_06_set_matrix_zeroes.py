# LeetCode: https://leetcode.com/problems/set-matrix-zeroes/
# Given an m x n matrix, if an element is 0, set its entire row and column to 0 in-place.

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        zero_rows = set()
        zero_cols = set()
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    zero_rows.add(row)
                    zero_cols.add(col)

        for item in zero_rows:
            for i in range(n):
                matrix[item][i] = 0
        for item in zero_cols:
            for i in range(m):
                matrix[i][item] = 0


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

Solution().setZeroes(matrix)
print(matrix)
assert matrix == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]

Solution().setZeroes(matrix)
print(matrix)
assert matrix == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
