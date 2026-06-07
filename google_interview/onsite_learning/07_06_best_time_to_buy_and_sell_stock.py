# LeetCode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Given daily stock prices, choose one day to buy and a later day to sell.
# Return the maximum possible profit, or 0 if no profitable transaction exists.

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        ret = float("-inf")
        min_from_now = prices[0]
        for i in range(1, len(prices)):
            min_from_now = min(min_from_now, prices[i])
            ret = max(ret, prices[i] - min_from_now)

        return ret


prices = [7, 1, 5, 3, 6, 4]

print(Solution().maxProfit(prices))
assert Solution().maxProfit(prices) == 5

prices = [7, 6, 4, 3, 1]

print(Solution().maxProfit(prices))
assert Solution().maxProfit(prices) == 0
