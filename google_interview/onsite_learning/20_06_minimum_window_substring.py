# LeetCode: https://leetcode.com/problems/minimum-window-substring/
# Given two strings s and t of lengths m and n respectively,
# return the minimum window substring of s such that every character in t (including duplicates) is included in the window.
# If there is no such substring, return the empty string "".
# The testcases will be generated such that the answer is unique.


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        pass


s = "ADOBECODEBANC"
t = "ABC"

print(Solution().minWindow(s, t))
assert Solution().minWindow(s, t) == "BANC"

s = "a"
t = "aa"

print(Solution().minWindow(s, t))
assert Solution().minWindow(s, t) == ""
