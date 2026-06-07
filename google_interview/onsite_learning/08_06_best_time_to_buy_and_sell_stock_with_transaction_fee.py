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
    def maxProfit(self, prices: List[int], fee: int) -> int:
        pass


prices = [1, 3, 2, 8, 4, 9]
fee = 2

print(Solution().maxProfit(prices, fee))
assert Solution().maxProfit(prices, fee) == 8

prices = [1, 3, 7, 5, 10, 3]
fee = 3

print(Solution().maxProfit(prices, fee))
assert Solution().maxProfit(prices, fee) == 6
