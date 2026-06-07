# LeetCode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
#
# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time.
# However, you can sell and buy the stock multiple times on the same day, ensuring you never hold more than one share of the stock.
#
# Find and return the maximum profit you can achieve.


from typing import List


class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        profit = 0
        prev_price = prices[0]
        for i in range(1, len(prices)):
            if prev_price < prices[i]:
                profit += prices[i] - prev_price
                prev_price = prices[i]
            else:
                prev_price = min(prev_price, prices[i])
        return profit

    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit


prices = [7, 1, 5, 3, 6, 4]
print(Solution().maxProfit(prices))
assert Solution().maxProfit(prices) == 7

prices = [1, 2, 3, 4, 5]
print(Solution().maxProfit(prices))
assert Solution().maxProfit(prices) == 4

prices = [7, 6, 4, 3, 1]
print(Solution().maxProfit(prices))
assert Solution().maxProfit(prices) == 0
