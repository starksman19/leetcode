class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        def to_dict(st: str):
            out = {}
            for letter in st:
                if letter in out:
                    out[letter] += 1
                else:
                    out[letter] = 1
            return out

        rans = to_dict(ransomNote)
        mag = to_dict(magazine)

        for key, value in rans.items():
            if key not in mag:
                return False
            if value > mag[key]:
                return False
        return True
