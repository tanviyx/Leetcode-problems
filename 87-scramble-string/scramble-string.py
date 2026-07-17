from functools import lru_cache

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:

        @lru_cache(None)
        def dfs(a, b):
            # If they are already equal
            if a == b:
                return True

           
            if sorted(a) != sorted(b):
                return False

            n = len(a)

            # Try every possible split
            for i in range(1, n):

                # Case 1: No swap
                if dfs(a[:i], b[:i]) and dfs(a[i:], b[i:]):
                    return True

                # Case 2: Swap
                if dfs(a[:i], b[n-i:]) and dfs(a[i:], b[:n-i]):
                    return True

            return False

        return dfs(s1, s2)

        