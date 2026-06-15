# LeetCode: https://leetcode.com/problems/spiral-matrix/
# Given an m x n matrix, return all elements in spiral order.

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1
        ret = []

        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                ret.append(matrix[top][i])
            top += 1

            for i in range(top, bottom + 1):
                ret.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    ret.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ret.append(matrix[i][left])
                left += 1

        return ret


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(Solution().spiralOrder(matrix))
assert Solution().spiralOrder(matrix) == [1, 2, 3, 6, 9, 8, 7, 4, 5]

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

print(Solution().spiralOrder(matrix))
assert Solution().spiralOrder(matrix) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

matrix = [[1], [2], [3]]

print(Solution().spiralOrder(matrix))
assert Solution().spiralOrder(matrix) == [1, 2, 3]
