class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        for i,j in zip(word1,word2):
            result+=(i+j)
        if len(word1) == len(word2):
            return result
        elif len(word1)>len(word2):
            dummy = word1[len(word2)::]
            result += dummy
            return result
        else:
            dummy = word2[len(word1)::]
            result += dummy
            return result

        