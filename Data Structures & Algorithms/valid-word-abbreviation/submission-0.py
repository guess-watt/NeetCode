class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        a = 0  # index for abbr
        b = 0  # index for word
        
        while a < len(abbr) and b < len(word):
            # Case 1: If it is a number
            if abbr[a].isdigit():
                # Zero cannot be at the start of a number
                if abbr[a] == '0':
                    return False
                
                # Turn the number string into an actual integer
                num = 0
                while a < len(abbr) and abbr[a].isdigit():
                    num = num * 10 + int(abbr[a])
                    a += 1
                
                # Jump the word pointer forward
                b += num
                
            # Case 2: If it is a letter
            else:
                if abbr[a] != word[b]:
                    return False
                a += 1
                b += 1
                
        # True only if BOTH pointers reached the very end
        return a == len(abbr) and b == len(word)
