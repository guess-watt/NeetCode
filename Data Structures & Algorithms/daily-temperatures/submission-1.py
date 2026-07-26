class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        count = 0
        result = []
        for i in range(len(temperatures)-1):
            count = 0
            for j in range(i+1,len(temperatures)):
                count += 1
                if temperatures[i] < temperatures[j]:
                    result.append(count)
                    break
            else:
                result.append(0)
        result.append(0)
        return result

        """

        ### using monotonous stack ###

        n = len(temperatures)
        result = [0]*n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                result[prev] = i - prev

            stack.append(i)

        return result

        """


                
                    


        