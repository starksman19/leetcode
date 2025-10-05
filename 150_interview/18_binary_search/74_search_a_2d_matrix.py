# You are given an m x n integer matrix with the following two properties:
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.
# You must write a solution in O(log(m * n)) time complexity.
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104
from typing import List


class Solution:
    def searchMatrix_2_searches(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        start, end = 0, rows - 1
        row = -10
        while start <= end:
            mid = (start + end) // 2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                row = matrix[mid]
                break
            elif matrix[mid][0] >= target:
                end = mid - 1
            elif matrix[mid][0] <= target:
                start = mid + 1

        if row == -10:
            return False

        start, end = 0, cols - 1

        while start <= end:
            mid = (start + end) // 2
            if row[mid] == target:
                return True
            elif row[mid] >= target:
                end = mid - 1
            elif row[mid] <= target:
                start = mid + 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        # Binary search over the entire matrix by treating it as a 1D array
        left, right = 0, m * n - 1
        while left <= right:
            mid = (left + right) // 2
            # Map 1D index back to 2D
            row, col = divmod(mid, n)
            val = matrix[row][col]
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False


matrix1 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target1 = 3
matrix2 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target2 = 13


# print(Solution().searchMatrix(matrix1, target1))
# assert Solution().searchMatrix(matrix1, target1) == True
#
# print(Solution().searchMatrix(matrix2, target2))
# assert Solution().searchMatrix(matrix2, target2) == False


print(Solution().searchMatrix_2_searches(matrix1, target1))
assert Solution().searchMatrix_2_searches(matrix1, target1) == True

print(Solution().searchMatrix_2_searches(matrix2, target2))
assert Solution().searchMatrix_2_searches(matrix2, target2) == False
