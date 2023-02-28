class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        @lru_cache(None)
        def check(i, j):
            if j >= len(t):
                return 1
            
            res = 0
            if i < len(s):
                if s[i] == t[j]:
                    res += check(i + 1, j + 1)
                res += check(i + 1, j)
            return res
            
                
        return check(0,0)
