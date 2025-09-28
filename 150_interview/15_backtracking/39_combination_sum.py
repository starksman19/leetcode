# Given an array of distinct integers candidates and a target integer target,
# return a list of all unique combinations of candidates where the chosen numbers sum to target.
# You may return the combinations in any order.
#
# The same number may be chosen from candidates an unlimited number of times.
# Two combinations are unique if the frequency of at least one of the chosen numbers is different.
#
# The test cases are generated such that the number of unique combinations
# that sum up to target is less than 150 combinations for the given input.
# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# All elements of candidates are distinct.
# 1 <= target <= 40
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(start, path, total):
            if total == target:
                res.append(path[:])
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i])
                path.pop()  # cofamy wybór

        backtrack(0, [], 0)
        return res


candidates1 = [2, 3, 5]
target1 = 8
candidates2 = [2]
target2 = 1

print(Solution().combinationSum(candidates1, target1))
assert Solution().combinationSum(candidates1, target1) == [
    [2, 2, 2, 2],
    [2, 3, 3],
    [3, 5],
]

print(Solution().combinationSum(candidates2, target2))
assert Solution().combinationSum(candidates2, target2) == []
