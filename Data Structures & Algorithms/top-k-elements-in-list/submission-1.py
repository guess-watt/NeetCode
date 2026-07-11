class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dummy = {}
        for i in nums:
            if i not in dummy:
                dummy[i] = 1
            else:
                dummy[i] += 1
        
        sorted_d = sorted(dummy.items(), key=lambda x:x[1],reverse=True)
        # Convert dict to (key, value) pairs and sort them by value (frequency) in descending order

        
        result = []
        for i in range(k):
            result.append(sorted_d[i][0])
        
        return result


        