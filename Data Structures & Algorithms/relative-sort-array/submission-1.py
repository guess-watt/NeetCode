class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        count = 0
        for i in arr2:
            for j in arr1:
                if i==j:
                    count += 1
            result.extend([i]*count)
            count = 0
        dummy = []
        for i in arr1:
            if i not in result:
                dummy.append(i)
        dummy.sort()
        result.extend(dummy)
        return result
        

        """
        freq = {}

        # Count frequencies
        for num in arr1:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        result = []

        # Add elements according to arr2
        for num in arr2:
            result.extend([num] * freq[num])
            del freq[num]

        # Add remaining elements in sorted order
        for num in sorted(freq):
            result.extend([num] * freq[num])

        return result


        much more efficient
        """
                
                
        