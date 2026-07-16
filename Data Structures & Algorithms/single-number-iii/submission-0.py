from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        result = Counter(nums)
        op = []
        for key,value in result.items():
            if value == 1:
                op.append(key)
        return op
        
        