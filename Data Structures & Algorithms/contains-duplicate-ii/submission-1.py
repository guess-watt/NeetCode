class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dummy = {}
        arr = []
        flag = 0
        for i in nums:
            if i not in dummy:
                dummy[i] = 1
            else:
                flag = 1
                target = i
        if flag == 0:
            return False


        for pos,j in enumerate(nums):   #enumerate mainly used to track the index and value in array in one loop
            if j == target:             #pos,j are not keywords
                arr.append(pos)
        
        for i in range(len(arr)-1):
            if abs(arr[i]-arr[i+1]) <= k:
                return True
        return False


