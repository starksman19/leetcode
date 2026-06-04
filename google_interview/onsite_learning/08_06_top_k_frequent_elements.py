# LeetCode: https://leetcode.com/problems/top-k-frequent-elements/
# Given an integer array nums and an integer k, return the k most frequent elements.
# The answer may be returned in any order.

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pass


nums = [1, 1, 1, 2, 2, 3]
k = 2

print(Solution().topKFrequent(nums, k))
assert sorted(Solution().topKFrequent(nums, k)) == [1, 2]

nums = [1]
k = 1

print(Solution().topKFrequent(nums, k))
assert Solution().topKFrequent(nums, k) == [1]
