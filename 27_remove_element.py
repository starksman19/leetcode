from collections import deque
from typing import List


# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
#
# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
#
# Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
# The remaining elements of nums are not important as well as the size of nums.
# Return k.

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        avaliable_slots = deque()
        for i in range(len(nums)):
            if nums[i] == val:
                k -= 1
                avaliable_slots.append(i)
            elif avaliable_slots:
                nums[avaliable_slots.popleft()] = nums[i]
                avaliable_slots.append(i)
        return k

nums1 = [3, 2, 2, 3]
val1 = 3
nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
val2 = 2

print(Solution().removeElement(nums1, val1))
assert Solution().removeElement(nums1, val1) == 2

print(Solution().removeElement(nums2, val2))
assert Solution().removeElement(nums2, val2) == 5

