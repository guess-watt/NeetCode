class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        valid = 0
        a = 0
        while a < len(flowerbed):
        #     if flowerbed[a] == 1:
        #         a = a+2
        #     else:
        #         if flowerbed[a+1] == 0:
        #             valid += 1
        #         a += 1
        # if flowerbed[-1] == 0 and flowerbed[-2] == 0:
        #     valid += 1
        # if n <= valid:
        #     return True
        # else:return False

            if flowerbed[a] == 0:

                left = (a == 0 or flowerbed[a-1] == 0)
                right = (a == len(flowerbed)-1 or flowerbed[a+1] == 0)

                if left and right:
                    flowerbed[a] = 1
                    valid += 1

            a += 1

        if n <= valid:
            return True
        else:
            return False
            
        