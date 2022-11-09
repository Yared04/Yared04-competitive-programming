class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        bucket = [0] * (n+1)
        for cit in citations:
            if cit > n:
                bucket[n] += 1
            else:
                bucket[cit] += 1
        
        h_index = 0
        
        for i in range(n, -1, -1):
            h_index += bucket[i]
            if h_index >= i:
                return i
        