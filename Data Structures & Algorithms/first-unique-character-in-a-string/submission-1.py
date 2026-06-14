class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        result = Counter(s)

        for key,value in result.items():
            if value == 1:
                return s.index(key)
        else:
            return -1
        