# LeetCode: https://leetcode.com/problems/merge-intervals/
# Given an array of intervals, merge all overlapping intervals and return the non-overlapping result.

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        pass


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

print(Solution().merge(intervals))
assert Solution().merge(intervals) == [[1, 6], [8, 10], [15, 18]]

intervals = [[1, 4], [4, 5]]

print(Solution().merge(intervals))
assert Solution().merge(intervals) == [[1, 5]]
