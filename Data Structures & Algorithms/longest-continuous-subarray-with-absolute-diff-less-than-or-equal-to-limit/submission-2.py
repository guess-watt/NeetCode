class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        op = 0

        left = 0
        maximum = deque()
        minimum = deque()

        for right in range(len(nums)):

            # maintain maximum
            while maximum and nums[maximum[-1]] < nums[right]:
                maximum.pop()
            maximum.append(right)

            # maintain minimum
            while minimum and nums[minimum[-1]] > nums[right]:
                minimum.pop()
            minimum.append(right)

            # shrink window
            while nums[maximum[0]] - nums[minimum[0]] > limit:

                if maximum[0] == left:
                    maximum.popleft()

                if minimum[0] == left:
                    minimum.popleft()

                left += 1

            op = max(op, right - left + 1)

        return op
        

        # ABSOLUTE BRUTE FORCE , NOT SOLUTION FOR LEETCODE
        # COMPLEXITY APPROX N^3

        # op = 0
        
        # for i in range(len(nums)):
        #     result = []
        #     result.append(nums[i])
        #     for j in range(i,len(nums)):
        #         if i != j:
        #             result.append(nums[j])
              
                    
        #         a = max(result)
        #         b = min(result)

        #         ans = abs(a-b)
        #         if ans <= limit:
        #             op = max(op,len(result))
        #         else:
        #             break
        # return op

                    
                    


