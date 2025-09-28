from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        offset = 0

        while nums:
            mid = len(nums) // 2
            if nums[mid] == target:
                return mid + offset
            elif nums[mid] > target:
                nums = nums[:mid]
            else:
                nums = nums[mid + 1 :]
                offset += mid + 1
        return offset

    def searchInsert2(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (right + left) // 2 + left
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left


nums = [1, 3, 5, 6, 9, 12, 14, 16, 17]
target = 7

print(Solution().searchInsert2(nums, target))
assert Solution().searchInsert2(nums, target) == 4
