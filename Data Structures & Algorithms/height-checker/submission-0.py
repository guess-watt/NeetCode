class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        dummy = heights.copy()
        dummy.sort()
        count = 0
        for i in range(len(heights)):
            for j in range(i,len(dummy)):
                if heights[i] != dummy[j]:
                    count += 1
                break
        return count
        