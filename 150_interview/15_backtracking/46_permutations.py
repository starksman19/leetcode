from typing import List

# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        used = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                ret.append(path[:])
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    backtrack(path)
                    path.pop()
                    used[i] = False

        backtrack([])
        return ret


nums1 = [1, 2, 3]
out1 = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

print(Solution().permute(nums1))
assert Solution().permute(nums1) == out1


nums2 = [0, 1]
out2 = [[0, 1], [1, 0]]

print(Solution().permute(nums2))
assert Solution().permute(nums2) == out2
