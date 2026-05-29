class Solution:
    def findLucky(self, arr: List[int]) -> int:
        result = {}
        count = -1
        for i in arr:
            if i not in result:
                result[i] = 1
            else:
                result[i] = result[i]+1
        
        for key,value in result.items():
            if key == value:
                count = max(count,key)
        
        return count
            
        