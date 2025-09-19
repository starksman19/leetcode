from typing import List

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
# find two numbers such that they add up to a specific target number.
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
#
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
#
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
#
# Your solution must use only constant extra space.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) -1
        while right > left:
            sum = numbers[left] + numbers[right]
            if sum == target:
                break
            elif sum > target:
                right -=1
            else:
                left += 1
        return [left+1, right+1]




numbers1 = [2,7,11,15]
target1 = 9

numbers2 = [2,3,4]
target2 = 6

print(Solution().twoSum(numbers1,target1))
assert Solution().twoSum(numbers1,target1) == [1,2]

print(Solution().twoSum(numbers1,target1))
assert Solution().twoSum(numbers1,target1) == [1,3]

