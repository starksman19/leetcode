# LeetCode: https://leetcode.com/problems/top-k-frequent-elements/
# Given an integer array nums and an integer k, return the k most frequent elements.
# The answer may be returned in any order.

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        buckets = [[] for i in range(len(nums))]

        for val in nums:
            if val in freq:
                freq[val] += 1
            else:
                freq[val] = 1

        for item, value in freq.items():
            buckets[value - 1].append(item)

        ret = []
        for i in range(len(buckets) - 1, -1, -1):
            if len(ret) < k:
                while len(ret) < k and buckets[i]:
                    ret.append(buckets[i].pop())
        return ret


nums = [1, 1, 1, 2, 2, 3]
k = 2

print(Solution().topKFrequent(nums, k))
assert sorted(Solution().topKFrequent(nums, k)) == [1, 2]

nums = [1]
k = 1

print(Solution().topKFrequent(nums, k))
assert Solution().topKFrequent(nums, k) == [1]
