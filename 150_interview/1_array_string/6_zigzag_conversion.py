# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string s, int numRows);


class Solution:
    def convert_long_solution(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        map_string = [["" for _ in range(len(s))] for _ in range(numRows)]

        direction = 1
        rows = 0
        cols = 0
        for char in s:
            map_string[rows][cols] = char

            if direction == 1:
                if rows == numRows - 1:
                    direction = -1
                    rows -= 1
                    cols += 1
                else:
                    rows += 1
            else:
                if rows == 0:
                    direction = 1
                    rows += 1
                else:
                    rows -= 1
                    cols += 1

        ret = ""
        for i in range(len(map_string)):
            for j in range(len(map_string[0])):
                if map_string[i][j] != "":
                    ret = ret + map_string[i][j]
        return ret

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [""] * numRows
        direction = 1
        row = 0

        for char in s:
            rows[row] += char
            if direction == 1:
                if row == numRows - 1:
                    direction = -1
                    row -= 1
                else:
                    row += 1
            else:
                if row == 0:
                    direction = 1
                    row += 1
                else:
                    row -= 1
        return "".join(rows)


# s = "PAYPALISHIRING"
# numRows = 3
# print(Solution().convert(s, numRows))
# assert Solution().convert(s, numRows) == "PAHNAPLSIIGYIR"

s = "PAYPALISHIRING"
numRows = 4
print(Solution().convert(s, numRows))
assert Solution().convert(s, numRows) == "PINALSIGYAHRPI"

s = "A"
numRows = 1
print(Solution().convert(s, numRows))
assert Solution().convert(s, numRows) == "A"
