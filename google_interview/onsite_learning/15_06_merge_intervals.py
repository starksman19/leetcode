# LeetCode: https://leetcode.com/problems/merge-intervals/
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ret = []
        for start, stop in intervals:
            if not ret:
                ret.append([start, stop])
                continue

            prev = ret[-1]
            if start <= prev[1] < stop:
                prev[1] = stop
            else:
                if prev[1] < stop:
                    ret.append([start, stop])
        return ret


intervals = [[1, 4], [2, 3]]

print(Solution().merge(intervals))
assert Solution().merge(intervals) == [[1, 4]]

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

print(Solution().merge(intervals))
assert Solution().merge(intervals) == [[1, 6], [8, 10], [15, 18]]

intervals = [[1, 4], [4, 5]]

print(Solution().merge(intervals))
assert Solution().merge(intervals) == [[1, 5]]
