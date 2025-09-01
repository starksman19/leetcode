# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        s_pointer = 0
        for t_pointer in range(len(t)):
            if t[t_pointer] == s[s_pointer]:
                s_pointer += 1
            if s_pointer == len(s):
                return True
        return False


s = "abc"
t = "ahbgdc"

print(Solution().isSubsequence(s, t))
assert Solution().isSubsequence(s, t) == True
