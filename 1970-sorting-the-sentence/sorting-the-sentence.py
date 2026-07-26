class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        t = [""] * len(words)

        for word in words:
            char = ""

            for ch in word:
                if ch.isalpha():
                    char += ch
                else:
                    index = int(ch) - 1
                    t[index] = char

        return " ".join(t)
            
