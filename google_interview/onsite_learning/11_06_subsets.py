# LeetCode: https://leetcode.com/problems/subsets/
# Given an integer array nums with unique values, return all possible subsets.
# The answer may be returned in any order.

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        pass


def normalize(subsets: List[List[int]]) -> List[List[int]]:
    return sorted([sorted(subset) for subset in subsets])


nums = [1, 2, 3]

print(Solution().subsets(nums))
assert normalize(Solution().subsets(nums)) == [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

nums = [0]

print(Solution().subsets(nums))
assert normalize(Solution().subsets(nums)) == [[], [0]]
