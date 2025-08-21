class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        return False


x1 = 121
out_test = True

print(Solution().isPalindrome(x1))
assert Solution().isPalindrome(x1) == out_test

x2 = -121
out_test = False

print(Solution().isPalindrome(x2))
assert Solution().isPalindrome(x2) == out_test