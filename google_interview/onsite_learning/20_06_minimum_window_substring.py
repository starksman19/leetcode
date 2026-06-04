# Given strings s and t, return the smallest substring of s that contains every character from t.
# If no such substring exists, return an empty string.


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
