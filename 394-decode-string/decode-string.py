class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current = ""
        num = 0

        for ch in s:

            # Build the complete number (handles 12[a], 100[bc], etc.)
            if ch.isdigit():
                num = num * 10 + int(ch)

            # Start of a new encoded string
            elif ch == '[':
                stack.append((current, num))
                current = ""
                num = 0

            # End of the current encoded string
            elif ch == ']':
                prev, repeat = stack.pop()
                current = prev + current * repeat

            # Normal character
            else:
                current += ch

        return current


