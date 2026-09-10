class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result = 0
        left = 0
        right = len(mat[0])-1
        for i in mat:
            while left < len(i) and right >= 0:
                if left != right:
                    result = result + i[left]+i[right]
                    left += 1
                    right -= 1
                    break
                else:
                    result += i[right]
                    left += 1
                    right -= 1
                    break
        return result
            