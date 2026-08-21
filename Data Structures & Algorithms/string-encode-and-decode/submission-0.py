class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for word in strs:
            result += str(len(word)) + "#" + word

        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            # Find #
            while s[j] != "#":
                j += 1

            # Get length
            length = int(s[i:j])

            # Get the word
            word = s[j + 1 : j + 1 + length]
            result.append(word)

            # Move to next encoded word
            i = j + 1 + length

        return result