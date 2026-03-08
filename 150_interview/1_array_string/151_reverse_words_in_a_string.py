# Given an input string s, reverse the order of the words.
#
# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
#
# Return a string of the words in reverse order concatenated by a single space.
#
# Note that s may contain leading or trailing spaces or multiple spaces between two words.
# The returned string should only have a single space separating the words. Do not include any extra spaces.


class Solution:
    def reverseWords(self, s: str) -> str:
        if not s.strip():
            return ""
        ret_list = []
        s.strip()
        word = ""
        for string in s:
            if string == " ":
                if word != "":
                    ret_list.append(word)
                    word = ""
                else:
                    continue
            else:
                word = word + string
        if word != "":
            ret_list.append(word)
        ret_list.reverse()
        return " ".join(ret_list)


class Solution2:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


s1 = "the sky is blue"
o1 = "blue is sky the"

s2 = "  hello world  "
o2 = "world hello"

s3 = "a good   example"
o3 = "example good a"

print(Solution().reverseWords(s1))
assert Solution().reverseWords(s1) == o1

print(Solution().reverseWords(s2))
assert Solution().reverseWords(s2) == o2

print(Solution().reverseWords(s3))
assert Solution().reverseWords(s3) == o3
