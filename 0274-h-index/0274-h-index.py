class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)

        for i, cit in enumerate(citations):
            if cit >= n-i:
                return n - i

        return 0
        