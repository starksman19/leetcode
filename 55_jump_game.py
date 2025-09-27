# You are given an integer array nums. You are initially positioned at the array's first index,
# and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.
# 1 <= nums.length <= 104
# 0 <= nums[i] <= 105
from functools import lru_cache
from typing import List


class Solution:
    def canJump_bad(self, nums: List[int]) -> bool:
        @lru_cache
        def dfs(index: int) -> bool:
            if index >= len(nums) - 1:
                return True
            elif nums[index] == 0:
                return False
            n = nums[index]
            ret = []
            for i in range(1, n + 1):
                ret.append(dfs(index + i))
            return any(ret)

        if 0 in nums:
            return dfs(0)
        else:
            return True

    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i, jump in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + jump)
            if max_reach >= len(nums) - 1:
                return True
        return True


nums1 = [2, 3, 1, 1, 4]
nums2 = [3, 2, 1, 0, 4]
nums3 = [0, 1]
nums4 = [0]
nums5 = [2, 0]


print(Solution().canJump(nums1))
assert Solution().canJump(nums1) == True

print(Solution().canJump(nums2))
assert Solution().canJump(nums2) == False

print(Solution().canJump(nums3))
assert Solution().canJump(nums3) == False

print(Solution().canJump(nums4))
assert Solution().canJump(nums4) == True

print(Solution().canJump(nums5))
assert Solution().canJump(nums5) == True
