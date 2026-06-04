# Given an integer array nums and a window size k, return the maximum value in each sliding window.

from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pass


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

print(Solution().maxSlidingWindow(nums, k))
assert Solution().maxSlidingWindow(nums, k) == [3, 3, 5, 5, 6, 7]

nums = [1]
k = 1

print(Solution().maxSlidingWindow(nums, k))
assert Solution().maxSlidingWindow(nums, k) == [1]
