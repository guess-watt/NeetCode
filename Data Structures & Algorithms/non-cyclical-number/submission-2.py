class Solution:
    def isHappy(self, n: int) -> bool:
         # Returns the sum of the squares of the digits of a number
        def repeat(num):
            result = 0

            while num > 0:
                digit = num % 10          # Extract the last digit
                result += digit ** 2      # Add its square
                num //= 10                # Remove the last digit

            return result

        seen = set()  # Stores previously seen numbers to detect a cycle

        while n != 1:
            # If we've seen this number before, we're in a loop
            if n in seen:
                return False

            seen.add(n)   # Mark the current number as visited
            n = repeat(n) # Compute the next number in the sequence

        return True  # Reached 1, so it's a happy number
        