# LeetCode: https://leetcode.com/problems/word-search-ii/
# Given a board of characters and a list of words, return all words that can be formed in the board.
# Each word must use adjacent horizontal or vertical cells, and a cell may not be reused within one word.

from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        pass


board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
words = ["oath", "pea", "eat", "rain"]

print(Solution().findWords(board, words))
assert sorted(Solution().findWords(board, words)) == ["eat", "oath"]

board = [["a", "b"], ["c", "d"]]
words = ["abcb"]

print(Solution().findWords(board, words))
assert sorted(Solution().findWords(board, words)) == []
