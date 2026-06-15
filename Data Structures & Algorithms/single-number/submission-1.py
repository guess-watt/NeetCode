class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # from collections import Counter
        # result = Counter(nums)
        # for key,value in result.items():
        #     if value == 1:
        #         return key        correct but more space complexity

        result = 0
        for num in nums:
            result ^= num       # xor cancel out all r twice repeating term leaving only unique

        return result 
        