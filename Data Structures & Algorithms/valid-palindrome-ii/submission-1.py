class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        flag = False
        while left<=right:
            if s[left] != s[right]:

                #delete left element
                l = left + 1
                r = right

                while l<=r:
                    if s[l] != s[r]:
                        break
                    l += 1
                    r -= 1

                if l>r:
                    return True
                
                #delete right element
                l = left
                r = right - 1

                while l<=r:
                    if s[l] != s[r]:
                        return False
                    l += 1
                    r -= 1
                
                if l > r:
                    return True
            left += 1
            right -= 1


        return True
                    
            