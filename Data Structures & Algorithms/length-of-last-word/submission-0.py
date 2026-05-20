class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        dummy = s.split()
        return len(dummy[-1])
        
        