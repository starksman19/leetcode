# Design a data structure that supports adding numbers from a stream and returning the median.


class MedianFinder:
    def __init__(self):
        pass

    def addNum(self, num: int) -> None:
        pass

    def findMedian(self) -> float:
        pass


median_finder = MedianFinder()
median_finder.addNum(1)
median_finder.addNum(2)

print(median_finder.findMedian())
assert median_finder.findMedian() == 1.5

median_finder.addNum(3)

print(median_finder.findMedian())
assert median_finder.findMedian() == 2.0
