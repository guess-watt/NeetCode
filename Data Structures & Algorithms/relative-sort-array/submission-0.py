class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        count = 0
        for i in arr2:
            for j in arr1:
                if i==j:
                    count += 1
            result.extend([i]*count)
            count = 0
        dummy = []
        for i in arr1:
            if i not in result:
                dummy.append(i)
        dummy.sort()
        result.extend(dummy)
        return result
        
                
                
        