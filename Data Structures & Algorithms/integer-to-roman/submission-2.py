class Solution:
    def intToRoman(self, num: int) -> str:
        ref = [["I",1],["IV",4],["V",5],["IX",9],["X",10],["XL",40],["L",50],
        ["XC",90],["C",100],["CD",400],["D",500],["CM",900],["M",1000]]
        ## we define all numbers first,special number like 3,9,40 etc are also defiended
        ## as it first come with small and then larger(IV,IX) unlike the traditional setup of small after 
        ## large(XI,LX)


        res = ""

        for alp,value in reversed(ref):
            while num//value != 0:
                count = num//value
                res += (alp * count)
                num %= value
        
        return res
