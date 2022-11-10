class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        from functools import lru_cache
        @lru_cache(maxsize=None)
        def rec(i,j):
            """i and j are indices, both inclusive"""

            if i == m or j==n:
                return 0

            a = rec(i+1, j+1)
            b = rec(i+1, j)
            c = rec(i, j+1)

            if A[i]==B[j]:
                a+=1

            return max(a, b, c)

        m, n = len(A), len(B)
        return rec(0, 0)