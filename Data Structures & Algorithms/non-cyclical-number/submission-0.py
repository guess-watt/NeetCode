class Solution:
    def isHappy(self, n: int) -> bool:
        def repeat(num):
            result = 0
            while num > 0:
                digit = num % 10
                result += digit ** 2
                num //= 10
            return result

        seen = set()

        while n != 1:
            if n in seen:
                return False

            seen.add(n)
            n = repeat(n)

        return True