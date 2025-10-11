# Given m x n grid filled with non-negative numbers, find a path from top left to bottom right,
# which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[float("inf") for _ in range(n)] for _ in range(m)]
        dp[-1][-1] = grid[-1][-1]

        dp = [dp[i] + [float("inf")] for i in range(m)]
        dp.append([float("inf") for _ in range(n)])

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    continue
                dp[i][j] = int(min(grid[i][j] + dp[i + 1][j], grid[i][j] + dp[i][j + 1]))

        return int(dp[0][0])


grid1 = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
grid2 = [[1, 2, 3], [4, 5, 6]]


print(Solution().minPathSum(grid1))
assert Solution().minPathSum(grid1) == 7
print(Solution().minPathSum(grid2))
assert Solution().minPathSum(grid2) == 12
