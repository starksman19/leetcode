# Given a positive integer n, write a function that returns the number of set bits in its binary representation
# (also known as the Hamming weight).


class Solution:
    def hammingWeight(self, n: int) -> int:
        ret = 0
        if n == 0:
            return 0
        while n > 0:
            if n % 2 == 1:
                ret += 1
            n //= 2
        return ret


a = 11
b = 128

print(Solution().hammingWeight(a))
assert Solution().hammingWeight(a) == 3

print(Solution().hammingWeight(b))
assert Solution().hammingWeight(b) == 1
