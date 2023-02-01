class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        heap = []
        for idx, growth in enumerate(growTime):
            heappush(heap, (-growth, idx))
        end, start = 0, -1
        while heap:
            growth, index = heappop(heap)
            start += plantTime[index]
            end = max(end, start + (-growth))
        return end + 1