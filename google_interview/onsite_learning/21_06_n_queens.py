# Given an integer n, return all distinct ways to place n queens on an n x n chessboard
# so that no two queens attack each other.

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        pass


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
