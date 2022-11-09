class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        h = []
        for key, val in freq.items():
            heappush(h,(val,key))
            
        result =[]
        while len(h) > k:
            heapq.heappop(h)
            
        for i in range(len(h)):
            result.append(h[i][1])
           
        return result