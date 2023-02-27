class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        @lru_cache(None)
        def check(i, j, k):
            if i >= len(s1) and j >= len(s2):
                return True

            res = False
            if i < len(s1) and s1[i] == s3[k]:
                res |= check(i+1, j, k+1)
            if j < len(s2) and s2[j] == s3[k]:
                res |= check(i, j+1, k+1)
    
            return res
        return check(0,0,0)
            
                