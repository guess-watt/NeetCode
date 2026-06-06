class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        result = {}

        for i in nums:
            if i not in result:
                result[i] = 1
            else:
                result[i] += 1


        nums.sort(key=lambda x: (result[x], -x))
        return nums
        



        