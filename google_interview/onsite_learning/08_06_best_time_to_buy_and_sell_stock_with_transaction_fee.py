# LeetCode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/
# You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.
#
# Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.
#
# Note:
#
# You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
# The transaction fee is only charged once for each stock purchase and sale.
from typing import List


class Solution:
    def maxProfit_bad(self, prices: List[int], fee: int) -> int:
        if len(prices) < 2:
            return 0
        dp = [0] * (len(prices))
        for i in range(1, len(prices)):
            dp[i] = dp[i - 1]

            for j in range(i):
                prev_profit = dp[j - 1] if j > 0 else 0
                dp[i] = max(dp[i], prev_profit + prices[i] - prices[j] - fee)
        return dp[-1]

    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash = 0
        hold = -prices[0]

        for i in range(1, len(prices)):
            cash = max(cash, hold - fee + prices[i])
            hold = max(hold, cash - prices[i])

        return cash


prices = [1, 7, 2, 8, 4, 9]
fee = 2

print(Solution().maxProfit(prices, fee))
assert Solution().maxProfit(prices, fee) == 11


prices = [1, 3, 2, 8, 4, 9]
fee = 2

print(Solution().maxProfit(prices, fee))
assert Solution().maxProfit(prices, fee) == 8

prices = [1, 3, 7, 5, 10, 3]
fee = 3

print(Solution().maxProfit(prices, fee))
assert Solution().maxProfit(prices, fee) == 6
