class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        dummy = sorted(nums,reverse=True)
        first = dummy[0]*dummy[1]
        last = dummy[-1]*dummy[-2]

        result = first - last
        return result
        
        