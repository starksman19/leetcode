# LeetCode: https://leetcode.com/problems/counting-bits/
# Given an integer n, return an array ans where ans[i] is the number of set bits in i.

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        pass


n = 2

print(Solution().countBits(n))
assert Solution().countBits(n) == [0, 1, 1]

n = 5

print(Solution().countBits(n))
assert Solution().countBits(n) == [0, 1, 1, 2, 1, 2]
