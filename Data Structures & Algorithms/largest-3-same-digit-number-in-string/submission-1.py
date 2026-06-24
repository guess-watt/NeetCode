class Solution:
    def largestGoodInteger(self, num: str) -> str:
        final = ""
        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                result = num[i] + num[i+1] + num[i+2]
                final = max(final,result)
        return final

        