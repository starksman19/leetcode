from typing import List


# noinspection PyInconsistentReturns
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        def partition(left, right):
            pivot, pointer = nums[right], left
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[i], nums[pointer] = nums[pointer], nums[i]
                    pointer += 1
            nums[right], nums[pointer] = nums[pointer], nums[right]
            if pointer == k:
                return nums[pointer]
            elif pointer > k:
                return partition(left, pointer - 1)
            else:
                return partition(pointer + 1, right)


        return partition(0, len(nums)-1)


nums = [3,2,1,5,6,4]
k = 2
print(Solution().findKthLargest(nums, k))
assert Solution().findKthLargest(nums, k) == 5