class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
        
        c = str(x)
        if c == c[::-1]:
            return True
        else:
            return False
        