class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        @lru_cache(None)
        def checkValidity(w):
            count = 0
            for i in range(len(w)):
                pre = w[:i] + w[i+1:]
                if pre in seen:
                    count = max(count, checkValidity(pre))
            return 1 + count

        ans = 0
        seen = set(words)
        for word in words:
            ans = max(ans, checkValidity(word))
        return ans