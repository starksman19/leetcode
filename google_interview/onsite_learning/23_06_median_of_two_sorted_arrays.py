# LeetCode: https://leetcode.com/problems/median-of-two-sorted-arrays/
# Given two sorted arrays nums1 and nums2, return the median of the two arrays.
# The solution should run in O(log(m + n)) time.

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A

        m, n = len(A), len(B)
        left, right = 0, m
        half = (m + n + 1) // 2

        while left <= right:
            i = (left + right) // 2
            j = half - i

            Aleft = A[i - 1] if i > 0 else float("-inf")
            Aright = A[i] if i < m else float("inf")

            Bleft = B[j - 1] if j > 0 else float("-inf")
            Bright = B[j] if j < n else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if (m + n) % 2 == 1:
                    return float(max(Aleft, Bleft))

                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            elif Aleft > Bright:
                right = i - 1
            else:
                left = i + 1


nums1 = [1, 3]
nums2 = [2]

print(Solution().findMedianSortedArrays(nums1, nums2))
assert Solution().findMedianSortedArrays(nums1, nums2) == 2.0

nums1 = [1, 2]
nums2 = [3, 4]

print(Solution().findMedianSortedArrays(nums1, nums2))
assert Solution().findMedianSortedArrays(nums1, nums2) == 2.5
