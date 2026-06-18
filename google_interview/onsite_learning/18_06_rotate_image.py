# LeetCode: https://leetcode.com/problems/rotate-image/
# Given an n x n matrix representing an image, rotate the image 90 degrees clockwise in-place.

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix) - 1
        visited = set()
        for i in range(n):
            for j in range(n):
                if (i, j) not in visited:
                    row, col = i, j
                    start = (i, j)
                    val = matrix[row][col]

                    while True:
                        new_row = col
                        new_col = n - row
                        next_val = matrix[new_row][new_col]
                        matrix[new_row][new_col] = val

                        row = new_row
                        col = new_col
                        val = next_val
                        visited.add((row, col))
                        if (row, col) == start:
                            break

    def rotate2(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            row.reverse()


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

Solution().rotate(matrix)
print(matrix)
assert matrix == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]

Solution().rotate(matrix)
print(matrix)
assert matrix == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]


# r   c      r  c
# (0, 0) -> (0, 2) ->r-
# (0, 1) -> (1, 2)
# (0, 2) -> (2, 2)
#
# (2, 1) -> (1, 0)
#
# 0,0 -> (0, 2)
# 1,0 -> (0, 1)
# 2,0 -> (0, 0)
