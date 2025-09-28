from typing import List

# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
# The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
#
# Increment the large integer by one and return the resulting array of digits.


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.insert(0, 0)
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
            else:
                if digits[0] == 0:
                    del digits[0]
                return digits

    def plusOneBad(self, digits: List[int]) -> List[int]:
        multiplayer = 10 ** (len(digits) - 1)
        ret = 0
        for num in digits:
            ret += num * multiplayer
            multiplayer = multiplayer / 10

        ret_st = str(int(ret + 1))
        return [int(r) for r in ret_st]


digits1 = [1, 2, 3]
digits2 = [4, 3, 2, 1]
res1 = [1, 2, 4]
res2 = [4, 3, 2, 2]

print(Solution().plusOne(digits1))
print(Solution().plusOne(digits2))
print(Solution().plusOne([9]))

assert Solution().plusOne(digits1) == res1
assert Solution().plusOne(digits2) == res2
