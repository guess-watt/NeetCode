class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return [i,j]
        #         else:
        #             continue




        #two pointer approach
        
        seen = {}  # val : original_index
        
        for i, num in enumerate(nums):
            remaining = target - num
            
            # If the complement is already in the map, we found our pair
            if remaining in seen:
                # Return with the smaller index first
                return [seen[remaining], i]
                
            # Otherwise, store the current number and its index
            seen[num] = i


        