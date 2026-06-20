# LeetCode: https://leetcode.com/problems/word-search-ii/
# Given an m x n board of characters and a list of strings words, return all words on the board.
#
# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.
# The same letter cell may not be used more than once in a word.

from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for s in word:
            if s not in node.children:
                node.children[s] = TrieNode()
            node = node.children[s]
        node.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board:
            return []
        rows = len(board)
        cols = len(board[0])
        ret = []
        trie = Trie()
        for word in words:
            trie.insert(word)

        def dfs(i: int, j: int, trie_node: TrieNode):
            if i >= rows or i < 0:
                return
            if j >= cols or j < 0:
                return

            char = board[i][j]
            if char == "." or char not in trie_node.children:
                return

            next_node = trie_node.children[char]
            if next_node.word:
                ret.append(next_node.word)
                next_node.word = None

            board[i][j] = "."
            dfs(i + 1, j, next_node)
            dfs(i - 1, j, next_node)
            dfs(i, j + 1, next_node)
            dfs(i, j - 1, next_node)
            board[i][j] = char

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie.root)
        return ret


board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
words = ["oath", "pea", "eat", "rain"]

print(Solution().findWords(board, words))
assert sorted(Solution().findWords(board, words)) == ["eat", "oath"]

board = [["a", "b"], ["c", "d"]]
words = ["abcb"]

print(Solution().findWords(board, words))
assert sorted(Solution().findWords(board, words)) == []
