class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        

        result = ""
        hashdict = {}
        for i in words:
            result += i
        for i in result:
            if i not in hashdict:
                hashdict[i] = 1
            else:
                hashdict[i] += 1
        
        n = len(words)

        for count in hashdict.values():
            if count % n != 0:
                return False
        return True







        