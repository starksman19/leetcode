from typing import List

# Given a triangle array, return the minimum path sum from top to bottom.
# For each step, you may move to an adjacent number of the row below. More formally,
# if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.
# 1 <= triangle.length <= 200
# triangle[0].length == 1
# triangle[i].length == triangle[i - 1].length + 1
# -104 <= triangle[i][j] <= 104


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        mem = [[float("inf") for _ in range(len(triangle[row]))] for row in range(len(triangle))]
        mem[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    mem[i][j] = triangle[i][j] + mem[i-1][j]
                elif j == len(triangle[i]) - 1:
                    mem[i][j] = triangle[i][j] + mem[i-1][j-1]
                else:
                    mem[i][j] = min(triangle[i][j] + mem[i-1][j], triangle[i][j] + mem[i-1][j-1])
        return int(min(mem[-1]))
triangle1 = [[2],[3,4],[6,5,7],[4,1,8,3]]
triangle2 = [[-10]]


print(Solution().minimumTotal(triangle1))
assert Solution().minimumTotal(triangle1) == 11

print(Solution().minimumTotal(triangle2))
assert Solution().minimumTotal(triangle2) == -10
