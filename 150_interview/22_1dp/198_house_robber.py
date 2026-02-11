from typing import List

# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed,
# the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected
# and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house
# return the maximum amount of money you can rob tonight without alerting the police.


def rob(nums: List[int]) -> int:
    if not nums:
        return 0
    elif len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return max(nums)

    first, second = (
        max(nums[0], nums[1]),
        nums[0],
    )
    for i in range(2, len(nums)):
        temp = first
        first = max(second + nums[i], first)
        second = temp
    return first


if __name__ == "__main__":
    nums1 = [1, 2, 3, 1]
    nums2 = [2, 7, 9, 3, 1]
    assert (rob(nums1)) == 4
    assert (rob(nums2)) == 12
    assert (rob([])) == 0
    assert (rob([1])) == 1
    assert (rob([1, 2])) == 2
    assert (rob([2, 1, 1, 2])) == 4
