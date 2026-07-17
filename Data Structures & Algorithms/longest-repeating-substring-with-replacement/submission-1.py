from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # Stores the frequency of characters in the current window
        count = defaultdict(int)

        left = 0
        max_freq = 0
        ans = 0

        # Expand the window
        for right in range(len(s)):

            # Include the current character
            count[s[right]] += 1

            # Update the maximum frequency in the window
            max_freq = max(max_freq, count[s[right]])

            # Shrink the window if more than k replacements are needed
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

           
            ans = max(ans, right - left + 1)

        return ans