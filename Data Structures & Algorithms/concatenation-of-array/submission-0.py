class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        # length = len(nums)
        # ans = [0]*length*2
        # for i in range(len(ans)):

        dummy = nums.copy()
        nums.extend(i for i in dummy) 
        return nums
            


        