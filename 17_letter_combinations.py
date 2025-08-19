from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

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
        def backtrack(string, level):
            nonlocal digits
            if level == len(digits):
                out.append(string)
            else:
                for letter in num_map[digits[level]]:
                    backtrack(string+letter, level+1)

        start = ""
        backtrack(start, 0)
        return out

    def letterCombinationsIteratirve(self, digits: str) -> List[str]:
        if not digits:
            return []

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
        out = [""]
        for digit in digits:
            new_out = []
            for temp_out in out:
                for letter in num_map[digit]:
                    new_out.append(temp_out+letter)
            out = new_out
        return out


digits1 = "23"
out1 = ["ad","ae","af","bd","be","bf","cd","ce","cf"]

print(Solution().letterCombinations(digits1))
assert(Solution().letterCombinations(digits1) == out1)

digits1 = "23"
out1 = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
