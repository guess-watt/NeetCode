class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        limit = num // 2
        if num == 1:
            return True
        i = 2
        while i <= limit:
            if i*i == num:
                return True
            i += 1
        return False

        