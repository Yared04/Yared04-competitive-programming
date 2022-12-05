class Solution:
    def countArrangement(self, n: int) -> int:
        @lru_cache(None)
        def backtrack(pl, visited):
            if pl == 0:
                return 1
            beautiful_arr = 0
            for i in range(1, n+1):
                if not visited & 1<<i-1 and (i % pl == 0 or pl % i == 0):
                    visited ^= 1<<i-1
                    beautiful_arr += backtrack(pl - 1, visited)
                    visited ^= 1<<i-1
            return beautiful_arr       
        return backtrack(n, 0)
                    
        