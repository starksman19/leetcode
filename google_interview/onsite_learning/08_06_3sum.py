# LeetCode: https://leetcode.com/problems/3sum/
# Given an integer array nums, return all unique triplets [nums[i], nums[j], nums[k]]
# such that i, j and k are different indices and the three values sum to 0.
#
# The solution set must not contain duplicate triplets.

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []

        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break

            value, left, right = nums[i], i + 1, len(nums) - 1

            while left < right:
                if value + nums[left] + nums[right] == 0:
                    ret.append([value, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif value + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1

        return ret


def normalize(triplets: List[List[int]]) -> List[List[int]]:
    return sorted([sorted(triplet) for triplet in triplets])


nums = [1, 2, 0, 1, 0, 0, 0, 0]

print(Solution().threeSum(nums))
assert normalize(Solution().threeSum(nums)) == [[0, 0, 0]]


nums = [-1, 0, 1, 2, -1, -4]

print(Solution().threeSum(nums))
assert normalize(Solution().threeSum(nums)) == [[-1, -1, 2], [-1, 0, 1]]

nums = [0, 1, 1]

print(Solution().threeSum(nums))
assert normalize(Solution().threeSum(nums)) == []

nums = [0, 0, 0]

print(Solution().threeSum(nums))
assert normalize(Solution().threeSum(nums)) == [[0, 0, 0]]

nums = [0, 0, 0, 0]

print(Solution().threeSum(nums))
assert normalize(Solution().threeSum(nums)) == [[0, 0, 0]]

nums = [-2, 0, 1, 1, 2]

print(Solution().threeSum(nums))
assert normalize(Solution().threeSum(nums)) == [[-2, 0, 2], [-2, 1, 1]]
