# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper,
# return the researcher's h-index.
#
# According to the definition of h-index on Wikipedia:
# The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        pass


citations = [3, 0, 6, 1, 5]

print(Solution().hIndex(citations))
assert Solution().hIndex(citations) == [24, 12, 8, 6]


citations = [1, 3, 1]


print(Solution().hIndex(citations))
assert Solution().hIndex(citations) == [0, 0, 9, 0, 0]
