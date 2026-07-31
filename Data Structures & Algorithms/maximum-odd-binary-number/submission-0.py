from collections import Counter
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        dummy = Counter(s)
        result = "0"*len(s)
    
        for key,value in dummy.items():
            if key == "1" and value == 1:
                result = result[:-1]+"1"
                return result
            if key == "1" and value > 1:
                
                return "1"*(value-1) + "0"*(len(s)-value) + "1"
            
        
        