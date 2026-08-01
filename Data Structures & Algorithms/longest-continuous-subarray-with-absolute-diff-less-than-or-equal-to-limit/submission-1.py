class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        op = 0
        
        for i in range(len(nums)):
            result = []
            result.append(nums[i])
            for j in range(i,len(nums)):
                if i != j:
                    result.append(nums[j])
              
                    
                a = max(result)
                b = min(result)

                ans = abs(a-b)
                if ans <= limit:
                    op = max(op,len(result))
                else:
                    break
        return op

                    
                    


