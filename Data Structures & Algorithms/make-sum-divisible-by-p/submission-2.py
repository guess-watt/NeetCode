class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:

        total = sum(nums)
        target = total % p

        if target == 0:
            return 0

        min_len = len(nums)
        prefix = 0

        # remainder -> index
        seen = {0: -1}

        for i, num in enumerate(nums):
            prefix = (prefix + num) % p

            needed = (prefix - target) % p

            if needed in seen:
                min_len = min(min_len, i - seen[needed])

            seen[prefix] = i

        if min_len == len(nums):
            return -1

        return min_len


        #  BRUTE FORCE BUT NOT CORRECT

        # min_len = float('inf')
        # total = sum(nums)
        # if total % p == 0:
        #     return 0
        
        # for i in range(len(nums)):
        #     count = 1
        #     sub_sum = nums[i]
        #     if (total-sub_sum)%p == 0:
        #         min_len = min(min_len,count)
        #     for j in range(i+1,len(nums)):
        #         sub_sum += nums[j]
        #         count += 1
        #         if (total-sub_sum) % p == 0:
        #             min_len = min(min_len,count)
        # if min_len == float('inf'):
        #     return -1
        # return min_len


                

            