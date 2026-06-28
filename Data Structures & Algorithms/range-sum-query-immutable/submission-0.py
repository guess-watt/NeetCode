class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def sumRange(self, left: int, right: int) -> int:
        self.left,self.right = left,right

        result = 0
        for i in range(self.left,self.right):
            result += self.nums[i]
        result += self.nums[self.right]
        return result


        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)