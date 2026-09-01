class Solution:
        def isAnagram(self, s: str, t: str) -> bool:
                if sorted(s) == sorted(t):#sort the string
                        return True
                else:
                        return False