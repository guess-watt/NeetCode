class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count = 0
        for i in range(len(g)):
            for j in s:
                if j >= g[i]:
                    count+=1
                    s.remove(j)
                    break
        return count