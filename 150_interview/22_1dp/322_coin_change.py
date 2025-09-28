from typing import List

# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = [float("inf") for _ in range(amount + 1)]
        mem[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    mem[i] = min(mem[i], mem[i - coin] + 1)
        return int(mem[-1]) if mem[-1] != float("inf") else -1


assert Solution().coinChange([1, 2, 5], 11) == 3
