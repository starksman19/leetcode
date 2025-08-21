class Solution:
    def isPalindrome(self, x: int) -> bool:
        pass


x1 = 121
out_test = True

print(Solution().isPalindrome(x1))
assert Solution().isPalindrome(x1) == out_test

x2 = -121
out_test = False

print(Solution().isPalindrome(x2))
assert Solution().isPalindrome(x2) == out_test