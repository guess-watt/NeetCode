class Solution:
    def check(self, nums: List[int]) -> bool:
        length = len(nums)
        start = nums.index(min(nums))
        compare = 0
        for i in range(length):
            current = (start+i)%length
            if compare<= nums[current]:
                compare = nums[current]
            else:
                return False
        return True
        