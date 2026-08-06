class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        for char in t:
            if i < len(s) and s[i] == char:
                i += 1
    
        return i == len(s)
        

        """

        left,right = 0,len(t)-1

        for i in s:
            while left <= right:
                if t[left] == i:
                    left += 1
                    break
                else:
                    left += 1
            else:
                return False
        return True

        """