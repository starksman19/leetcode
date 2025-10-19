# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
#
# Evaluate the expression. Return an integer that represents the value of the expression.
# Note that:
# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.
# Constraints:
#
# 1 <= tokens.length <= 104
# tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].

from typing import List


class Solution:
    def operation(self, sing: str, num1: int, num2: int):
        if sing == "+":
            return int(num1) + int(num2)
        elif sing == "-":
            return int(num1) - int(num2)
        elif sing == "*":
            return int(num1) * int(num2)
        elif sing == "/":
            return int(int(num1) / int(num2))
        else:
            raise ValueError("Not a valid sign")

    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        valid_tok = "+-*/"
        for i in range(len(tokens)):
            if tokens[i] in valid_tok:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(self.operation(tokens[i], num1, num2))
            else:
                stack.append(tokens[i])
        return stack[0]


tokens1 = ["2", "1", "+", "3", "*"]
tokens2 = ["4", "13", "5", "/", "+"]
tokens3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]

print(Solution().evalRPN(tokens1))
assert Solution().evalRPN(tokens1) == 9

print(Solution().evalRPN(tokens2))
assert Solution().evalRPN(tokens2) == 6

print(Solution().evalRPN(tokens3))
assert Solution().evalRPN(tokens3) == 22
