# LeetCode: https://leetcode.com/problems/trapping-rain-water/
# Given an array of non-negative bar heights, return how much rain water can be trapped after raining.

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        pass


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

print(Solution().trap(height))
assert Solution().trap(height) == 6

height = [4, 2, 0, 3, 2, 5]

print(Solution().trap(height))
assert Solution().trap(height) == 9
