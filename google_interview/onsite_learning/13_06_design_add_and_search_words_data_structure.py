# Design a word dictionary that supports adding words and searching words.
# The search pattern may contain '.', which matches any single letter.


class WordDictionary:
    def __init__(self):
        pass

    def addWord(self, word: str) -> None:
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
