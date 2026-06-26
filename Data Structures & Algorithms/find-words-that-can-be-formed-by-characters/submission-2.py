class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        # count = 0
        # for i in words:
        #     dummy = list(chars)
        #     for j in range(len(i)):
        #         if i[j] not in dummy:
        #             break
        #         else:
        #             dummy.remove(i[j])
        #     else:
        #         count = count + len(i)
        # return count
        # correct but expensive since .remove in every iter.

        from collections import Counter

        char_count = Counter(chars)
        result = 0

        for word in words:
            word_count = Counter(word)

            for ch, freq in word_count.items():
                if freq > char_count[ch]:
                    break
            else:
                result += len(word)

        return result




            
            

            
            
        