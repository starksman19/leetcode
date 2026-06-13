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
        node = self.root
        for ch in word:
            if ch in node.children:
                node = node.children[ch]
            else:
                new_node = TrieNode()
                node.children[ch] = new_node
                node = new_node
        node.end_of_word = True

    def dfs(self, node: TrieNode, word: str) -> bool:
        if not word:
            return node.end_of_word

        ch = word[0]

        if ch == ".":
            for child in node.children.values():
                if self.dfs(child, word[1:]):
                    return True
            return False
        elif ch not in node.children:
            return False

        return self.dfs(node.children[ch], word[1:])

    def search(self, word: str) -> bool:
        node = self.root
        for i in range(len(word)):
            if word[i] == ".":
                return self.dfs(node, word[i:])
            elif word[i] in node.children:
                node = node.children[word[i]]
            else:
                return False
        return node.end_of_word


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
