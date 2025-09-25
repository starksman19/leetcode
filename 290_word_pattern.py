# Given a pattern and a string s, find if s follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:
#
# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_map = {}
        word_list = s.split(" ")
        if len(pattern) != len(word_list):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in pattern_map:
                if word_list[i] not in pattern_map.values():
                    pattern_map[pattern[i]] = word_list[i]
                else:
                    return False
            else:
                if not pattern_map[pattern[i]] == word_list[i]:
                    return False
        return True


pattern1 = "abba"
t1 = "dog cat cat dog"

pattern2 = "abba"
t2 = "dog cat cat fish"

print(Solution().wordPattern(pattern1, t1))
assert Solution().wordPattern(pattern1, t1) == True

print(Solution().wordPattern(pattern2, t2))
assert Solution().wordPattern(pattern2, t2) == False
