from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        offset = 0

        while nums:
            mid_index = len(nums) // 2

            if nums[mid_index] == target:
                return mid_index + offset

            if nums[mid_index] > target:
                nums = nums[:mid_index]
            else:
                nums = nums[1+mid_index:]
                offset +=  mid_index + 1
        return offset

    def searchInsert2(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # At this point, left is the insertion position
        return left


nums = [1, 3, 5, 6, 9, 12, 14, 16, 17]
target = 7

print(Solution().searchInsert(nums, target))
assert(Solution().searchInsert(nums, target) == 4)