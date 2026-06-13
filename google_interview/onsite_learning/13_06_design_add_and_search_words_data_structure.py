# LeetCode: https://leetcode.com/problems/design-add-and-search-words-data-structure/
# Design a data structure that supports adding new words and finding if a string matches any previously added string.
#
# Implement the WordDictionary class:
#
# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise.
# word may contain dots '.' where dots can be matched with any letter.


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        pass

    def dfs(self, node: TrieNode, word: str) -> bool:
        pass

    def search(self, word: str) -> bool:
        pass


word_dictionary = WordDictionary()
word_dictionary.addWord("bad")
word_dictionary.addWord("dad")
word_dictionary.addWord("mad")

print(word_dictionary.search("pad"))
assert word_dictionary.search("pad") == False

print(word_dictionary.search("bad"))
assert word_dictionary.search("bad") == True

print(word_dictionary.search(".ad"))
assert word_dictionary.search(".ad") == True

print(word_dictionary.search("b.."))
assert word_dictionary.search("b..") == True
