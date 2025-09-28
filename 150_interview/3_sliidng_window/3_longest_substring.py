# Given a string s, find the length of the longest substring without duplicate characters.
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ret, l, r = 0, 0, 0

        letters = set()
        while r < len(s):
            if s[r] not in letters:
                letters.add(s[r])
                r += 1
                ret = max(ret, r - l)
            else:
                letters.remove(s[l])
                l += 1
        return ret


s1 = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"


print(Solution().lengthOfLongestSubstring(s1))
assert Solution().lengthOfLongestSubstring(s1) == 3

print(Solution().lengthOfLongestSubstring(s2))
assert Solution().lengthOfLongestSubstring(s2) == 1

print(Solution().lengthOfLongestSubstring(s3))
assert Solution().lengthOfLongestSubstring(s3) == 3
