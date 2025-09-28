# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
from typing import List


class Solution:
    def twoSum_bad(self, nums: List[int], target: int) -> List[int]:
        minus_first = {}
        for i in range(len(nums)):
            minus_first[i] = target - nums[i]
        for key, item in minus_first.items():
            for key2, item2 in minus_first.items():
                if key != key2:
                    if item + item2 == target:
                        return [key, key2]
        return None

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        minus_first = {}
        for index, val in enumerate(nums):
            diff = target - val
            if target - diff in minus_first:
                return [minus_first[target - diff], index]
            minus_first[diff] = index


nums1 = [2, 7, 11, 15]
target1 = 9

nums2 = [3, 2, 4]
target2 = 6

print(Solution().twoSum(nums1, target1))
assert Solution().twoSum(nums1, target1) == [0, 1]

print(Solution().twoSum(nums2, target2))
assert Solution().twoSum(nums2, target2) == [1, 2]
