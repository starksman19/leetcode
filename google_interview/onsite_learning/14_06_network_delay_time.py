# LeetCode: https://leetcode.com/problems/network-delay-time/
# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi),
# where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.
#
# We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal.
# If it is impossible for all the n nodes to receive the signal, return -1.
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime_mine(self, times: List[List[int]], n: int, k: int) -> int:
        routes_map = {}
        times_map = {}
        for source, target, cost in times:
            if source in routes_map:
                routes_map[source].append((target, cost))
            else:
                routes_map[source] = [(target, cost)]
            times_map[source] = float("inf")
            if target not in times_map:
                times_map[target] = float("inf")

        if len(times_map) != n:
            return -1

        que = [k]
        times_map[k] = 0
        while que:
            source = que.pop()
            if source not in routes_map:
                continue
            routes = routes_map[source]
            for target, cost in routes:
                new_time = cost + times_map[source]

                if new_time < times_map[target]:
                    times_map[target] = new_time
                    que.append(target)
        return max(times_map.values()) if float("inf") not in times_map.values() else -1

    # min heap dijkstra
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for source, target, cost in times:
            graph[source].append((target, cost))

        dist = {i: float("inf") for i in range(1, n + 1)}
        dist[k] = 0

        heap = [(0, k)]

        while heap:
            time, node = heapq.heappop(heap)

            if time > dist[node]:
                continue

            for target, cost in graph[node]:
                new_time = time + cost

                if new_time < dist[target]:
                    dist[target] = new_time
                    heapq.heappush(heap, (new_time, target))

        answer = max(dist.values())
        return answer if answer != float("inf") else -1


times = [[1, 2, 1], [2, 1, 3]]
n = 2
k = 2

print(Solution().networkDelayTime(times, n, k))
assert Solution().networkDelayTime(times, n, k) == 3


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
