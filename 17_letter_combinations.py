from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        out = []
        num_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        return out

digits1 = "23"
out1 = ["ad","ae","af","bd","be","bf","cd","ce","cf"]

print(Solution().letterCombinations(digits1))
assert(Solution().letterCombinations(digits1) == out1)

digits1 = "23"
out1 = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
