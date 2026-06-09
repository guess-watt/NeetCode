class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        result = {}
        ans = []
        for i in range(len(heights)):
            result[heights[i]] = names[i]
        sort_res = sorted(result.items(),key=lambda x:x[0],reverse=True)    #for sorting based on the key and reverse it. return type is list not dict
        for value in sort_res:
            ans.append(value[1])
        return ans



        