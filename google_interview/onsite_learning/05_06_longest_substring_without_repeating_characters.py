# Given a string s, return the length of the longest substring that contains no repeated characters.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pass


s = "abcabcbb"

print(Solution().lengthOfLongestSubstring(s))
assert Solution().lengthOfLongestSubstring(s) == 3

s = "bbbbb"

print(Solution().lengthOfLongestSubstring(s))
assert Solution().lengthOfLongestSubstring(s) == 1

s = "pwwkew"

print(Solution().lengthOfLongestSubstring(s))
assert Solution().lengthOfLongestSubstring(s) == 3
