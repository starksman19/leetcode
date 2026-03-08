# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper,
# return the researcher's h-index.
#
# According to the definition of h-index on Wikipedia:
# The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        stacks = [0] * (n + 1)

        for cit in citations:
            if cit < n:
                stacks[cit] += 1
            else:
                stacks[n] += 1
        sum_up_to_this_point = 0
        for i in range(n, -1, -1):
            sum_up_to_this_point += stacks[i]
            if sum_up_to_this_point >= i:
                return i
        return 0

    def hIndex_auto_sort(self, citations: List[int]) -> int:
        h_index = 0
        citations.sort(reverse=True)
        for i in range(len(citations)):
            if citations[i] >= i + 1:
                h_index = i + 1
            else:
                break
        return h_index


citations = [3, 0, 6, 1, 5]
print(Solution().hIndex(citations))
assert Solution().hIndex(citations) == 3


citations = [1, 3, 1]
print(Solution().hIndex(citations))
assert Solution().hIndex(citations) == 1
