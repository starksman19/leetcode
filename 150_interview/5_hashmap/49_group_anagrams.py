# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rep_dict = {}
        for item in strs:
            finished = "".join(sorted(item))
            if finished in rep_dict:
                rep_dict[finished].append(item)
            else:
                rep_dict[finished] = [item]
        ret = [val for val in rep_dict.values()]
        return ret


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(strs))
assert Solution().groupAnagrams(strs) == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]


strs = [""]
print(Solution().groupAnagrams(strs))
assert Solution().groupAnagrams(strs) == [[""]]


strs = ["a"]
print(Solution().groupAnagrams(strs))
assert Solution().groupAnagrams(strs) == [["a"]]
