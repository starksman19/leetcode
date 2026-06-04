# Given bar heights in a histogram, return the area of the largest rectangle that can be formed.

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        pass


heights = [2, 1, 5, 6, 2, 3]

print(Solution().largestRectangleArea(heights))
assert Solution().largestRectangleArea(heights) == 10

heights = [2, 4]

print(Solution().largestRectangleArea(heights))
assert Solution().largestRectangleArea(heights) == 4
