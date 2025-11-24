# You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]).
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
#
# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
#
# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
#
# The testcases are generated so that the answer will be less than or equal to 2 * 109.

from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for d in dp:
            d.append(0)
        dp.append([0 for _ in range(n)])
        dp[m - 1][n - 1] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if not (i == m - 1 and j == n - 1):
                        dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
        return dp[0][0]


obstacleGrid1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
obstacleGrid2 = [[0, 1], [0, 0]]


print(Solution().uniquePathsWithObstacles(obstacleGrid1))
assert Solution().uniquePathsWithObstacles(obstacleGrid1) == 2

print(Solution().uniquePathsWithObstacles(obstacleGrid2))
assert Solution().uniquePathsWithObstacles(obstacleGrid2) == 1
