# LeetCode: https://leetcode.com/problems/implement-trie-prefix-tree/
# Implement the Trie class:
#
# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch in node.children:
                node = node.children[ch]
            else:
                new_node = TrieNode()
                node.children[ch] = new_node
                node = new_node
        node.end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch in node.children:
                node = node.children[ch]
            else:
                return False

        return node.end_of_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch in node.children:
                node = node.children[ch]
            else:
                return False
        return True


trie = Trie()
trie.insert("apple")

print(trie.search("apple"))
assert trie.search("apple") == True

print(trie.search("app"))
assert trie.search("app") == False

print(trie.startsWith("app"))
assert trie.startsWith("app") == True

trie.insert("app")

print(trie.search("app"))
assert trie.search("app") == True
