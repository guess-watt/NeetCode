class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        words = sorted(words, key=len)
        result = []
        for i in words[0]:
            for j in range(1,len(words)):
                if i not in words[j]:
                    break
                else:
                    words[j]=words[j].replace(i,"",1)
            else:
                result.append(i)
            
        return result
            


        