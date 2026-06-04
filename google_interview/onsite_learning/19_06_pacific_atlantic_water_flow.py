# LeetCode: https://leetcode.com/problems/pacific-atlantic-water-flow/
# Given a matrix of heights, return all coordinates where water can flow to both the Pacific and Atlantic oceans.
# Water may flow from a cell to neighboring cells with height less than or equal to the current cell.

from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pass


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
