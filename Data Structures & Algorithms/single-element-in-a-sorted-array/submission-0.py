class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        dummy = 0
        for i in nums:
            dummy ^= i
        return dummy
        