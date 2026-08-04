class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        count = 0
        left,right = 0,len(s)-1
        for i in range(len(t)):
            while left <= right:
                if s[left] == t[i]:
                    count += 1
                    left += 1
                    break
                else:
                    left += 1
        return (len(t)-count)

            

            


