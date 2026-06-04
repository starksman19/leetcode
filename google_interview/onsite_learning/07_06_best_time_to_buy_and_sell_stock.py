# Given daily stock prices, choose one day to buy and a later day to sell.
# Return the maximum possible profit, or 0 if no profitable transaction exists.

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pass


prices = [7, 1, 5, 3, 6, 4]

print(Solution().maxProfit(prices))
assert Solution().maxProfit(prices) == 5

prices = [7, 6, 4, 3, 1]

print(Solution().maxProfit(prices))
assert Solution().maxProfit(prices) == 0
