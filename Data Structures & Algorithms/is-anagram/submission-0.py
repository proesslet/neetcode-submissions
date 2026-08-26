class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sLetters = {}
        tLetters = {}

        index = 0

        while index < len(s):
            sLetters[s[index]] = 1 + sLetters.get(s[index], 0)
            tLetters[t[index]] = 1 + tLetters.get(t[index], 0)

            index += 1

        return sLetters == tLetters
            