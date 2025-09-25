# Given a string s and a dictionary of strings wordDict,
# return true if s can be segmented into a space-separated sequence of one or more dictionary words.
#
# Note that the same word in the dictionary may be reused multiple times in the segmentation.

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        pass


s1 = "leetcode"
wordDict1 = ["leet", "code"]

s2 = "catsandog"
wordDict2 = ["cats", "dog", "sand", "and", "cat"]

print(Solution().wordBreak(s1, wordDict1))
assert Solution().wordBreak(s1, wordDict1) == True

print(Solution().wordBreak(s2, wordDict2))
assert Solution().wordBreak(s2, wordDict2) == False
