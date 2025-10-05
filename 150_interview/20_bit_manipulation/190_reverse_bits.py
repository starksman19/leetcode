# Reverse bits of a given 32 bits signed integer.


class Solution:
    def reverseBits(self, n: int) -> int:
        n = n & 0xFFFFFFFF

        bits = ""
        for i in range(32):
            bits = str(n % 2) + bits
            n //= 2

        reversed_bits = bits[::-1]
        result = 0
        for bit in reversed_bits:
            result = result * 2 + int(bit)

        return result

    def reverseBits2(self, n: int) -> int:
        result = 0
        for i in range(32):
            result <<= 1  # shift left
            result |= n & 1  # add LSB of n
            n >>= 1  # shift n right
        return result


n1 = 43261596
o1 = 964176192


n2 = 2147483644
o2 = 1073741822


print(Solution().reverseBits(n1))
assert Solution().reverseBits(n1) == o1

print(Solution().reverseBits(n2))
assert Solution().reverseBits(n2) == o2
