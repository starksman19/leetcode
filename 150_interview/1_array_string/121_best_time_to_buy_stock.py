# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


from typing import List


class Solution:
    def maxProfit_n2(self, prices: List[int]) -> int:
        if not prices:
            return 0

        biggest_diff_this_far = 0

        for i in range(len(prices)):
            for j in range(i, len(prices)):
                biggest_diff_this_far = max(biggest_diff_this_far, prices[j] - prices[i])

        return biggest_diff_this_far

    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_price = float("inf")
        ret = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            ret = max(ret, prices[i] - min_price)
        return ret


prices = [7, 1, 5, 3, 6, 4]

print(Solution().maxProfit(prices))
assert Solution().maxProfit(prices) == 5

prices = [7, 6, 4, 3, 1]
print(Solution().maxProfit(prices))
assert Solution().maxProfit(prices) == 0
