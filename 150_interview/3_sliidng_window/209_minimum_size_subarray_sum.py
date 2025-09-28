from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        big_number = 1000000000
        start = 0
        suma = 0
        ret = big_number
        for index, val in enumerate(nums):
            suma += val
            while suma >= target:
                ret = min(ret, index - start + 1)
                suma -= nums[start]
                start += 1
        return 0 if ret == big_number else ret
