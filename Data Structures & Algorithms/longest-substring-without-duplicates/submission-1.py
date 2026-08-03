class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()      # Characters in current window
        left = 0          # Left pointer
        result = 0

        for right in range(len(s)):  # Expand window

            while s[right] in seen:  # Remove duplicate
                seen.remove(s[left])
                left += 1

            seen.add(s[right])  # Add new character

            result = max(result, right - left + 1)  # Update max length

        return result