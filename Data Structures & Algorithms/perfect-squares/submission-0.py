class Solution:
    def numSquares(self, n: int) -> int:
        i = 1
        perfect = []
        while i*i <= n:
            perfect.append(i*i)
            i += 1

        dp = [float('inf')]*(n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2,n+1):
            dummy = float('inf')
            for j in perfect:
                if j > i:
                    break
                dummy = min(dp[i-j]+1,dummy)
            dp[i] = dummy
        
        return dp[n]
        