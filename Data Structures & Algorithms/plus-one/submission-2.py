class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        dummy = ""
        for i in digits:
            dummy += str(i)
        
        number = int(dummy) + 1
        number = str(number)
        result = []
        

        #not efficient 
        for j in number:
            result.append(j)
        return result
        