# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
#
# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
#
# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially.
# The remaining elements of nums are not important as well as the size of nums.
# Return k.
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        i = 0  # slow pointer
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1

nums1 = [1,1,2]
nums2 = [0,0,1,1,1,2,2,3,3,4,0,1,1]


# print(Solution().removeDuplicates(nums1))
# assert Solution().removeDuplicates(nums1) == 2

print(Solution().removeDuplicates(nums2))
assert Solution().removeDuplicates(nums2) == 5

