# LeetCode: https://leetcode.com/problems/binary-search/
# Given a sorted integer array nums and an integer target, return the index of target.
# If target is not present, return -1.
#
# The solution should run in O(log n) time.

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pass


nums = [-1, 0, 3, 5, 9, 12]
target = 9

print(Solution().search(nums, target))
assert Solution().search(nums, target) == 4

nums = [-1, 0, 3, 5, 9, 12]
target = 2

print(Solution().search(nums, target))
assert Solution().search(nums, target) == -1
