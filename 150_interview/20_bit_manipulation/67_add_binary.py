class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_pointer = len(a) - 1
        b_pointer = len(b) - 1
        carry = 0
        out = []

        while a_pointer >= 0 or b_pointer >= 0:
            a_val = int(a[a_pointer]) if a_pointer >= 0 else 0
            b_val = int(b[b_pointer]) if b_pointer >= 0 else 0
            a_pointer -= 1
            b_pointer -= 1

            suma = carry + a_val + b_val
            out.append(str(suma % 2))
            carry = suma // 2
        if carry:
            out.append(str(carry))
        out.reverse()
        return "".join(out)


a = "1010"
b = "1011"
out_test = "10101"
print(Solution().addBinary(a, b))
assert Solution().addBinary(a, out_test)
