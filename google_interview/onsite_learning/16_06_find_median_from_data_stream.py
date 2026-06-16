# LeetCode: https://leetcode.com/problems/find-median-from-data-stream/
# Design a data structure that supports adding numbers from a stream and returning the median.
import heapq


class MedianFinder:
    def __init__(self):
        self.lower_part = []
        self.higher_part = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lower_part, -num)
        heapq.heappush(self.higher_part, -heapq.heappop(self.lower_part))

        if len(self.lower_part) < len(self.higher_part):
            heapq.heappush(self.lower_part, -heapq.heappop(self.higher_part))

    def findMedian(self) -> float:
        if len(self.lower_part) > len(self.higher_part):
            return -self.lower_part[0]
        else:
            return (-self.lower_part[0] + self.higher_part[0]) / 2


median_finder = MedianFinder()
median_finder.addNum(1)
median_finder.addNum(2)

print(median_finder.findMedian())
assert median_finder.findMedian() == 1.5

median_finder.addNum(3)

print(median_finder.findMedian())
assert median_finder.findMedian() == 2.0
