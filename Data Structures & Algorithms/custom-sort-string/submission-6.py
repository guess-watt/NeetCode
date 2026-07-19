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
        """

        class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Frequency of each character in s
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        result = []

        # Add characters according to the custom order
        for ch in order:
            index = ord(ch) - ord('a')
            result.append(ch * freq[index])
            freq[index] = 0

        # Add remaining characters
        for i in range(26):
            if freq[i] > 0:
                result.append(chr(i + ord('a')) * freq[i])

        return "".join(result)


        efficient approach
        

        """
