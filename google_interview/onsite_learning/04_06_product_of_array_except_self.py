# LeetCode: https://leetcode.com/problems/product-of-array-except-self/
# Given an integer array nums, return an array answer such that answer[i]
# is equal to the product of all the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# You must write an algorithm that runs in O(n) time and without using the division operation.


from typing import List


class Solution:
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sum_from_left = [1] * len(nums)
        sum_from_right = [1] * len(nums)
        ret = []
        for i in range(1, n):
            sum_from_left[i] = nums[i - 1] * sum_from_left[i - 1]
        for i in range(n - 2, -1, -1):
            sum_from_right[i] = nums[i + 1] * sum_from_right[i + 1]

        for i in range(n):
            ret.append(sum_from_left[i] * sum_from_right[i])

        return ret

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sum_from_left = [1] * len(nums)
        ret = []
        for i in range(1, n):
            sum_from_left[i] = nums[i - 1] * sum_from_left[i - 1]

        right = 1
        for i in range(n - 1, -1, -1):
            ret.append(sum_from_left[i] * right)
            right *= nums[i]
        ret = ret[::-1]
        return ret


nums = [1, 2, 3, 4]

print(Solution().productExceptSelf(nums))
assert Solution().productExceptSelf(nums) == [24, 12, 8, 6]

nums = [-1, 1, 0, -3, 3]

print(Solution().productExceptSelf(nums))
assert Solution().productExceptSelf(nums) == [0, 0, 9, 0, 0]
