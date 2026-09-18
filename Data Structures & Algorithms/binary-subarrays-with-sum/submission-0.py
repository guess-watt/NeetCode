class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count,dummy = 0,0
        

        for i in range(len(nums)):
            if nums[i] == goal:
                count += 1
            dummy = nums[i]
            for j in range(i+1,len(nums)):
                dummy = dummy + nums[j]
                if dummy == goal:
                    count += 1
                if dummy > goal:
                    break
        return count
            
        