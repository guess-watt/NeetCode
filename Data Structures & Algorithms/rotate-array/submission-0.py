class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        
        # nums[-k:] gets the last k elements
        # nums[:-k] gets everything except the last k elements
        nums[:] = nums[-k:] + nums[:-k]