class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(s)
        result = []
        reverse_result = []
        for i in range(len(s)):
            if s[i].isalnum():
                result.append(s[i].lower())
            else:continue
        for j in range(len(s)-1,-1,-1):
            if s[j].isalnum():
                reverse_result.append(s[j].lower())
            else:continue
        
        if result == reverse_result:
            return True
        else:return False
        