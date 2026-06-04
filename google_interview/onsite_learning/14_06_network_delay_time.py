# LeetCode: https://leetcode.com/problems/network-delay-time/
# Given directed travel times between nodes, return how long it takes for all nodes to receive a signal from k.
# Return -1 if some node cannot be reached.

from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        pass


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2

print(Solution().networkDelayTime(times, n, k))
assert Solution().networkDelayTime(times, n, k) == 2

times = [[1, 2, 1]]
n = 2
k = 2

print(Solution().networkDelayTime(times, n, k))
assert Solution().networkDelayTime(times, n, k) == -1
