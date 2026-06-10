class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # word = "balloon"
        # word = "".join(sorted(word))
        # dummy = ""
        # count = 0

        # for i in text:
        #     if dummy == word:
        #         count += 1
        #         dummy = ""
        #     if i in word:
        #         dummy += i
        #         text.remove(i)
        # return count

        words = "balloon"
        dummy = ""
        count = 0
        while True:
            for i in words:
                if dummy == words:
                    count += 1
                    dummy = ""
                if i in text:
                    dummy += i
                    text = text.replace(i,"",1)
                else:
                    return count
            
            
        