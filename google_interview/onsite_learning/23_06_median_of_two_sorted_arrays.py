# Given two sorted arrays nums1 and nums2, return the median of the two arrays.
# The solution should run in O(log(m + n)) time.

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pass


nums1 = [1, 3]
nums2 = [2]

print(Solution().findMedianSortedArrays(nums1, nums2))
assert Solution().findMedianSortedArrays(nums1, nums2) == 2.0

nums1 = [1, 2]
nums2 = [3, 4]

print(Solution().findMedianSortedArrays(nums1, nums2))
assert Solution().findMedianSortedArrays(nums1, nums2) == 2.5
