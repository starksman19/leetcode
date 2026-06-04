# LeetCode: https://leetcode.com/problems/kth-largest-element-in-a-stream/
# Design a class that receives a stream of integers and can return the kth largest value after each insertion.

from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        pass

    def add(self, val: int) -> int:
        pass


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
