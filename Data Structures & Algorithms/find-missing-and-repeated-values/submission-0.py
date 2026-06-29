class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        dummy = []
        for i in grid:
            for j in i:
                dummy.append(j)
        
        for k in range(1,len(dummy)+1):
            if k not in dummy:
                missing = k

        d = {}


        for a in dummy:
            if a not in d:
                d[a] = 1
            else:
                d[a] += 1
        for key,value in d.items():
            if value > 1:
                repeat = key
        
        return [repeat,missing]