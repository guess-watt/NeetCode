class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        result = []
        for i in range(len(s)-1,-1,-1):
            result.append(s[i])
        s[:] = result

        # s.reverse() is enough since there is inbuild function


        

        