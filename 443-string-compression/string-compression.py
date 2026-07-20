class Solution:
    def compress(self, chars: List[str]) -> int:
        comp = chars[0]
        count = 0
        s = ""

        for ch in chars:
            if ch == comp:
                count += 1
            else:
                if count == 1:
                    s += comp
                else:
                    s += comp + str(count)

                comp = ch
                count = 1

        # Don't forget the last group
        if count == 1:
            s += comp
        else:
            s += comp + str(count)

        chars[:] = list(s)
        return len(chars)