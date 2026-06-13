# LeetCode: https://leetcode.com/problems/kth-largest-element-in-a-stream/
# Design a class that receives a stream of integers and can return the kth largest value after each insertion.
import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for item in nums:
            if len(self.heap) < self.k:
                heapq.heappush(self.heap, item)
            else:
                heapq.heappushpop(self.heap, item)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            heapq.heappushpop(self.heap, val)
        ret = heapq.heappop(self.heap)
        heapq.heappush(self.heap, ret)
        return ret


class KthLargest_gpt:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)

        return self.heap[0]


kth_largest = KthLargest(3, [4, 5, 8, 2])

result = kth_largest.add(3)
print(result)
assert result == 4

result = kth_largest.add(5)
print(result)
assert result == 5

result = kth_largest.add(10)
print(result)
assert result == 5

result = kth_largest.add(9)
print(result)
assert result == 8

result = kth_largest.add(4)
print(result)
assert result == 8
