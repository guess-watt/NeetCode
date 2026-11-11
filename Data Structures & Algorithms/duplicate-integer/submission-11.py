from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        #using dict
        dummy = Counter(nums)   #counter inbuild similar to dict{}
        for key,value in dummy.items():
            if value > 1:
                return True
        return False

        