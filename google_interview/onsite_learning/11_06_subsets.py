# LeetCode: https://leetcode.com/problems/subsets/
# Given an integer array nums of unique elements, return all possible subsets (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in any order.

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []

        def backtrack(curr_set: List, cur_index: int):
            ret.append(curr_set[:])

            for i in range(cur_index, len(nums)):
                curr_set.append(nums[i])
                backtrack(curr_set, i + 1)
                curr_set.pop()

        backtrack([], 0)
        return ret


def normalize(subsets: List[List[int]]) -> List[List[int]]:
    return sorted([sorted(subset) for subset in subsets])


nums = [1, 2, 3]

print(Solution().subsets(nums))
assert normalize(Solution().subsets(nums)) == [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

nums = [0]

print(Solution().subsets(nums))
assert normalize(Solution().subsets(nums)) == [[], [0]]
