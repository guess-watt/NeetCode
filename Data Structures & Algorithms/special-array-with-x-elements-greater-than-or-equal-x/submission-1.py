class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)

        # Try every possible value of x
        for x in range(n + 1):
            count = 0

            # Count elements greater than or equal to x
            for num in nums:
                if num >= x:
                    count += 1

            # Found the required x
            if count == x:
                return x

        return -1