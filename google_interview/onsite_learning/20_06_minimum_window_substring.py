# LeetCode: https://leetcode.com/problems/minimum-window-substring/
# Given two strings s and t of lengths m and n respectively,
# return the minimum window substring of s such that every character in t (including duplicates) is included in the window.
# If there is no such substring, return the empty string "".
# The testcases will be generated such that the answer is unique.
from collections import defaultdict, Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        required_dict = defaultdict(int)
        current_dict = defaultdict(tuple)

        for letter in t:
            required_dict[letter] += 1
            current_dict[letter] = (0, False)
        required = len(required_dict)
        satisfied = 0
        ret = ""

        left, right = 0, 0
        while right < len(s) or satisfied == required:
            if satisfied != required:
                if right >= len(s):
                    return ret
                right_letter = s[right]
                if right_letter not in required_dict:
                    right += 1
                    continue

                number, is_satisfied = current_dict[right_letter]
                if is_satisfied:
                    current_dict[right_letter] = (number + 1, is_satisfied)
                else:
                    if number + 1 >= required_dict[right_letter]:
                        current_dict[right_letter] = (number + 1, True)
                        satisfied += 1
                    else:
                        current_dict[right_letter] = (number + 1, False)
                right += 1
            else:
                if ret == "":
                    ret = s[left:right]
                else:
                    ret = s[left:right] if len(s[left:right]) < len(ret) else ret

                left_letter = s[left]
                if left_letter not in required_dict:
                    left += 1
                    continue

                number, is_satisfied = current_dict[left_letter]

                if number - 1 >= required_dict[left_letter]:
                    current_dict[left_letter] = (number - 1, True)
                else:
                    current_dict[left_letter] = (number - 1, False)
                    satisfied -= 1

                left += 1

        return ret

    def minWindow_gpt(self, s: str, t: str) -> str:
        need = Counter(t)
        window = defaultdict(int)

        have = 0
        required = len(need)

        left = 0
        best = ""

        for right, char in enumerate(s):
            window[char] += 1

            if char in need and window[char] == need[char]:
                have += 1

            while have == required:
                current = s[left : right + 1]

                if best == "" or len(current) < len(best):
                    best = current

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1

        return best


s = "ADOBECODEBANC"
t = "ABC"

print(Solution().minWindow(s, t))
assert Solution().minWindow(s, t) == "BANC"

s = "a"
t = "aa"

print(Solution().minWindow(s, t))
assert Solution().minWindow(s, t) == ""
