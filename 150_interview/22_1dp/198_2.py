# You are a professional robber planning to rob houses along a street
# Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected
# and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) <= 2:
            return max(nums)
        size = len(nums)
        dp = [float("-inf")] * len(nums)
        dp[0], dp[1] = nums[0], nums[1]
        for i in range(2, size):
            dp[i] = max(nums[i] + dp[i - 2], nums[i - 1])
        return int(max(dp))


if __name__ == "__main__":
    nums1 = [1, 2, 3, 1]
    nums2 = [2, 7, 9, 3, 1]
    assert (Solution().rob(nums1)) == 4
    assert (Solution().rob(nums2)) == 12
    assert (Solution().rob([])) == 0
