# LeetCode: https://leetcode.com/problems/valid-parentheses/
# Given a string containing only parentheses characters '(', ')', '{', '}', '[' and ']',
# return true when every opening bracket is closed by the same type of bracket in the correct order.


class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        para_map = {"{": "}", "(": ")", "[": "]"}
        stack = []
        for item in s:
            if item in para_map:
                stack.append(item)
            elif not stack or item != para_map[stack.pop()]:
                return False
        return True if not stack else False


s = "()"

print(Solution().isValid(s))
assert Solution().isValid(s) == True

s = "()[]{}"

print(Solution().isValid(s))
assert Solution().isValid(s) == True

s = "(]"

print(Solution().isValid(s))
assert Solution().isValid(s) == False
