class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        results = []
        for i in range(len(s)-1,-1,-1):
            results.append(s[i])
        s[:] = results

        # s.reverse() is enough since there is inbuild function


        

        