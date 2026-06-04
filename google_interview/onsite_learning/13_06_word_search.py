# LeetCode: https://leetcode.com/problems/word-search/
# Given an m x n board of characters and a word, return true if the word exists in the grid.
# The word must be formed by adjacent horizontal or vertical cells, and a cell may not be reused.

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        pass


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"

print(Solution().exist(board, word))
assert Solution().exist(board, word) == True

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCB"

print(Solution().exist(board, word))
assert Solution().exist(board, word) == False
