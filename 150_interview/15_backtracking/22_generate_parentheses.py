# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# 1 <= n <= 8
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        pass


n1 = 3
n2 = 1


print(Solution().generateParenthesis(n1))
assert Solution().generateParenthesis(n1) == [
    "((()))",
    "(()())",
    "(())()",
    "()(())",
    "()()()",
]


print(Solution().generateParenthesis(n2))
assert Solution().generateParenthesis(n2) == ["()"]
