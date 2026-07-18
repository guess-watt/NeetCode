class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)):

            for j in range(i+1,len(words)):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    count += 1
        return count

        """
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                a = words[i]
                b = words[j]

                if len(a) <= len(b):
                    if b[:len(a)] == a and b[-len(a):] == a:
                        count += 1

        return count

        without using startwith() endswith()
        """