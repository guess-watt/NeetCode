class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = {}
        for i in nums:
            if i not in result:
                result[i] = 1
            else:
                result[i] += 1
        
        majo = len(nums)/2

        for i,j in result.items():  #here result.item is used to get both key and values.It is assigned to i(key) and j(values) respectively
            if j > majo:
                return i
        