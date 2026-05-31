class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a = len(nums)
        count = 0
        while val in nums:
            nums.remove(val)
            count += 1
        k = a - count
        return k

        