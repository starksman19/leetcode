# You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.
#
# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:
#
# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                current_end = farthest
                jumps += 1

        return jumps


nums1 = [2, 3, 1, 1, 4]
nums2 = [2, 3, 0, 1, 4]
nums3 = [0]


print(Solution().jump(nums1))
assert Solution().jump(nums1) == 2

print(Solution().jump(nums2))
assert Solution().jump(nums2) == 2

print(Solution().jump(nums3))
assert Solution().jump(nums3) == 0
