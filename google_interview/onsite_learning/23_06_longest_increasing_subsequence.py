# LeetCode: https://leetcode.com/problems/longest-increasing-subsequence/
# Given an integer array nums, return the length of the longest strictly increasing subsequence.

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * (len(nums))
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


nums = [10, 9, 2, 5, 3, 7, 101, 18]

print(Solution().lengthOfLIS(nums))
assert Solution().lengthOfLIS(nums) == 4

nums = [0, 1, 0, 3, 2, 3]

print(Solution().lengthOfLIS(nums))
assert Solution().lengthOfLIS(nums) == 4
