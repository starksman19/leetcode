# LeetCode: https://leetcode.com/problems/pacific-atlantic-water-flow/
# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean.
# The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.
#
# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).
#
# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west
# if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.
#
# Return a 2D list of grid coordinates result where result[i] = [ri, ci]
# denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
from collections import deque
from typing import List


class Solution:
    def pacificAtlantic_loops(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()
        pacific_que = deque([])
        atlantic_que = deque([])
        for i in range(cols):
            pacific_que.append((0, i))
            pacific_reachable.add((0, i))

        for i in range(1, rows):
            pacific_que.append((i, 0))
            pacific_reachable.add((i, 0))

        for i in range(cols):
            atlantic_que.append((rows - 1, i))
            atlantic_reachable.add((rows - 1, i))

        for i in range(rows - 1):
            atlantic_que.append((i, cols - 1))
            atlantic_reachable.add((i, cols - 1))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while pacific_que:
            r, c = pacific_que.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if heights[r][c] <= heights[nr][nc]:
                        if (nr, nc) not in pacific_reachable:
                            pacific_reachable.add((nr, nc))
                            pacific_que.append((nr, nc))

        while atlantic_que:
            r, c = atlantic_que.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if heights[r][c] <= heights[nr][nc]:
                        if (nr, nc) not in atlantic_reachable:
                            atlantic_reachable.add((nr, nc))
                            atlantic_que.append((nr, nc))

        ret = []
        for item in pacific_reachable:
            if item in atlantic_reachable:
                ret.append(list(item))
        return ret

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        def bfs(starts):
            visited = set(starts)
            q = deque(starts)

            while q:
                r, c = q.popleft()

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and (nr, nc) not in visited
                        and heights[nr][nc] >= heights[r][c]
                    ):
                        visited.add((nr, nc))
                        q.append((nr, nc))

            return visited

        pacific_starts = [(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)]

        atlantic_starts = [(rows - 1, c) for c in range(cols)] + [
            (r, cols - 1) for r in range(rows)
        ]

        pacific = bfs(pacific_starts)
        atlantic = bfs(atlantic_starts)
        ret = []
        for item in pacific:
            if item in atlantic:
                ret.append(list(item))
        return ret


heights = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4],
]

print(Solution().pacificAtlantic(heights))
assert sorted(Solution().pacificAtlantic(heights)) == sorted(
    [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
)

heights = [[1]]

print(Solution().pacificAtlantic(heights))
assert Solution().pacificAtlantic(heights) == [[0, 0]]
