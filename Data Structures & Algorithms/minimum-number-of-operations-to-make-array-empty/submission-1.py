from collections import Counter
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        dummy = Counter(nums)
        count = 0
        for key,value in dummy.items():
            if value == 1:
                return -1
            while value > 0:
                if value%3 == 0:
                    value -= 3
                else:
                    value -= 2
                count += 1
        return count