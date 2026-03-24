# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        pass


nums1 = [3, 2, 3]
nums2 = [2, 2, 1, 1, 1, 2, 2]


print(Solution().majorityElement(nums1))
assert Solution().majorityElement(nums1) == 3

print(Solution().majorityElement(nums2))
assert Solution().majorityElement(nums2) == 2
