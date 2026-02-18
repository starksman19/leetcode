# Given m x n grid filled with non-negative numbers, find a path from top left to bottom right,
# which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[float("inf") for _ in range(len(grid[0]))] for _ in range(len(grid))]
        dp[-1][-1] = grid[-1][-1]

        for i in range(len(dp)):
            dp[i].append(float("inf"))
        dp.append([float("inf") for _ in range(len(grid[0]))])

        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[0]) - 1, -1, -1):
                if dp[i][j] == float("inf"):
                    dp[i][j] = min(dp[i + 1][j], dp[i][j + 1]) + grid[i][j]
        return dp[0][0]


grid1 = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
grid2 = [[1, 2, 3], [4, 5, 6]]


print(Solution().minPathSum(grid1))
assert Solution().minPathSum(grid1) == 7
print(Solution().minPathSum(grid2))
assert Solution().minPathSum(grid2) == 12
