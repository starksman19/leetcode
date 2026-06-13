# LeetCode: https://leetcode.com/problems/word-search/
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(i: int, j: int, word_left: str) -> bool:
            if not word_left:
                return True

            if i >= rows or i < 0:
                return False
            if j >= cols or j < 0:
                return False

            ch = word_left[0]

            if ch == board[i][j]:
                temp = board[i][j]
                board[i][j] = "."

                ret = any(
                    [
                        dfs(i + 1, j, word_left[1:]),
                        dfs(i - 1, j, word_left[1:]),
                        dfs(i, j + 1, word_left[1:]),
                        dfs(i, j - 1, word_left[1:]),
                    ]
                )
                board[i][j] = temp
                return ret
            else:
                return False

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, word):
                    return True
        return False


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"

print(Solution().exist(board, word))
assert Solution().exist(board, word) == True

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCB"

print(Solution().exist(board, word))
assert Solution().exist(board, word) == False
