class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        # Stores indices of unmatched '('
        stack = []

        # Stores indices to remove
        remove = set()

        # Traverse the string
        for i, ch in enumerate(s):

            if ch == '(':
                stack.append(i)

            elif ch == ')':

                # Matching '(' exists
                if stack:
                    stack.pop()

                # Unmatched ')'
                else:
                    remove.add(i)

        # Remaining '(' are unmatched
        while stack:
            remove.add(stack.pop())

        # Build answer excluding removed indices
        ans = []

        for i, ch in enumerate(s):
            if i not in remove:
                ans.append(ch)

        return "".join(ans)