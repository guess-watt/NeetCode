class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        result = []
        for i in nums:
            if i != 0:
                result.append(i)
        c = nums.count(0)
        result.extend([0]*c)
        nums[:] = result