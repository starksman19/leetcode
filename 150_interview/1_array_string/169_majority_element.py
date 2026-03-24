# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        val_map = {}
        for i in range(len(nums)):
            if nums[i] not in val_map:
                val_map[nums[i]] = 1
            else:
                val_map[nums[i]] += 1
        for key, val in val_map.items():
            if val > len(nums) / 2:
                return key
        return None

    def majorityElement_but_better(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate


nums1 = [3, 2, 3]
nums2 = [2, 2, 1, 1, 1, 2, 2]


print(Solution().majorityElement(nums1))
assert Solution().majorityElement(nums1) == 3

print(Solution().majorityElement(nums2))
assert Solution().majorityElement(nums2) == 2
