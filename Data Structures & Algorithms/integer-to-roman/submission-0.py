class Solution:
    def intToRoman(self, num: int) -> str:
        ref = [["I",1],["IV",4],["V",5],["IX",9],["X",10],["XL",40],["L",50],
        ["XC",90],["C",100],["CD",400],["D",500],["CM",900],["M",1000]]
        
        res = ""

        for alp,value in reversed(ref):
            if num//value:
                count = num//value
                res += (alp * count)
                num %= value
        
        return res
