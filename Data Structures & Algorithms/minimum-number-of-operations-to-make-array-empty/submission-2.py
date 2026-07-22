from collections import Counter

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Count the frequency of each number
        dummy = Counter(nums)
        count = 0

        # Traverse each unique number and its frequency
        for key, value in dummy.items():

            # If a number appears only once, it is impossible
            if value == 1:
                return -1

            # Try removing groups of 3, otherwise remove groups of 2
            while value > 0:
                if value % 3 == 0:
                    value -= 3
                else:
                    value -= 2
                count += 1

        return count