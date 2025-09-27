# You are given an integer array nums. You are initially positioned at the array's first index,
# and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.
# 1 <= nums.length <= 104
# 0 <= nums[i] <= 105


from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pass


nums1 = [2, 3, 1, 1, 4]

nums2 = [3, 2, 1, 0, 4]

print(Solution().canJump(nums1))
assert Solution().canJump(nums1) == True

print(Solution().canJump(nums2))
assert Solution().canJump(nums2) == False
