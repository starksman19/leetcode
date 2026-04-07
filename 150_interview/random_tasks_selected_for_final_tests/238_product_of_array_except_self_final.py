# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# You must write an algorithm that runs in O(n) time and without using the division operation.


from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sum_from_left = [1] * n
        sum_from_right = [1] * n
        for i in range(1, n):
            sum_from_left[i] = sum_from_left[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            sum_from_right[i] = sum_from_right[i + 1] * nums[i + 1]
        ret = []
        for i in range(n):
            ret.append(sum_from_left[i] * sum_from_right[i])
        return ret


nums1 = [1, 2, 3, 4]
nums2 = [-1, 1, 0, -3, 3]
print(Solution().productExceptSelf(nums1))
assert Solution().productExceptSelf(nums1) == [24, 12, 8, 6]

print(Solution().productExceptSelf(nums2))
assert Solution().productExceptSelf(nums2) == [0, 0, 9, 0, 0]
