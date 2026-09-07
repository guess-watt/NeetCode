class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        bcount,wcount = 0,0
        # for i in range(len(blocks)):
        #     if block[i] == "B":
        #         bcount += 1
        #     else:
        #         wcount += 1
            
        #     if 
        left = 0
        right = 0
        result = 101
        while left <= right and right <= len(blocks)-1:
            if blocks[right] == "B":
                bcount += 1
            else:
                wcount += 1
            
            if bcount+wcount == k:
                result = min(result,wcount) 
                if blocks[left ] == "B":
                    bcount -= 1
                else:
                    wcount -= 1


                left += 1

            right += 1

        return result