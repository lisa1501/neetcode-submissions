class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False

        charToWord = {}

        for i in range(len(pattern)):
            ch = pattern[i]
            word = words[i]

            if ch not in charToWord:
                for k in charToWord:
                    if words[charToWord[k]] == word:
                        return False
                charToWord[ch] = i
            else:
                if words[charToWord[ch]] != word:
                    return False

        return True