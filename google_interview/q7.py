# Given an integer array nums and an integer k, return an array of the maximum values of each sliding window of size k.
#
# A sliding window moves from left to right by one position at a time.
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums:
            return []

        que = deque()
        ret = []
        for i in range(len(nums)):
            while que and que[0] <= i - k:
                que.popleft()

            while que and nums[que[-1]] < nums[i]:
                que.pop()

            que.append(i)

            if i >= k - 1:
                ret.append(nums[que[0]])

        return ret

    def maxSlidingWindow2(self, nums, k):
        if not nums:
            return []

        left, right = 0, k
        ret = []
        while right < len(nums) + 1:
            ret.append(max(nums[left:right]))
            left += 1
            right += 1
        return ret


s = Solution()

# Example 1
assert s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]

# Example 2
assert s.maxSlidingWindow([1], 1) == [1]

# Edge case: wszystkie takie same
assert s.maxSlidingWindow([2, 2, 2, 2], 2) == [2, 2, 2]

# Edge case: k = 1
assert s.maxSlidingWindow([4, 2, 12, 3], 1) == [4, 2, 12, 3]

# Edge case: k = len(nums)
assert s.maxSlidingWindow([9, 11], 2) == [11]

# malejąca tablica
assert s.maxSlidingWindow([5, 4, 3, 2, 1], 2) == [5, 4, 3, 2]

# rosnąca tablica
assert s.maxSlidingWindow([1, 2, 3, 4, 5], 2) == [2, 3, 4, 5]
