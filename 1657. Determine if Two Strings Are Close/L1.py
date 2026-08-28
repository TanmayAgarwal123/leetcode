class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) == len(word2):
            if set(word1) == set(word2):
                if sorted(Counter(word1).values()) == sorted(Counter(word2).values()):
                    return True
                return False
            return False
        return False