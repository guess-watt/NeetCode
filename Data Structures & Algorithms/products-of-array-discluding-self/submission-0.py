class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        result = 1
        # for i in range(len(nums)):
        #     result = result*nums[i]
        # for j in range(len(nums)):
        #     if nums[j]==0:
                
        #     real_result = result/(nums[j])
        #     output.append(int(real_result))
        #     real_result = result
        # return output
        for i in range(len(nums)):
            dummy = nums.copy()
            dummy.pop(i)
            for i in dummy:
                result = result*i
            output.append(result)
            result = 1
        return output

            