class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        if x == 2:
            return 1
        start = 0
        end = x//2
        for i in range(start,end+1):
            if i*i == x:
                return i
            elif i*i > x:
                return i-1

        return end