# LeetCode: https://leetcode.com/problems/largest-rectangle-in-histogram/
# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1,
# return the area of the largest rectangle in the histogram.

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        stack = []
        ret = float("-inf")
        for index, val in enumerate(heights):
            while stack and heights[stack[-1]] > val:
                last_index = stack.pop()
                width = index - stack[-1] - 1 if stack else index
                new_rectangle = heights[last_index] * width
                ret = max(ret, new_rectangle)
            stack.append(index)
        while stack:
            last_index = stack.pop()

            width = len(heights) - stack[-1] - 1 if stack else len(heights)
            new_rectangle = heights[last_index] * width
            ret = max(ret, new_rectangle)
        return ret


heights = [2, 1, 2]

print(Solution().largestRectangleArea(heights))
assert Solution().largestRectangleArea(heights) == 3

heights = [1, 1]

print(Solution().largestRectangleArea(heights))
assert Solution().largestRectangleArea(heights) == 2

heights = [2, 1, 5, 6, 2, 3]

print(Solution().largestRectangleArea(heights))
assert Solution().largestRectangleArea(heights) == 10

heights = [2, 4]

print(Solution().largestRectangleArea(heights))
assert Solution().largestRectangleArea(heights) == 4
