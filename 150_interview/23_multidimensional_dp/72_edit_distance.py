# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
#
# You have the following three operations permitted on a word:
#
# Insert a character
# Delete a character
# Replace a character

# 0 <= word1.length, word2.length <= 500
# word1 and word2 consist of lowercase English letters.


class Solution:
    def minDistance(self, word1: str, word2: str) -> int | float:
        dp = [[float("inf") for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        for i in range(len(dp)):
            dp[i][0] = i
        for j in range(len(dp[0])):
            dp[0][j] = j

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)

        return dp[-1][-1]


word1 = "horse"
word2 = "ros"

print(Solution().minDistance(word1, word2))
assert Solution().minDistance(word1, word2) == 3

word1 = "intention"
word2 = "execution"

print(Solution().minDistance(word1, word2))
assert Solution().minDistance(word1, word2) == 5
