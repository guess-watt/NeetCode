class Solution:
    def countPrimes(self, n: int) -> int:

         # Sieve of Eratosthenes
        if n <= 2:
            return 0
        
        isprime = [True]*n

        isprime[0] = isprime[1] = False

        for i in range(2,int(n**0.5)+1):    #only need to loop upto the root of number
            if isprime[i] == True:  #enough to get is_prime == True
                for j in range(i*i,n,i):    #to get the mutliples of i
                    isprime[j] = False
        return sum(isprime)     #gives sum of True case
