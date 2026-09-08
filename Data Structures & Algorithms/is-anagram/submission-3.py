class Solution:
        def isAnagram(self, s: str, t: str) -> bool:
                if sorted(s) == sorted(t):#sort the string, gives return value if sorted() is used
                        return True
                else:
                        return False