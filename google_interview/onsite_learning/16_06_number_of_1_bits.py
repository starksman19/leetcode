# LeetCode: https://leetcode.com/problems/number-of-1-bits/
# Given an unsigned integer n, return the number of set bits in its binary representation.


class Solution:
    def hammingWeight(self, n: int) -> int:
        ret = 0
        while n > 0:
            ret += n % 2
            n = n // 2
        return ret


n = 11

print(Solution().hammingWeight(n))
assert Solution().hammingWeight(n) == 3

n = 128

print(Solution().hammingWeight(n))
assert Solution().hammingWeight(n) == 1
