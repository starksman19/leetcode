from typing import List


# mam mapę visited -> i robię rozpszetszenieniae się

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows_len = len(grid)
        cols_len = len(grid[0])
        visited = [[0] * len(grid[0]) for _ in range(len(grid))]

        def dfs(grd, i2, j2, isl):
            nonlocal visited
            nonlocal rows_len
            nonlocal cols_len

            if i2 >= rows_len or i2 < 0 or j2 >= cols_len or j2 < 0:
                return
            if visited[i2][j2] == 1 or grd[i2][j2] == "0":
                return

            visited[i2][j2] = 1
            isl.append(1)

            dfs(grd, i2+1, j2, isl)
            dfs(grd, i2-1, j2, isl)
            dfs(grd, i2, j2+1, isl)
            dfs(grd, i2, j2-1, isl)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                island = []
                if visited[i][j] == 1:
                    continue
                elif grid[i][j] == '0':
                    visited[i][j] = 1
                else:
                    dfs(grid, i, j, island)
                    if island:
                        islands += 1

        return islands


test_grid = [
    ["1", "1", "1"],
    ["0", "1", "0"],
    ["1", "1", "1"],
]

print(Solution().numIslands(test_grid))
assert Solution().numIslands(test_grid) == 1
