# Given two strings s and t, determine if they are isomorphic.
#
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character, but a character may map to itself.


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letter_map = {}
        for i in range(len(s)):
            if s[i] not in letter_map:
                if t[i] not in letter_map.values():
                    letter_map[s[i]] = t[i]
                else:
                    return False
            else:
                if letter_map[s[i]] != t[i]:
                    return False
        return True


s1 = "egg"
t1 = "add"

s2 = "foo"
t2 = "bar"

print(Solution().isIsomorphic(s1, t1))
assert Solution().isIsomorphic(s1, t1) == True

print(Solution().isIsomorphic(s2, t2))
assert Solution().isIsomorphic(s2, t2) == False
