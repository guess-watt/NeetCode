class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums.sort()
        count = 0
        for i in range(len(nums)-1):
            if i%2 == 0:
                if nums[i] == nums[i+1]:
                    count = count + 1
                else:
                    return False
        return True


