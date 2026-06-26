class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        
        for i in words:
            dummy = list(chars)
            for j in range(len(i)):
                if i[j] not in dummy:
                    break
                else:
                    dummy.remove(i[j])
            else:
                count = count + len(i)
        return count
        

            
            

            
            
        