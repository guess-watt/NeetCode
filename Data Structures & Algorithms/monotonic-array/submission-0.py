class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        else:
            count1,count2 = 0,0
            for i in range(len(nums)-2):
                if nums[i] <= nums[i+1] and nums[i+1] <= nums[i+2]:
                    count1 += 1
            if count1 == len(nums)-2:
                return True
            else:
                for j in range(len(nums)-2):
                    if nums[j] >= nums[j+1] and nums[j+1] >= nums[j+2]:
                        count2 += 1
            if count2 == len(nums)-2:
                return True
            else:
                return False
            
                


        