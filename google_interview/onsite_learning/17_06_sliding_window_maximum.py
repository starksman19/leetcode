# LeetCode: https://leetcode.com/problems/sliding-window-maximum/
# Given an integer array nums and a window size k, return the maximum value in each sliding window.
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k > len(nums):
            return []
        que = deque([])
        ret = []
        for i in range(len(nums)):
            if que and que[0] < i - k + 1:
                que.popleft()
            while que and nums[i] > nums[que[-1]]:
                que.pop()
            que.append(i)

            if i >= k - 1:
                ret.append(nums[que[0]])

        return ret


nums = [1, 3, 1, 2, 0, 5]
k = 3

print(Solution().maxSlidingWindow(nums, k))
assert Solution().maxSlidingWindow(nums, k) == [3, 3, 2, 5]

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

print(Solution().maxSlidingWindow(nums, k))
assert Solution().maxSlidingWindow(nums, k) == [3, 3, 5, 5, 6, 7]

nums = [1]
k = 1

print(Solution().maxSlidingWindow(nums, k))
assert Solution().maxSlidingWindow(nums, k) == [1]
