class Solution:
    def isValid(self, s: str) -> bool:

        pairs = {
            '(':')',
            '[':']',
            '{':'}'
        }
        stack = []
        for i in s:
            if i in pairs:
                stack.append(i)
            else:
                if not stack:
                    return False
                if i == pairs[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

        # ANOTHER APPROACH

        # stack = []
        # reference = ""
        # left = "([{"
        # right = ")}]"
        # for i in s:
        #     if i in left:
        #         stack.append(i)
        #     else:
        #         if not stack:
        #             return False
        #         reference += stack[-1]
        #         reference += i
        #         if reference == "{}" or reference == "[]" or reference == "()":
        #             stack.pop()
        #         else:
        #             return False
        #         reference = ""
        # return len(stack)==0
