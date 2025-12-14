# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
#
# An interleaving of two strings s and t is a configuration where s and t are divided into n and m substrings respectively, such that:
#
# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
# Note: a + b is the concatenation of strings a and b.


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s1 + len_s2 != len(s3):
            return False
        dp = [[False for _ in range(len_s2 + 1)] for _ in range(len_s1 + 1)]
        dp[0][0] = True

        for i in range(1, len_s1 + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

        for j in range(1, len_s2 + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, len_s1 + 1):
            for j in range(1, len_s2 + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (
                    dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                )
        return dp[len_s1][len_s2]


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
s4 = "aabcc"
s5 = "dbbca"
s6 = "aadbbbaccc"


print(Solution().isInterleave(s1, s2, s3))
assert Solution().isInterleave(s1, s2, s3) == True
print(Solution().isInterleave(s4, s5, s6))
assert Solution().isInterleave(s4, s5, s6) == False
