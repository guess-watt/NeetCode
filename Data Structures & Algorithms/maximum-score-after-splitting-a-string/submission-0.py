class Solution:
    def maxScore(self, s: str) -> int:
        result = 0
        for i in range(1,len(s)):
            first = s[:i]
            second = s[i:]
            op = first.count('0') + second.count('1')
            result = max(result,op)
        return result
        
        
        