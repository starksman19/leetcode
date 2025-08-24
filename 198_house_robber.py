from typing import List


def rob(nums: List[int]) -> int:
    if not nums:
        return 0
    elif len(nums) <= 2:
        return max(nums)
    dp = [0] * len(nums)
    for index in range(0, len(nums)):
        # Might be done better cause you access index -2 and index -1 in the first two iterations
        dp[index] = max(dp[index - 2] + nums[index], dp[index - 1])
    return max(dp)


if __name__ == "__main__":
    nums1 = [1, 2, 3, 1]
    nums2 = [2, 7, 9, 3, 1]
    assert (rob(nums1)) == 4
    assert (rob(nums2)) == 12
    assert (rob([])) == 0
