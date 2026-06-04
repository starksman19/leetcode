# LeetCode: https://leetcode.com/problems/contains-duplicate/
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
from collections import defaultdict
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = defaultdict(int)  # -> można też na secie to zrobić
        for item in nums:
            visited[item] += 1
            if visited[item] > 1:
                return True
        return False

    def containsDuplicate_most_pythonic(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


nums = [1, 2, 3, 1]

print(Solution().containsDuplicate(nums))
assert Solution().containsDuplicate(nums) == True

nums = [1, 2, 3, 4]

print(Solution().containsDuplicate(nums))
assert Solution().containsDuplicate(nums) == False
