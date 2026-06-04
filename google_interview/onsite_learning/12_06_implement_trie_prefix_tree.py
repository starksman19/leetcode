# Implement a trie with insert, search and startsWith operations for lowercase English words.


class Trie:
    def __init__(self):
        pass

    def insert(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass

    def startsWith(self, prefix: str) -> bool:
        pass


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
