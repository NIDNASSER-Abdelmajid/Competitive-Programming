class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        n = len(word1)
        m = len(word2)
        if n > m:
            z = m
            reste = word1[m:]
        elif m >= n:
            z = n
            reste = word2[n:]
        for i in range(z):
            merged += word1[i] + word2[i]
        return merged + reste