class Solution:
    def maxDifference(self, s: str) -> int:
        result = {}
        for i in s:
            if i not in result:
                result[i] = 1
            else:
                result[i] += 1
        
        odd = 0
        even = float("inf")     #initialize to +ve infy , for negative use "-inf"

        for value in result.values():
            if value % 2 != 0:
                odd = max(odd,value)
            else:
                even = min(even,value)      #here float and int value get compared and even become int. so no need to typecast it into int
        
        return (odd - even)

        