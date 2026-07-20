class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i in range(len(numbers)-1):
        #     for j in range(i+1,len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i+1,j+1]
        #         if numbers[i] + numbers[j] > target:
        #             break
        #  pure brute force

        
        #using two pointer(aka without using any data type)
        left = 0
        right = len(numbers)-1
        

        while left < right:
            if numbers[left]+numbers[right] < target:
                left += 1
            elif numbers[left]+numbers[right] > target:
                right -= 1
            else:
                return [left+1,right+1]
                    
