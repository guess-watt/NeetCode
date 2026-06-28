class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        unique = {}
        dummy = []
        for i in arr:
            if i not in unique:
                unique[i] = 1
            else:
                unique[i] += 1
        
        for key,value in unique.items():
            if value == 1:
                dummy.append(key)
        if len(dummy) >= k:
            return dummy[k-1]
        else:
            return ""
