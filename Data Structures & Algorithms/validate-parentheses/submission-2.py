class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        reference = ""
        left = "([{"
        right = ")}]"
        for i in s:
            if i in left:
                stack.append(i)
            else:
                if not stack:
                    return False
                reference += stack[-1]
                reference += i
                if reference == "{}" or reference == "[]" or reference == "()":
                    stack.pop()
                else:
                    return False
                reference = ""
        return len(stack)==0
