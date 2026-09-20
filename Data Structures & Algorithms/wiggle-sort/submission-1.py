class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        for i in range(1, len(nums) - 1, 2):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]

        
        
        """

        arr = sorted(nums)
        n = len(nums)

        for i in range(n):
            if i % 2 == 0:
                nums[i] = arr[i // 2]
            else:
                nums[i] = arr[n // 2 + i // 2]

        """
