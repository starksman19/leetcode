from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        pass



nums1 = [1,2,3]
out1 = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

print(Solution().permute(nums1))
assert Solution().permute(nums1) == out1


nums2 = [0,1]
out2 = [[0,1],[1,0]]

print(Solution().permute(nums2))
assert Solution().permute(nums2) == out2
