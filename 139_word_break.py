# Given a string s and a dictionary of strings wordDict,
# return true if s can be segmented into a space-separated sequence of one or more dictionary words.
#
# Note that the same word in the dictionary may be reused multiple times in the segmentation.

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        dp = (
            [False] * (len(s) + 1)
        )  # is word of len i in dict. In loop check if shorter setups are avaliable, all lenghts previously
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[-1]


s1 = "leetcode"
wordDict1 = ["leet", "code"]

s2 = "catsandog"
wordDict2 = ["cats", "dog", "sand", "and", "cat"]

print(Solution().wordBreak(s1, wordDict1))
assert Solution().wordBreak(s1, wordDict1) == True

print(Solution().wordBreak(s2, wordDict2))
assert Solution().wordBreak(s2, wordDict2) == False
