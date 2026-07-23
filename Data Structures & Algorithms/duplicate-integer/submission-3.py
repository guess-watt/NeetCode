from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # a = len(nums)
        # b = len(set(nums))

        # if a == b:
        #     return False
        # else:return True
        

        #using dict
        dummy = Counter(nums)   #counuter inbuild similar to dict{}

        for key,value in dummy.items():
            if value > 1:
                return True
        return False

        