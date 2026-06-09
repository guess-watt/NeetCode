class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        result = {}
        ans = []
        for i in range(len(heights)):
            result[heights[i]] = names[i]
        sort_res = sorted(result.items(),key=lambda x:x[0],reverse=True)
        for value in sort_res:
            ans.append(value[1])
        return ans



        