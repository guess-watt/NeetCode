class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        final = 0
        result = nums[0]
        if len(nums) == 1:
            return nums[0]

        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                result = nums[i]+result
                final = max(result,final)
            else:
                result = nums[i]
        return max(final,result,nums[0])

            