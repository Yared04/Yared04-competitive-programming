class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)
        for idx,char in enumerate(shortest):
            for word in strs:
                if word[idx] != char:
                    return shortest[:idx]
        return shortest
        
