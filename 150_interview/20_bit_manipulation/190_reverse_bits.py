# Reverse bits of a given 32 bits signed integer.


class Solution:
    def reverseBits(self, n: int) -> int:
        pass


n1 = 43261596
o1 = 964176192


n2 = 43261596
o2 = 964176192


print(Solution().reverseBits(n1))
assert Solution().reverseBits(n1) == o1

print(Solution().reverseBits(n2))
assert Solution().reverseBits(n2) == o2
