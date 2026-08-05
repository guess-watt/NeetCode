class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result = []
        length = len(matrix[0])
        
        for i in range(length):
            dummy = []
            for j in range(len(matrix)):
                dummy.append(matrix[j][i])
            result.append(dummy)
        return result

        