class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sLetters = {}
        tLetters = {}

        for index in range(len(s)):
            sLetters[s[index]] = 1 + sLetters.get(s[index], 0)
            tLetters[t[index]] = 1 + tLetters.get(t[index], 0)

        return sLetters == tLetters
            