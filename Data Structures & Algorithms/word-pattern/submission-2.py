class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        forward,backward = {},{}

        for c,w in zip(pattern,words):      #zip function is a built-in Python function that lets you iterate over multiple sequences at the same time.
            if c in forward and forward[c] != w:
                return False
            if w in backward and backward[w] != c:
                return False
            forward[c] = w
            backward[w] = c

        return True

        