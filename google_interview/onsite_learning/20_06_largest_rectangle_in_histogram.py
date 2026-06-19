# LeetCode: https://leetcode.com/problems/largest-rectangle-in-histogram/
# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1,
# return the area of the largest rectangle in the histogram.

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
