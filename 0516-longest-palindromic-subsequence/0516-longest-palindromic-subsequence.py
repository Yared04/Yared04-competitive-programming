class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        len_s = len(s)
        @lru_cache(None)
        def topDown(ptr1, ptr2):
            if ptr1 > ptr2:
                return 0
            elif ptr1 == ptr2:
                return 1
            if s[ptr1] == s[ptr2]:
                return 2 + topDown(ptr1 + 1, ptr2 - 1)
            return max(topDown(ptr1, ptr2 - 1), topDown(ptr1 + 1, ptr2))
        return topDown(0,len_s - 1)
            
        