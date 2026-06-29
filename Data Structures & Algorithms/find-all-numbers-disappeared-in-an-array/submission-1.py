class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length = len(nums)
        nums = set(nums)
        result = []
        for i in range(1,length+1):
            if i not in nums:
                result.append(i)
        return result
        
