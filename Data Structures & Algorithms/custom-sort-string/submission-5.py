from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        result = ""
        dummy = Counter(s)

        # If no custom order is given, return the original string
        if not order:
            return s

        else:
            # Add characters according to the given order
            for i in order:
                if i in dummy:
                    result += i * dummy[i]
                    del dummy[i]

            # Add remaining characters
            for key, value in dummy.items():
                result += key * value

            return result
            