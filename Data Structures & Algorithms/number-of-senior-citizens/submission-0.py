class Solution:
    def countSeniors(self, details: List[str]) -> int:
        result = 0
        for i in details:
            a = i[11:13]
            if int(a)>60:
                result += 1
        return result
