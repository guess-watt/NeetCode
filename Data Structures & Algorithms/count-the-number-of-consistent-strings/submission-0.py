class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        result = 0
        for i in range(len(words)):
            words[i] = set(words[i])
        
        for i in words:
            for j in i:
                if j not in allowed:
                    break
            else:
                result += 1
        return result
        
        


                 