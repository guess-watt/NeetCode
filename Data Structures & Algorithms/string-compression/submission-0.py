class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1

        ref = chars[0]
        count = 1
        op = ""

        for i in range(1, len(chars)):
            if chars[i] == ref:
                count += 1
            else:
                op += ref

                if count > 1:
                    op += str(count)

                ref = chars[i]
                count = 1

        # Add the last group
        op += ref

        if count > 1:
            op += str(count)

        # Copy compressed result into chars
        for i in range(len(op)):
            chars[i] = op[i]

        return len(op)

        