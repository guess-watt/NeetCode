class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        seq_length = 0
        for i in nums:
            if i-1 not in nums:
                current = i
                length = 1
                while current+1 in nums:
                    length = length + 1
                    current += 1
                seq_length = max(seq_length,length)
        return seq_length
            




