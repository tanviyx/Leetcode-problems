class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        longp = ""
        p = ""

        n = len(strs)

        for i in range(len(strs[0])):

            ch = strs[0][i]

            for k in range(1, n):

                if i < len(strs[k]) and strs[k][i] == ch:
                    continue
                else:
                    return longp

            p += ch

            if len(p) > len(longp):
                longp = p

        return longp


