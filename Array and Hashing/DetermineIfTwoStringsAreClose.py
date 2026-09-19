class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        frequency1 = {}
        frequency2 = {}
        for i in word1:
            frequency1[i] = 1 + frequency1.get(i,0)
        for i in word2:
            frequency2[i] = 1 + frequency2.get(i,0)
        if set(frequency1.keys()) != set(frequency2.keys()):
            return False
        if sorted(frequency1.values()) != sorted(frequency2.values()):
            return False
        return True