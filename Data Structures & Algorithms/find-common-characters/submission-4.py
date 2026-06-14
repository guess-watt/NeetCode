class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # words = sorted(words, key=len)
        # result = []
        # for i in words[0]:
        #     for j in range(1,len(words)):
        #         if i not in words[j]:
        #             break
        #         else:
        #             words[j]=words[j].replace(i,"",1)
        #     else:
        #         result.append(i)        #for - else loop working is based on the inner break condition. if we 
        #                                 #  reach inner break, outer else will not work. 
            
        # return result
            
        from collections import Counter

        common = Counter(words[0])

        for word in words[1:]:
            common &= Counter(word)     # & is diff based on DT, so here it return the minimum no. of apperance

        result = []

        for ch, freq in common.items():
            result.extend([ch]*freq)    #extend add all elements of a list into other list
        return result


        