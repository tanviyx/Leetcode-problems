class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:

        ones = s.count('1')

        # augment
        t = "1" + s + "1"

        # Run-length encoding
        blocks = []
        i = 0
        while i < len(t):
            j = i
            while j < len(t) and t[j] == t[i]:
                j += 1
            blocks.append((t[i], j - i))
            i = j

        gain = 0

        # look for 0-block,1-block,0-block
        for i in range(1, len(blocks)-1):

            if (blocks[i][0] == '1' and
                blocks[i-1][0] == '0' and
                blocks[i+1][0] == '0'):

                gain = max(gain,
                           blocks[i-1][1] + blocks[i+1][1])

        return ones + gain
