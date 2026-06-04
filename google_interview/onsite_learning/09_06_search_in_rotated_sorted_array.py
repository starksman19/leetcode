# LeetCode: https://leetcode.com/problems/search-in-rotated-sorted-array/
# Given a sorted array rotated at an unknown pivot and an integer target,
# return the target index, or -1 if target is not present.
#
# The solution should run in O(log n) time.

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pass


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

print(Solution().search(nums, target))
assert Solution().search(nums, target) == 4

nums = [4, 5, 6, 7, 0, 1, 2]
target = 3

print(Solution().search(nums, target))
assert Solution().search(nums, target) == -1
