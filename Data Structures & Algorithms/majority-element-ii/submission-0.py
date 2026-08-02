from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = []
        dummy = Counter(nums)
        limit = len(nums)/3

        for key,value in dummy.items():
            if value > limit:
                result.append(key)
        return result
        