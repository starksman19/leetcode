# Given an m x n matrix, return all elements of the matrix in spiral order.
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []
        if not matrix:
            return ret

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            for col in range(left, right + 1):
                ret.append(matrix[top][col])
            top += 1

            for i in range(top, bottom + 1):
                ret.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for col in range(right, left - 1, -1):
                    ret.append(matrix[bottom][col])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ret.append(matrix[i][left])
                left += 1
        return ret


matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
out1 = [1, 2, 3, 6, 9, 8, 7, 4, 5]

matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
out2 = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]


# print(Solution().spiralOrder(matrix1))
# assert Solution().spiralOrder(matrix1) == out1

print(Solution().spiralOrder(matrix2))
assert Solution().spiralOrder(matrix2) == out2
