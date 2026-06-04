# Given a string containing only parentheses characters '(', ')', '{', '}', '[' and ']',
# return true when every opening bracket is closed by the same type of bracket in the correct order.


class Solution:
    def isValid(self, s: str) -> bool:
        pass


s = "()"

print(Solution().isValid(s))
assert Solution().isValid(s) == True

s = "()[]{}"

print(Solution().isValid(s))
assert Solution().isValid(s) == True

s = "(]"

print(Solution().isValid(s))
assert Solution().isValid(s) == False
