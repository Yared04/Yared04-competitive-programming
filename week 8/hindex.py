class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        for idx, val in enumerate(citations):
            if len(citations) - idx <= val:
                return len(citations) - idx
        return 0
        