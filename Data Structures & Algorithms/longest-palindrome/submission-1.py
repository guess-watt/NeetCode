from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> int:

        # Store the frequency of each character
        count = defaultdict(int)

        # Stores the length of the palindrome
        result = 0

        # Count characters one by one
        for c in s:
            count[c] += 1

            # Whenever the frequency becomes even,
            # we have formed one new pair.
            # Each pair contributes 2 characters.
            if count[c] % 2 == 0:
                result += 2

        # Check if there is at least one character
        # with an odd frequency.
        # Only one odd character can be placed
        # in the center of the palindrome.
        for freq in count.values():
            if freq % 2 == 1:
                result += 1
                break   # Only one center is allowed

        return result