# LeetCode: https://leetcode.com/problems/contains-duplicate/
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        pass


nums = [1, 2, 3, 1]

print(Solution().containsDuplicate(nums))
assert Solution().containsDuplicate(nums) == True

nums = [1, 2, 3, 4]

print(Solution().containsDuplicate(nums))
assert Solution().containsDuplicate(nums) == False
