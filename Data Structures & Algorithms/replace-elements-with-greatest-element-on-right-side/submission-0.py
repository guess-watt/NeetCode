class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        a = 0
        result = []
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                a = max(a,arr[j])
            result.append(a) 
            a = 0
        result.append(-1)
        return result
        