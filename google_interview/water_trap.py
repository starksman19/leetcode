# You are given an array height where height[i] represents the height of a bar at index i.
#
# Each bar has width 1.
#
# After raining, water can be trapped between the bars.
#
# Return the total amount of trapped water.
#
# Example 1:
# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# ru
# Example 2:
# height = [4,2,0,3,2,5]
# Output: 9

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        pass


height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
height2 = [4, 2, 0, 3, 2, 5]
height3 = [1, 0, 2]

solution = Solution()

assert solution.trap(height1) == 6
assert solution.trap(height2) == 9
assert solution.trap(height3) == 1

print("All tests passed!")
