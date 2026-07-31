class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        dummy = Counter(s)
        result = "0" * len(s)

        for key, value in dummy.items():
            # If there is only one '1', place it at the end to make the number odd
            if key == "1" and value == 1:
                result = result[:-1] + "1"
                return result

            # If there are multiple '1's, keep one at the end and put the rest at the front
            # Remaining positions are filled with zeros
            if key == "1" and value > 1:
                return "1" * (value - 1) + "0" * (len(s) - value) + "1"
            
        
        