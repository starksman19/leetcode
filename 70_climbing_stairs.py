class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        dp = [0 for _ in range(n)]
        dp[-1] = 1
        dp[-2] = 2
        for i in range(n-3, -1, -1):
            dp[i] = dp[i + 1] + dp[i + 2]

        return dp[0]

    def climbStairs2(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one

print(Solution().climbStairs(10))
# assert Solution().climbStairs(2) == 2
#
# print(Solution().climbStairs(3))
# assert Solution().climbStairs(3) == 3


