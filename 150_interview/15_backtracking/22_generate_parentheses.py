# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# 1 <= n <= 8
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        def backtrack(path: List[str], open_count: int, close_count: int):
            if len(path) == 2*n:
                ret.append("".join(path[:]))
                return
            if open_count < n:
                path.append("(")
                backtrack(path, open_count + 1, close_count)
                path.pop()
            if close_count < open_count:
                path.append(")")
                backtrack(path, open_count, close_count + 1)
                path.pop()
        backtrack([], 0, 0)
        return ret

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
