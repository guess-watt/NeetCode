from collections import Counter

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:

        if len(s) == len(set(s)):
            return -1

        result = 0
        dummy = Counter(s)
        for key,value in dummy.items():
            if value > 1:
                start = s.index(key)
                finish = s.rindex(key)
                result = max(result,(finish-start)-1)
        return result

        