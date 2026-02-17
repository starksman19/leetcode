# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
# Constraints:
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] is '0' or '1'.

from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not len(matrix):
            return 0
        elif len(matrix) == 1:
            return 1 if "1" in matrix[0] else 0

        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        dp[0] = [int(val) for val in matrix[0]]
        for i in range(len(dp)):
            dp[i][0] = int(matrix[i][0])

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == "0":
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        val = max([max(l) for l in dp])
        return val * val


# matrix = [
#     ["1", "0", "1", "0", "0"],
#     ["1", "0", "1", "1", "1"],
#     ["1", "1", "1", "1", "1"],
#     ["1", "0", "0", "1", "0"],
# ]
# print(Solution().maximalSquare(matrix))
# assert Solution().maximalSquare(matrix) == 4
#
# matrix = [["0", "1"], ["1", "0"]]
# print(Solution().maximalSquare(matrix))
# assert Solution().maximalSquare(matrix) == 1

matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "1", "1", "1"],
]
print(Solution().maximalSquare(matrix))
assert Solution().maximalSquare(matrix) == 9
