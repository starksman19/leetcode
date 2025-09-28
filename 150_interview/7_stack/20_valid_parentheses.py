class Solution:
    def isValid(self, s: str) -> bool:
        opening_dict = {"}": "{", "]": "[", ")": "("}
        stack = []
        for character in s:
            if character in opening_dict.values():
                stack.append(character)
            else:
                if not stack or not opening_dict[character] == stack.pop():
                    return False
        if not stack:
            return True
        else:
            return False
