class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        smallest = min(strs,key=len)
        for i in range(len(smallest)):
            for word in strs:
                if word[i] != smallest[i]:
                    return result
            result += smallest[i]
        return result

        