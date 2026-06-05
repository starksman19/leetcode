# LeetCode: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Given a string s, return the length of the longest substring that contains no repeated characters.
from collections import deque


class Solution:
    def lengthOfLongestSubstring_worse(self, s: str) -> int:
        string = deque()
        ret = 0
        for letter in s:
            if letter in string:
                while letter in string:
                    string.popleft()
            string.append(letter)
            ret = max(ret, len(string))

        return ret

    def lengthOfLongestSubstring(self, s: str) -> int:
        start, stop, ret = 0, 0, 0
        letters = set()
        while stop < len(s):
            if s[stop] in letters:
                letters.remove(s[start])
                start += 1
            else:
                letters.add(s[stop])
                stop += 1
                ret = max(ret, stop - start)
        return ret


s = "aab"

print(Solution().lengthOfLongestSubstring(s))
assert Solution().lengthOfLongestSubstring(s) == 2

s = "abcabcbb"

print(Solution().lengthOfLongestSubstring(s))
assert Solution().lengthOfLongestSubstring(s) == 3

s = "bbbbb"

print(Solution().lengthOfLongestSubstring(s))
assert Solution().lengthOfLongestSubstring(s) == 1

s = "pwwkew"

print(Solution().lengthOfLongestSubstring(s))
assert Solution().lengthOfLongestSubstring(s) == 3
