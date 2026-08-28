class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        dummy = s.split()      #splits default based on space
        return len(dummy[-1])
        
        
        