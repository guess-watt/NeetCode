class Solution:
    def arrangeCoins(self, n: int) -> int:
        limit = n
        count = 0
        if n == 1:
            return 1
        for i in range(1,n):
            if i <= limit:
                limit -= i
                count += 1
            else:
                break
        return count


        