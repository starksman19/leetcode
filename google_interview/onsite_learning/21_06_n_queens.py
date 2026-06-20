# LeetCode: https://leetcode.com/problems/n-queens/
# Given an integer n, return all distinct ways to place n queens on an n x n chessboard
# so that no two queens attack each other.

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ret = []
        used_cols = set()
        used_diag_positive = set()  # r+c
        used_diag_negative = set()  # r-c
        board = [["."] * n for i in range(n)]

        def backtrack(row: int):
            if row == n:
                ret.append(["".join(row) for row in board])
                return
            for col in range(n):
                if (
                    col in used_cols
                    or (row + col) in used_diag_positive
                    or (row - col) in used_diag_negative
                ):
                    continue

                board[row][col] = "Q"
                used_cols.add(col)
                used_diag_negative.add(row - col)
                used_diag_positive.add(row + col)

                backtrack(row + 1)

                board[row][col] = "."
                used_cols.remove(col)
                used_diag_negative.remove(row - col)
                used_diag_positive.remove(row + col)

        backtrack(0)
        return ret


def normalize(boards: List[List[str]]) -> List[List[str]]:
    return sorted(boards)


n = 4

print(Solution().solveNQueens(n))
assert normalize(Solution().solveNQueens(n)) == normalize(
    [
        [".Q..", "...Q", "Q...", "..Q."],
        ["..Q.", "Q...", "...Q", ".Q.."],
    ]
)

n = 1

print(Solution().solveNQueens(n))
assert Solution().solveNQueens(n) == [["Q"]]


# 00 01 02
# 10 11 12
# 20 21 22
# 2
