# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pass


nums1 = [2, 7, 11, 15]
target1 = 9

nums2 = [3, 2, 4]
target2 = 6

print(Solution().twoSum(nums1, target1))
assert Solution().twoSum(nums1, target1) == 9

print(Solution().twoSum(nums2, target2))
assert Solution().twoSum(nums2, target2) == 6
