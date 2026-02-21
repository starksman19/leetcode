# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
#
# You must write an algorithm that runs in O(n) time.

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)
        ret = 1

        for item in nums_set:
            if item - 1 in nums_set:
                continue

            length = 1
            while item + length in nums_set:
                length += 1

            ret = max(ret, length)
        return ret


nums1 = [100, 4, 200, 1, 3, 2]
nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
nums3 = [1, 0, 1, 2]


print(Solution().longestConsecutive(nums1))
assert Solution().longestConsecutive(nums1) == 4


print(Solution().longestConsecutive(nums2))
assert Solution().longestConsecutive(nums2) == 9


print(Solution().longestConsecutive(nums3))
assert Solution().longestConsecutive(nums3) == 3
