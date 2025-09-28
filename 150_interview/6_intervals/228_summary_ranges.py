from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        def to_str(a, b):
            return str(a) if a == b else f"{a}->{b}"

        if not nums:
            return []

        out = []
        start = nums[0]

        for i in range(1, len(nums) + 1):
            if i == len(nums) or nums[i] != nums[i - 1] + 1:
                out.append(to_str(start, nums[i - 1]))
                if i < len(nums):
                    start = nums[i]

        return out
