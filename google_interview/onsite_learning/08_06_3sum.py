# LeetCode: https://leetcode.com/problems/3sum/
# Given an integer array nums, return all unique triplets [nums[i], nums[j], nums[k]]
# such that i, j and k are different indices and the three values sum to 0.
#
# The solution set must not contain duplicate triplets.

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pass


def normalize(triplets: List[List[int]]) -> List[List[int]]:
    return sorted([sorted(triplet) for triplet in triplets])


nums = [-1, 0, 1, 2, -1, -4]

print(Solution().threeSum(nums))
assert normalize(Solution().threeSum(nums)) == [[-1, -1, 2], [-1, 0, 1]]

nums = [0, 1, 1]

print(Solution().threeSum(nums))
assert normalize(Solution().threeSum(nums)) == []
