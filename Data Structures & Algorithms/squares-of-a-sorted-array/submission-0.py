class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        nums.sort()
        for i in nums:
            result.append(i*i)
        result = sorted(result)
        return result
        