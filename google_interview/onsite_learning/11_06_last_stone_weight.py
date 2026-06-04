# LeetCode: https://leetcode.com/problems/last-stone-weight/
# Given stones with positive weights, repeatedly smash the two heaviest stones.
# If they differ, the remaining difference becomes a new stone. Return the final stone weight, or 0.

from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pass


stones = [2, 7, 4, 1, 8, 1]

print(Solution().lastStoneWeight(stones))
assert Solution().lastStoneWeight(stones) == 1

stones = [1]

print(Solution().lastStoneWeight(stones))
assert Solution().lastStoneWeight(stones) == 1
