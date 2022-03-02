class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)        
        heap=[]
        for key, val in freq.items():
            heap.append((-val, key))
        heapq.heapify(heap)
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        
        
        return result