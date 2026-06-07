# LeetCode: https://leetcode.com/problems/trapping-rain-water/
# Given an array of non-negative bar heights, return how much rain water can be trapped after raining.

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        sum_of_water = 0
        current_lowest_side = min(height[0], height[-1])
        pointer_left, pointer_right = 0, len(height) - 1

        while pointer_left < pointer_right:
            if height[pointer_left] < height[pointer_right]:
                if height[pointer_left] < current_lowest_side:
                    sum_of_water += current_lowest_side - height[pointer_left]
                else:
                    current_lowest_side = height[pointer_left]
                pointer_left += 1
            else:
                if height[pointer_right] < current_lowest_side:
                    sum_of_water += current_lowest_side - height[pointer_right]
                else:
                    current_lowest_side = height[pointer_right]
                pointer_right -= 1

        return sum_of_water

    def trap_gpt(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                water += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                water += right_max - height[right]
                right -= 1

        return water


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

print(Solution().trap(height))
assert Solution().trap(height) == 6

height = [4, 2, 0, 3, 2, 5]

print(Solution().trap(height))
assert Solution().trap(height) == 9
